#!/usr/bin/env python3
"""Раскладка Instagram по правилам проекта (решение пользователя 11.10.2026: «чёткая раскладка, процесс автоматизировать»).

python3 CONTROL/TOOLS/instagram_plan.py GTT              # показать календарь (ничего не меняет)
python3 CONTROL/TOOLS/instagram_plan.py GTT --apply      # разложить: даты в именах, тексты Reels/Stories, анонсы, КАЛЕНДАРЬ.md
python3 CONTROL/TOOLS/instagram_plan.py GTT --html out.html   # календарь с картинками (показать пользователю)

Правила — `<ПРОЕКТ>/INSTAGRAM/PLAN.json`.
**Даты можно не назначать** (решение пользователя 11.10.2026: «пока не ставь время… время определим позже»): при `"start": null`
план — только порядок: файлы называются `NNN_тема` (NNN — номер публикации по порядку), в шапке `order` и `day`
(«День N» от старта), времени и даты нет; такие посты `to_ready.py` в очередь не переносит — выйти они не могут.
Когда пользователь назначит старт и время — `start`, `time` в `launch` и `rhythm` → `--apply` переименует в `ГГГГ-ММ-ДД_ЧЧММ_тема`.
- `launch` — публикации вручную (`day` — день от старта или `date`, `time`, type, carousel / reels; `rubric` — своя рубрика,
  `launch: false` — не «первый запуск», `week` — к какой неделе отнести, `part` — утро / день / вечер, пока нет времени); план из одних таких записей — `weeks: 0` (так у Aura); `week` у них занимает слоты этой недели;
- `weeks_from_day` (день от старта) или `weeks_from` (дата), `weeks`, `rhythm` — неделя (без даты старта первый день считается воскресеньем): день (пн…вс), время, type: `carousel` (pool: theme / china / asia …),
  `anons` (Stories-анонс карусели недели), `reels` (ролик недели), `reels_stories` (две части ролика недели в Stories);
- `theme_weeks` — по неделе: [номер карусели, ролик или null]; `pools` — очереди каруселей по номерам;
- `moves` — праздники: дата → куда перенести (`ГГГГ-ММ-ДД` или `ГГГГ-ММ-ДД ЧЧ:ММ`; без времени карусель встаёт на 12:00); `reels` — ролики (файл в VIDEO-HUB, название, длина);
- `anons` — заголовок анонса и плашка для недели без ролика.
Что делает --apply (файлы только переносятся `git mv`, не удаляются):
- карусели `CAROUSEL/TEXT|PHOTO/<имя>` → `ГГГГ-ММ-ДД_ЧЧММ_тема`, в шапке date, time, rubric, week, launch, связка anons / reels;
- Reels и Stories из роликов: `REELS/TEXT`, `STORIES/TEXT` (подпись Reels не трогается, меняются имя и шапка; новый ролик —
  заготовка «[подпись: уточнить]»); видео — поле `video_hub` (мастер в VIDEO-HUB);
- Stories-анонсы: props `reels-studio/props/announces/<проект>-instagram.json` → `npm run announce` в VIDEO-HUB →
  `STORIES/PHOTO/<имя>/01.jpg` + `STORIES/TEXT/<имя>.md`;
- `<ПРОЕКТ>/INSTAGRAM/КАЛЕНДАРЬ.md` — календарь по неделям.
"""
import argparse
import base64
import datetime as dt
import io
import json
import re
import subprocess
from pathlib import Path

from PIL import Image

HUB = Path(__file__).resolve().parents[2]
VH = Path('/home/user/VIDEO-HUB')
WD = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
DAYS_ACC = ['в понедельник', 'во вторник', 'в среду', 'в четверг', 'в пятницу', 'в субботу', 'в воскресенье']
MON = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
DATED = re.compile(r'^\d{4}-\d{2}-\d{2}_\d{4}_')
PREFIX = re.compile(r'^(\d{4}-\d{2}-\d{2}_\d{4}_|\d{3}_)')     # дата и время или номер по порядку
BASE = dt.date(2000, 1, 2)                                      # воскресенье: опора для плана без дат
LAUNCH = 'первый запуск — тест форматов'


