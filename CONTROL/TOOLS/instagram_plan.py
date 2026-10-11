#!/usr/bin/env python3
"""Раскладка Instagram по правилам проекта (решение пользователя 11.10.2026: «чёткая раскладка, процесс автоматизировать»).

python3 CONTROL/TOOLS/instagram_plan.py GTT              # показать календарь (ничего не меняет)
python3 CONTROL/TOOLS/instagram_plan.py GTT --apply      # разложить: даты в именах, тексты Reels/Stories, анонсы, КАЛЕНДАРЬ.md
python3 CONTROL/TOOLS/instagram_plan.py GTT --html out.html   # календарь с картинками (показать пользователю)

Правила — `<ПРОЕКТ>/INSTAGRAM/PLAN.json`:
- `launch` — первые публикации вручную (дата, время, type, carousel / reels); `week` у них занимает слоты этой недели;
- `weeks_from`, `weeks`, `rhythm` — неделя: день (пн…вс), время, type: `carousel` (pool: theme / china / asia …),
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
        self.car = {}
        for f in sorted((self.ig / 'CAROUSEL/TEXT').glob('*.md')):
            m, _ = meta_of(f)
            n = int(m['number'])
            self.car[n] = {'file': f, 'stem': f.stem, 'theme': DATED.sub('', re.sub(r'^\d+_', '', f.stem)),
                           'title': json.loads(m['title']), 'vh': json.loads(m.get('video_hub', '""'))}
        self.ev = self.build()

    # ——— календарь ———
    def build(self):
        c = self.cfg
        ev = []
        covered = set()
        for e in c['launch']:
            x = {**e, 'date': dt.date.fromisoformat(e['date']), 'launch': True, 'week': e.get('week', 0)}
            ev.append(x)
            if 'week' in e:
                covered.add((e['week'], e['type']))
        theme = list(c['theme_weeks'])
        pools = {k: list(v) for k, v in c['pools'].items()}
        start = dt.date.fromisoformat(c['weeks_from'])
        for w in range(1, c['weeks'] + 1):
            no, reels = theme.pop(0) if theme else (None, None)
            monday = start + dt.timedelta(weeks=w - 1)
            for r in c['rhythm']:
                d = monday + dt.timedelta(days=WD.index(r['day']))
                t = r['type']
                if t == 'carousel' and r['pool'] == 'theme':
                    if (w, 'carousel') in covered or no is None:
                        continue
                    ev.append({'date': d, 'time': r['time'], 'type': 'carousel', 'carousel': no, 'week': w, 'theme_reels': reels})
                elif t == 'carousel':
                    if pools.get(r['pool']):
                        ev.append({'date': d, 'time': r['time'], 'type': 'carousel', 'carousel': pools[r['pool']].pop(0), 'week': w})
                elif t == 'anons':
                    if (w, 'anons') not in covered and no is not None:
                        ev.append({'date': d, 'time': r['time'], 'type': 'anons', 'carousel': no, 'week': w, 'theme_reels': reels})
                elif reels and (w, t) not in covered:
                    ev.append({'date': d, 'time': r['time'], 'type': t, 'reels': reels, 'week': w, 'carousel_of_week': no})
        moves = {dt.date.fromisoformat(k): v for k, v in c.get('moves', {}).items()}
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
        ev.sort(key=lambda e: (e['date'], e['time'], ['reels', 'carousel', 'anons', 'reels_stories'].index(e['type'])))
        for e in ev:
            e['name'] = self.name(e)
            if e['type'] == 'carousel':
                asia = any(k in self.car[e['carousel']]['theme'] for k in ('japan', 'thailand', 'vietnam', 'korea', 'uae'))
                e['rubric'] = 'тема недели' if 'theme_reels' in e else 'Азия' if asia else 'Китай'
        return ev

    def name(self, e):
        d, hm = e['date'].isoformat(), e['time'].replace(':', '')
        if e['type'] == 'carousel':
            return f"{d}_{hm}_{self.car[e['carousel']]['theme']}"
        if e['type'] == 'anons':
            return f"{d}_{hm}_anons-{self.car[e['carousel']]['theme']}"
        return f"{d}_{hm}_{e['reels']}"

    def find(self, typ, key):
        return next((e for e in self.ev if e['type'] == typ and (e.get('carousel') == key or e.get('reels') == key)), None)

    def note(self, e):
        if not e.get('theme_reels'):
            return self.cfg['anons']['no_reels_note']
        r = self.find('reels', e['theme_reels'])
        when = 'Завтра' if r['date'] - e['date'] == dt.timedelta(days=1) else DAYS_ACC[r['date'].weekday()].capitalize()
        return f"{when} в {r['time']} — ролик об этом туре"

    def label(self, e):
        R = self.cfg['reels']
        if e['type'] == 'carousel':
            return 'Карусель', f"№{e['carousel']} {self.car[e['carousel']]['title']}"
        if e['type'] == 'reels':
            return 'Reels', R[e['reels']]['title']
        if e['type'] == 'anons':
            same = ' (одновременно с каруселью)' if e.get('launch') else ''
            return 'Stories', f"анонс карусели №{e['carousel']} · «{self.note(e)}»{same}"
        return 'Stories ×2', f"части ролика «{R[e['reels']]['title']}»"

    def table(self):
        out = []
        for e in self.ev:
            kind, what = self.label(e)
            mv = f" (перенос с {e['moved_from'].strftime('%d.%m')})" if e.get('moved_from') else ''
            out.append(f"{e['date'].strftime('%d.%m')} {WD[e['date'].weekday()]} {e['time']} | {kind:<10} | {what}{mv}")
        n = lambda t: sum(e['type'] == t for e in self.ev)
        out.append(f"Итого: каруселей {n('carousel')}, Reels {n('reels')}, Stories из роликов {n('reels_stories')}, анонсов {n('anons')}.")
        return out

    # ——— применить ———
    def mv(self, a, b):
        if a != b:
            subprocess.run(['git', 'mv', str(a), str(b)], cwd=HUB, check=True)

    def existing(self, folder, suffix):
        """Файл в TEXT, имя которого (без даты) равно suffix."""
        return next((f for f in sorted((self.ig / folder / 'TEXT').glob('*.md')) if DATED.sub('', f.stem) == suffix), None)

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
        h = {'date': e['date'].isoformat(), 'time': e['time'], 'rubric': e.get('rubric') or {
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
        self.render_anons(anons)
        for e in self.ev:
            n = e['name']
            h = {**self.head(e), **self.links(e)}
            if e['type'] == 'carousel':
                c = self.car[e['carousel']]
                self.mv(self.ig / 'CAROUSEL/PHOTO' / c['stem'], self.ig / 'CAROUSEL/PHOTO' / n)
                self.mv(c['file'], self.ig / 'CAROUSEL/TEXT' / f'{n}.md')
                f = self.ig / 'CAROUSEL/TEXT' / f'{n}.md'
                m, body = meta_of(f)
                for k in ('date', 'time', 'rubric', 'week', 'launch', 'moved_from', 'anons', 'reels'):
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
                     'music': self.cfg.get('music', ''), 'caption_status': 'черновик по тексту ролика, на согласовании'}
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
                Image.open(self.anons_png(i)).convert('RGB').save(dst / '01.jpg', quality=92, optimize=True)
                m = {k: q(v) for k, v in h.items()}
                m['title'] = q(f"Анонс карусели №{e['carousel']} «{self.car[e['carousel']]['title']}»")
                m['image'] = q(n)
                m['note'] = q(self.note(e))
                m['video_hub'] = q(f'finished-videos/анонсы/{self.ann_name()}/{i:02d}.png')
                m['image_status'] = q('на согласовании')
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
            stories.append({'cover': f'{base}/01.png', 'back': [f'{base}/02.png', f'{base}/03.png'],
                            'title': self.cfg['anons']['title'], 'note': self.note(e)})
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
        week = None
        for e in self.ev:
            if self.group(e) != week:
                week = self.group(e)
                title = 'Первый запуск — тест форматов (Reels → карусель + Stories → Stories)' if week == 0 else f'Неделя {week}'
                th = next((x for x in self.ev if x['week'] == week and x['type'] == 'carousel' and 'theme_reels' in x), None)
                if week and th:
                    title += f" — тема: №{th['carousel']} {self.car[th['carousel']]['title']}"
                    title += ' (карусель — в первом запуске)' if th.get('launch') else ''
                lines += ['', f'## {title}', '', '| Дата | Время | Формат | Что | Файл |', '|---|---|---|---|---|']
            kind, what = self.label(e)
            mark = ' · тест' if e.get('launch') else ''
            mv = f" · перенос с {e['moved_from'].strftime('%d.%m')}" if e.get('moved_from') else ''
            folder = {'carousel': 'CAROUSEL', 'reels': 'REELS'}.get(e['type'], 'STORIES')
            lines.append(f"| {WD[e['date'].weekday()]} {e['date'].day} {MON[e['date'].month]} | {e['time']} | {kind}{mark} | "
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
            cls = {'carousel': 'car', 'reels': 'rl', 'anons': 'st', 'reels_stories': 'st'}[e['type']]
            tag = '<span class="t">тест</span>' if e.get('launch') else ''
            mv = f'<div class="mv">перенос с {e["moved_from"].strftime("%d.%m")}</div>' if e.get('moved_from') else ''
            cards.append(f'<div class="c {cls}"><div class="d">{WD[e["date"].weekday()]}, {e["date"].day} {MON[e["date"].month]} · '
                         f'<b>{e["time"]}</b></div><div class="k">{kind}{tag}</div>{img}<div class="w">{what}</div>{mv}</div>')
        page = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Календарь Instagram {self.project}</title><style>
:root{{--bg:#f4f5f8;--card:#fff;--ink:#17171d;--mute:#6b6b76;--line:#e3e3ea;--car:#2563eb;--rl:#e11d48;--st:#f59e0b}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111216;--card:#1b1c22;--ink:#ececf1;--mute:#9a9aa6;--line:#2c2d35}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:14px/1.4 -apple-system,Segoe UI,Inter,Roboto,sans-serif;padding:20px 16px 48px}}
h1{{margin:0 0 4px;font-size:24px}}.sub{{color:var(--mute);margin:0 0 8px;max-width:960px}}.lg span{{margin-right:16px}}.lg i{{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px}}
h2{{grid-column:1/-1;margin:22px 0 2px;font-size:17px}}.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px}}
.c{{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--car);border-radius:12px;padding:10px}}
.c.rl{{border-top-color:var(--rl)}}.c.st{{border-top-color:var(--st)}}.d{{color:var(--mute);font-size:12px}}.k{{font-weight:700;margin:2px 0 6px}}
.c img{{display:block;max-width:100%;max-height:200px;border-radius:8px;margin:0 auto 6px}}.w{{font-size:13px}}.mv{{color:var(--rl);font-size:12px;margin-top:4px}}
.t{{background:var(--rl);color:#fff;border-radius:4px;padding:0 5px;font-size:11px;margin-left:6px;font-weight:600}}
</style></head><body><h1>Календарь Instagram {self.project}</h1>
<p class="sub">С 1 ноября, время по Москве. Неделя = один тур: пн карусель → вт Stories-анонс → ср Reels того же тура; чт карусель Китая,
пт две части ролика в Stories, сб карусель Азии, вс пусто. {self.table()[-1]}</p>
<p class="sub lg"><span><i style="background:var(--car)"></i>карусель</span><span><i style="background:var(--rl)"></i>Reels</span><span><i style="background:var(--st)"></i>Stories</span></p>
<div class="g">{"".join(cards)}</div></body></html>'''
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