def meta_of(f):
    head, body = f.read_text(encoding='utf-8').split('---\n', 2)[1:]
    return dict(l.split(': ', 1) for l in head.strip().split('\n')), body


def fm(meta, body):
    return '---\n' + '\n'.join(f'{k}: {v}' for k, v in meta.items()) + '\n---\n' + body


def q(v):
    return v if isinstance(v, int) else json.dumps(v, ensure_ascii=False)


class Plan:
    def __init__(self, project):
        self.project = project
        self.ig = HUB / project / 'INSTAGRAM'
        self.cfg = json.loads((self.ig / 'PLAN.json').read_text(encoding='utf-8'))
        self.dated = bool(self.cfg.get('start'))
        self.base = dt.date.fromisoformat(self.cfg['start']) if self.dated else BASE
        self.car = {}
        for f in sorted((self.ig / 'CAROUSEL/TEXT').glob('*.md')):
            m, _ = meta_of(f)
            n = int(m['number'])
            self.car[n] = {'file': f, 'stem': f.stem, 'theme': re.sub(r'^\d+_', '', PREFIX.sub('', f.stem)),
                           'title': json.loads(m['title']), 'vh': json.loads(m.get('video_hub', '""'))}
        for f in sorted((self.ig / 'CAROUSEL/PUBLISHED').glob('*/*/post.md')):   # вышедшие: в плане остаются, файлы не трогаем
            m, _ = meta_of(f)
            n = int(m['number'])
            if n in self.car:
                continue
            info = f.parent / 'info.json'
            self.car[n] = {'file': f, 'stem': f.parent.name, 'theme': re.sub(r'^\d+_', '', PREFIX.sub('', f.parent.name)),
                           'title': json.loads(m['title']), 'vh': json.loads(m.get('video_hub', '""')), 'published': f.parent.name,
                           'url': json.loads(info.read_text(encoding='utf-8')).get('url') if info.exists() else None}
        self.ev = self.build()

    # ——— календарь ———
    def build(self):
        c = self.cfg
        ev = []
        covered = set()
        for e in c['launch']:
            d0 = self.base + dt.timedelta(days=e['day'] - 1) if 'day' in e else dt.date.fromisoformat(e['date'])
            x = {**e, 'date': d0, 'time': e.get('time'), 'launch': e.get('launch', True), 'week': e.get('week', 0)}
            ev.append(x)
            if 'week' in e:
                covered.add((e['week'], e['type']))
        theme = list(c['theme_weeks'])
        pools = {k: list(v) for k, v in c['pools'].items()}
        start = self.base + dt.timedelta(days=c['weeks_from_day'] - 1) if 'weeks_from_day' in c else dt.date.fromisoformat(c['weeks_from'])
        for w in range(1, c['weeks'] + 1):
            no, reels = theme.pop(0) if theme else (None, None)
            monday = start + dt.timedelta(weeks=w - 1)
            for r in c['rhythm']:
                d = monday + dt.timedelta(days=WD.index(r['day']))
                t = r['type']
                if t == 'carousel' and r['pool'] == 'theme':
                    if (w, 'carousel') in covered or no is None:
                        continue
                    ev.append({'date': d, 'time': r.get('time'), 'type': 'carousel', 'carousel': no, 'week': w, 'theme_reels': reels})
                elif t == 'carousel':
                    if pools.get(r['pool']):
                        ev.append({'date': d, 'time': r.get('time'), 'type': 'carousel', 'carousel': pools[r['pool']].pop(0), 'week': w})
                elif t == 'anons':
                    if (w, 'anons') not in covered and no is not None:
                        ev.append({'date': d, 'time': r.get('time'), 'type': 'anons', 'carousel': no, 'week': w, 'theme_reels': reels})
                elif reels and (w, t) not in covered:
                    ev.append({'date': d, 'time': r.get('time'), 'type': t, 'reels': reels, 'week': w, 'carousel_of_week': no})
        moves = {dt.date.fromisoformat(k): v for k, v in c.get('moves', {}).items()} if self.dated else {}
        for e in ev:
            if e['date'] in moves:
                to = moves[e['date']].split()
                e['moved_from'], e['date'] = e['date'], dt.date.fromisoformat(to[0])
                if len(to) > 1:
                    e['time'] = to[1]
                elif e['type'] == 'carousel':
                    e['time'] = '12:00'
        used = [e['carousel'] for e in ev if e['type'] == 'carousel']
        dup = {n for n in used if used.count(n) > 1}
        assert not dup, f'карусели стоят дважды: {sorted(dup)}'
        missing = sorted(set(self.car) - set(used))
        if missing:
            print('⚠ нет в расписании:', ', '.join(f'№{n}' for n in missing))
        part = {'утро': '10', 'день': '13', 'вечер': '19'}               # без времени порядок внутри дня — по `part`
        ev.sort(key=lambda e: (e['date'], e['time'] or part.get(e.get('part'), ''), ['reels', 'carousel', 'anons', 'reels_stories'].index(e['type'])))
        if self.dated:
            no_time = [e for e in ev if not e['time']]
            assert not no_time, f'старт назначен, а время нет у {len(no_time)} публикаций — впиши time в launch и rhythm'
        for i, e in enumerate(ev, 1):
            e['order'], e['day'] = i, (e['date'] - self.base).days + 1
            e['name'] = self.name(e)
            if e['type'] == 'carousel' and not e.get('rubric'):
                asia = any(k in self.car[e['carousel']]['theme'] for k in ('japan', 'thailand', 'vietnam', 'korea', 'uae'))
                e['rubric'] = 'тема недели' if 'theme_reels' in e else 'Азия' if asia else 'Китай'
        return ev

    def name(self, e):
        if e['type'] == 'carousel' and self.car[e['carousel']].get('published'):
            return self.car[e['carousel']]['published']
        pre = f"{e['date'].isoformat()}_{e['time'].replace(':', '')}_" if self.dated else f"{e['order']:03d}_"
        if e['type'] == 'carousel':
            return f"{pre}{self.car[e['carousel']]['theme']}"
        if e['type'] == 'anons':
            return f"{pre}anons-{self.car[e['carousel']]['theme']}"
        return f"{pre}{e['reels']}"

    def find(self, typ, key):
        return next((e for e in self.ev if e['type'] == typ and (e.get('carousel') == key or e.get('reels') == key)), None)

    def model(self, n):
        """«AgiBot A2: гуманоид-рекордсмен» → («AgiBot A2», «Гуманоид-рекордсмен»); без двоеточия — подзаголовок обложки."""
        t = self.car[n]['title']
        if ':' in t:
            a, b = t.split(':', 1)
            return a.strip(), b.strip()[:1].upper() + b.strip()[1:]
        try:
            cover = json.loads((VH / self.car[n]['vh']).read_text(encoding='utf-8'))['slides'][0]
            return t, re.sub(r'\*\*', '', cover.get('text', ''))
        except Exception:
            return t, ''

    def note(self, e):
        if e.get('note'):
            return e['note']
        if self.cfg['anons'].get('model_of_day'):                         # Aura: анонс модели дня — подзаголовок карусели
            return self.model(e['carousel'])[1]
        if not e.get('theme_reels'):
            return self.cfg['anons']['no_reels_note']
        r = self.find('reels', e['theme_reels'])
        if not self.dated:
            n = r['day'] - e['day']
            return {1: 'Завтра', 2: 'Послезавтра'}.get(n, f'Через {n} дн.') + ' — ролик об этом туре'
        when = 'Завтра' if r['date'] - e['date'] == dt.timedelta(days=1) else DAYS_ACC[r['date'].weekday()].capitalize()
        return f"{when} в {r['time']} — ролик об этом туре"

    def label(self, e):
        R = self.cfg['reels']
        if e['type'] == 'carousel':
            done = f" · ✓ вышла {self.car[e['carousel']]['url'] or ''}".rstrip() if self.car[e['carousel']].get('published') else ''
            return 'Карусель', f"№{e['carousel']} {self.car[e['carousel']]['title']}{done}"
        if e['type'] == 'reels':
            return 'Reels', R[e['reels']]['title']
        if e['type'] == 'anons':
            same = ' (одновременно с каруселью)' if e.get('launch') else ''
            if self.cfg['anons'].get('model_of_day'):
                return 'Stories', f"{self.cfg['anons'].get('kicker', 'Модель дня')}: {self.model(e['carousel'])[0]} · «{self.note(e)}»"
            return 'Stories', f"анонс карусели №{e['carousel']} · «{self.note(e)}»{same}"
        return 'Stories ×2', f"части ролика «{R[e['reels']]['title']}»"

    def table(self):
        out = []
        for e in self.ev:
            kind, what = self.label(e)
            mv = f" (перенос с {e['moved_from'].strftime('%d.%m')})" if e.get('moved_from') else ''
            when = f"{e['date'].strftime('%d.%m')} {WD[e['date'].weekday()]} {e['time']}" if self.dated else f"{e['order']:03d} · день {e['day']:>3}" + (f" · {e['part']}" if e.get('part') else '')
            out.append(f"{when} | {kind:<10} | {what}{mv}")
        n = lambda t: sum(e['type'] == t for e in self.ev)
        out.append(f"Итого: каруселей {n('carousel')}, Reels {n('reels')}, Stories из роликов {n('reels_stories')}, анонсов {n('anons')}.")
        return out

    # ——— применить ———
    def mv(self, a, b):
        if a == b or not Path(a).exists():
            return
        r = subprocess.run(['git', 'mv', str(a), str(b)], cwd=HUB, capture_output=True)
        if r.returncode:                                                 # не в git (пустая папка, новый файл) — просто переносим
            if Path(b).exists() and Path(b).is_dir() and not any(Path(a).iterdir()):
                Path(a).rmdir()
            else:
                Path(a).rename(b)

    def existing(self, folder, suffix):
        """Файл в TEXT, имя которого (без даты) равно suffix."""
        return next((f for f in sorted((self.ig / folder / 'TEXT').glob('*.md')) if PREFIX.sub('', f.stem) == suffix), None)

    def links(self, e):
        out = {}
        if e['type'] == 'carousel' and e.get('theme_reels'):
            a = self.find('anons', e['carousel'])
            out['anons'] = a['name'] if a else None
            out['reels'] = self.find('reels', e['theme_reels'])['name']
        if e['type'] in ('reels', 'reels_stories', 'anons'):
            no = e.get('carousel') if e['type'] == 'anons' else e.get('carousel_of_week')
            if no and self.find('carousel', no):
                out['carousel'] = self.find('carousel', no)['name']
        if e['type'] in ('reels_stories', 'anons') and (e.get('reels') or e.get('theme_reels')):
            r = self.find('reels', e.get('reels') or e.get('theme_reels'))
            if r:
                out['reels'] = r['name']
        return {k: v for k, v in out.items() if v}

    def head(self, e):
        when = {'date': e['date'].isoformat(), 'time': e['time']} if self.dated else {'order': e['order'], 'day': e['day']}
        h = {**when, 'rubric': e.get('rubric') or {
            'reels': 'тема недели' if e['week'] else 'знакомство', 'anons': 'анонс карусели',
            'reels_stories': 'части ролика недели' if e['week'] else 'знакомство'}[e['type']], 'week': e['week']}
        if e.get('launch'):
            h['launch'] = LAUNCH + (', выходит одновременно с каруселью' if e['type'] == 'anons' else '')
        if e.get('moved_from'):
            h['moved_from'] = e['moved_from'].isoformat()
        return h

    def apply(self):
        R = self.cfg['reels']
        anons = [e for e in self.ev if e['type'] == 'anons']
        if self.dated:                                                   # без времени анонс не рисуем: в нём «Завтра в 19:00»
            self.render_anons(anons)
        for e in self.ev:
            n = e['name']
            h = {**self.head(e), **self.links(e)}
            if e['type'] == 'carousel' and self.car[e['carousel']].get('published'):
                continue                                                 # уже вышла — архив не трогаем
            fmt_dir = {'reels': 'REELS', 'reels_stories': 'STORIES', 'anons': 'STORIES'}.get(e['type'])
            if fmt_dir and any((self.ig / fmt_dir / 'PUBLISHED').glob(f'*/{n}')):
                continue                                                 # Reels / Stories уже вышли — черновик заново не создаём
            if e['type'] == 'carousel':
                c = self.car[e['carousel']]
                self.mv(self.ig / 'CAROUSEL/PHOTO' / c['stem'], self.ig / 'CAROUSEL/PHOTO' / n)
                self.mv(c['file'], self.ig / 'CAROUSEL/TEXT' / f'{n}.md')
                f = self.ig / 'CAROUSEL/TEXT' / f'{n}.md'
                m, body = meta_of(f)
                for k in ('date', 'time', 'order', 'day', 'rubric', 'week', 'launch', 'moved_from', 'anons', 'reels'):
                    m.pop(k, None)
                m['image'] = q(n)
                order = {'number': m.pop('number')}
                order.update({k: q(v) for k, v in h.items() if k not in ('anons', 'reels')})
                order.update(m)
                order.update({k: q(h[k]) for k in ('anons', 'reels') if k in h})
                f.write_text(fm(order, body), encoding='utf-8')
            elif e['type'] == 'reels':
                old = self.existing('REELS', e['reels'])
                f = self.ig / 'REELS/TEXT' / f'{n}.md'
                body = '[подпись: уточнить]\n'
                if old:
                    self.mv(old, f)
                    body = meta_of(f)[1]
                r = R[e['reels']]
                m = {'number': list(R).index(e['reels']) + 1, **h, 'title': r['title'],
                     'video_hub': f"finished-videos/{r['video']}.mp4", 'duration': f"{r['seconds']} с",
                     'video_status': 'мастер в VIDEO-HUB; копия в REELS/VIDEO — по решению пользователя',
                     'music': r.get('music') or self.cfg.get('music', ''), 'caption_status': 'черновик по тексту ролика, на согласовании'}
                if r.get('guest'):
                    m['guest'] = r['guest']
                if old:
                    om, _ = meta_of(f)
                    m['caption_status'] = json.loads(om.get('caption_status', json.dumps(m['caption_status'])))
                f.write_text(fm({k: q(v) for k, v in m.items() if v != ''}, body), encoding='utf-8')
            elif e['type'] == 'reels_stories':
                old = self.existing('STORIES', e['reels'])
                f = self.ig / 'STORIES/TEXT' / f'{n}.md'
                if old:
                    self.mv(old, f)
                r = R[e['reels']]
                parts = sorted(p.name for p in (VH / 'finished-videos').glob(f"{r['video']}-stories-[0-9].mp4"))
                m = {k: q(v) for k, v in h.items()}
                m['title'] = q(f"Stories: части ролика «{r['title']}»")
                m['video_hub'] = '[' + ', '.join(q(f'finished-videos/{p}') for p in parts) + ']'
                m['video_status'] = q('мастер в VIDEO-HUB; копия в STORIES/VIDEO — по решению пользователя')
                f.write_text(fm(m, ''), encoding='utf-8')
            else:                                                        # анонс
                theme = self.car[e['carousel']]['theme']
                old = self.existing('STORIES', f'anons-{theme}')
                f = self.ig / 'STORIES/TEXT' / f'{n}.md'
                if old:
                    self.mv(old, f)
                    self.mv(self.ig / 'STORIES/PHOTO' / old.stem, self.ig / 'STORIES/PHOTO' / n)
                i = anons.index(e) + 1
                dst = self.ig / 'STORIES/PHOTO' / n
                dst.mkdir(parents=True, exist_ok=True)
                if self.dated:
                    Image.open(self.anons_png(i)).convert('RGB').save(dst / '01.jpg', quality=92, optimize=True)
                m = {k: q(v) for k, v in h.items()}
                m['title'] = q(f"{'Модель дня' if self.cfg['anons'].get('model_of_day') else 'Анонс карусели'} №{e['carousel']} «{self.car[e['carousel']]['title']}»")
                m['image'] = q(n)
                m['note'] = q(self.note(e))
                m['video_hub'] = q(f'finished-videos/анонсы/{self.ann_name()}/{i:02d}.png')
                m['image_status'] = q('на согласовании' if self.dated else 'перерисовать после назначения времени')
                m['image_cost'] = q('0')
                f.write_text(fm(m, ''), encoding='utf-8')
        (self.ig / 'КАЛЕНДАРЬ.md').write_text(self.markdown(), encoding='utf-8')
        print('разложено:', len(self.ev), 'публикаций; календарь —', (self.ig / 'КАЛЕНДАРЬ.md').relative_to(HUB))

    # ——— анонсы ———
    def ann_name(self):
        return f'{self.project.lower()}-instagram'

    def anons_png(self, i):
        return VH / 'finished-videos/анонсы' / self.ann_name() / f'{i:02d}.png'

    def render_anons(self, anons):
        stories = []
        for e in anons:
            d = Path(self.car[e['carousel']]['vh']).stem                 # 2026-10-10-foto-<тема>
            base = f'finished-videos/карусели/{d}'
            st = {'cover': f'{base}/01.png', 'back': [f'{base}/02.png', f'{base}/03.png'],
                  'title': e.get('title') or self.cfg['anons']['title'], 'note': self.note(e)}
            if self.cfg['anons'].get('model_of_day') and not e.get('title'):
                st['title'] = f"**{self.model(e['carousel'])[0]}**"
            if e.get('kicker') or self.cfg['anons'].get('kicker'):
                st['kicker'] = e.get('kicker') or self.cfg['anons']['kicker']
            stories.append(st)
        props = {'brand': self.project.lower(), 'stories': stories}
        p = VH / 'reels-studio/props/announces' / f'{self.ann_name()}.json'
        text = json.dumps(props, ensure_ascii=False, indent=2) + '\n'
        fresh = all(self.anons_png(i).exists() for i in range(1, len(stories) + 1))
        if p.exists() and p.read_text(encoding='utf-8') == text and fresh:
            return
        p.write_text(text, encoding='utf-8')
        subprocess.run(['npm', 'run', '-s', 'announce', '--', self.ann_name()], cwd=VH / 'reels-studio', check=True)

    # ——— календарь для людей ———
    @staticmethod
    def group(e):
        return 0 if e.get('launch') else e['week']

    def markdown(self):
        lines = [f'# Календарь Instagram {self.project}', '',
                 f'Собран командой `python3 CONTROL/TOOLS/instagram_plan.py {self.project} --apply` из `PLAN.json` '
                 '(правила — `RULES.md`, «Время публикаций»). Время — по Москве. Руками не править: меняй `PLAN.json` и запускай заново.', '']
        if not self.dated:
            lines += ['**Даты и время не назначены** (решение пользователя 11.10.2026) — ниже только порядок публикаций и день от старта. '
                      'Без даты пост не может попасть в очередь и выйти.', '']
        week = None
        for e in self.ev:
            if self.group(e) != week:
                week = self.group(e)
                title = 'Первый запуск — тест форматов (Reels → карусель + Stories → Stories)' if week == 0 else f'Неделя {week}'
                th = next((x for x in self.ev if x['week'] == week and x['type'] == 'carousel' and 'theme_reels' in x), None)
                if week and th:
                    title += f" — тема: №{th['carousel']} {self.car[th['carousel']]['title']}"
                    title += ' (карусель — в первом запуске)' if th.get('launch') else ''
                lines += ['', f'## {title}', '', ('| Дата | Время | Формат | Что | Файл |' if self.dated else '| № | День | Формат | Что | Файл |'), '|---|---|---|---|---|']
            kind, what = self.label(e)
            mark = ' · тест' if e.get('launch') else ''
            mv = f" · перенос с {e['moved_from'].strftime('%d.%m')}" if e.get('moved_from') else ''
            folder = {'carousel': 'CAROUSEL', 'reels': 'REELS'}.get(e['type'], 'STORIES')
            when = f"{WD[e['date'].weekday()]} {e['date'].day} {MON[e['date'].month]} | {e['time']}" if self.dated else f"{e['order']:03d} | День {e['day']}" + (f", {e['part']}" if e.get('part') else '')
            lines.append(f"| {when} | {kind}{mark} | "
                         f"{what.replace('|', '/')}{mv} | `{folder}/TEXT/{e['name']}.md` |")
        lines += ['', self.table()[-1], '']
        return '\n'.join(lines)

    @staticmethod
    def frame(video, at):
        """Кадр ролика для превью (кэш во временной папке)."""
        import tempfile
        src = VH / 'finished-videos' / f'{video}.mp4'
        dst = Path(tempfile.gettempdir()) / f'ig-frame-{video}-{at:g}.jpg'
        if src.exists() and src.stat().st_size > 1_000_000 and not dst.exists():
            subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(at), '-i', str(src), '-frames:v', '1', '-vf', 'scale=270:-1', '-y', str(dst)])
        return dst if dst.exists() else None

    def html(self, out):
        def thumb(path, w=150):
            if not path or not Path(path).exists():
                return ''
            im = Image.open(path).convert('RGB')
            im.thumbnail((w, w * 2))
            b = io.BytesIO()
            im.save(b, 'JPEG', quality=70)
            return f'<img src="data:image/jpeg;base64,{base64.b64encode(b.getvalue()).decode()}">'
        anons = [e for e in self.ev if e['type'] == 'anons']
        R = self.cfg['reels']
        cards, week = [], None
        for e in self.ev:
            if self.group(e) != week:
                week = self.group(e)
                title = 'Первый запуск — тест форматов' if week == 0 else f'Неделя {week}'
                th = next((x for x in self.ev if x['week'] == week and x['type'] == 'carousel' and 'theme_reels' in x), None)
                if week and th:
                    title += f" · тема — {self.car[th['carousel']]['title']}"
                cards.append(f'<h2>{title}</h2>')
            kind, what = self.label(e)
            if e['type'] == 'carousel':
                img = thumb(self.ig / 'CAROUSEL/PHOTO' / self.car[e['carousel']]['stem'] / '01.jpg')
                if not img:
                    img = thumb(self.ig / 'CAROUSEL/PHOTO' / e['name'] / '01.jpg')
            elif e['type'] == 'anons':
                img = thumb(self.anons_png(anons.index(e) + 1), 110)
            else:
                img = thumb(self.frame(R[e['reels']]['video'], 2.0 if e['type'] == 'reels' else 30.0), 110)
            link = ''
            if e['type'] == 'reels':
                link = f'<a class="l" href="https://media.githubusercontent.com/media/Ostap-87/VIDEO-HUB/main/finished-videos/{R[e["reels"]]["video"]}.mp4">смотреть ролик ↗</a>'
            elif e['type'] == 'carousel':
                stem = Path(self.car[e['carousel']]['vh']).stem
                link = f'<a class="l" href="https://raw.githubusercontent.com/Ostap-87/VIDEO-HUB/main/finished-videos/карусели/{stem}/_лист.jpg">все слайды ↗</a>'
            cls = {'carousel': 'car', 'reels': 'rl', 'anons': 'st', 'reels_stories': 'st'}[e['type']]
            tag = '<span class="t">тест</span>' if e.get('launch') else ''
            mv = f'<div class="mv">перенос с {e["moved_from"].strftime("%d.%m")}</div>' if e.get('moved_from') else ''
            when = (f'{WD[e["date"].weekday()]}, {e["date"].day} {MON[e["date"].month]} · <b>{e["time"]}</b>' if self.dated
                    else f'№{e["order"]} · <b>День {e["day"]}</b>' + (f', {e["part"]}' if e.get('part') else ''))
            cards.append(f'<div class="c {cls}"><div class="d">{when}'
                         f'</div><div class="k">{kind}{tag}</div>{img}<div class="w">{what}</div>{link}{mv}</div>')
        rhythm = self.cfg.get('_', '').split(' Меняешь здесь')[0]
        page = f'''<title>Календарь Instagram {self.project}</title><style>
:root{{--bg:#f4f5f8;--card:#fff;--ink:#17171d;--mute:#6b6b76;--line:#e3e3ea;--car:#2563eb;--rl:#e11d48;--st:#f59e0b}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111216;--card:#1b1c22;--ink:#ececf1;--mute:#9a9aa6;--line:#2c2d35;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111216;--card:#1b1c22;--ink:#ececf1;--mute:#9a9aa6;--line:#2c2d35;color-scheme:dark}}
.l{{display:inline-block;margin-top:6px;font-size:12px;color:var(--car);text-decoration:none}}.l:hover{{text-decoration:underline}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:14px/1.4 -apple-system,Segoe UI,Roboto,sans-serif;padding:20px 16px 48px}}
h1{{margin:0 0 4px;font-size:24px}}.sub{{color:var(--mute);margin:0 0 8px;max-width:960px}}.lg span{{margin-right:16px}}.lg i{{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px}}
h2{{grid-column:1/-1;margin:22px 0 2px;font-size:17px}}.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px}}
.c{{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--car);border-radius:12px;padding:10px}}
.c.rl{{border-top-color:var(--rl)}}.c.st{{border-top-color:var(--st)}}.d{{color:var(--mute);font-size:12px}}.k{{font-weight:700;margin:2px 0 6px}}
.c img{{display:block;max-width:100%;max-height:200px;border-radius:8px;margin:0 auto 6px}}.w{{font-size:13px}}.mv{{color:var(--rl);font-size:12px;margin-top:4px}}
.t{{background:var(--rl);color:#fff;border-radius:4px;padding:0 5px;font-size:11px;margin-left:6px;font-weight:600}}
</style><h1>Календарь Instagram {self.project}</h1>
<p class="sub">{(f'С {self.base.day} {MON[self.base.month]}, время по Москве.' if self.dated else '<b>Даты и время не назначены</b> — порядок публикаций и день от старта.')} Выходит только утверждённое. {rhythm or 'Неделя = один тур: пн карусель → вт Stories-анонс → ср Reels того же тура; чт карусель Китая, пт две части ролика в Stories, сб карусель Азии, вс пусто.'} {self.table()[-1]}</p>
<p class="sub lg"><span><i style="background:var(--car)"></i>карусель</span><span><i style="background:var(--rl)"></i>Reels</span><span><i style="background:var(--st)"></i>Stories</span></p>
<div class="g">{"".join(cards)}</div>'''
        Path(out).write_text(page, encoding='utf-8')
        print('календарь →', out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('project', choices=['GTT', 'AURA'])
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--html')
    a = ap.parse_args()
    p = Plan(a.project)
    if a.apply:
        p.apply()
        p = Plan(a.project)
    if a.html:
        p.html(a.html)
    if not a.apply and not a.html:
        print('\n'.join(p.table()))


if __name__ == '__main__':
    main()
