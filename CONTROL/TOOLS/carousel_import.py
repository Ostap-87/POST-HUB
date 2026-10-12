#!/usr/bin/env python3
"""Положить готовую карусель из VIDEO-HUB в запас Instagram проекта (CONTROL/AGENT.md, раздел 3).

python3 CONTROL/TOOLS/carousel_import.py AURA 1 2026-10-10-foto-agibot-a2-w [--video-hub /home/user/VIDEO-HUB]
Берёт слайды `finished-videos/карусели/<имя>/NN.png` и props `reels-studio/props/carousels/<имя>.json` из VIDEO-HUB и пишет:
  <ПРОЕКТ>/INSTAGRAM/CAROUSEL/PHOTO/<NN>_<тема>/01.jpg, 02.jpg …   — слайды 1080×1350, JPG
  <ПРОЕКТ>/INSTAGRAM/CAROUSEL/TEXT/<NN>_<тема>.md                  — шапка + подпись к посту
NN — номер карусели в сценарии пользователя (CONTROL/SOURCES/2026-10-10_карусели-instagram/). Если карусель уже стоит
в расписании (`ГГГГ-ММ-ДД_ЧЧММ_тема`, поле `number` в шапке), обновляются те же файлы, дата, время и связка в шапке остаются.

Подпись под постом (решение пользователя 11.10.2026: «к каруселям описание текстом внизу») собирается из всех слайдов:
заголовок и подзаголовок обложки, «Листай карусель →», главная цифра с источником, маршрут, «что вы поймёте», «почему с нами»,
«что входит», «для кого», призыв проекта и хештеги (тема и страна + хештеги проекта), до 2200 знаков и 30 хештегов;
статус — «на согласовании». Повторный запуск подпись не трогает, если её уже правили (caption_status не «собрана…»).

python3 CONTROL/TOOLS/carousel_import.py GTT --captions   # пересобрать подписи всех каруселей проекта (кроме правленных)
"""
import argparse
import json
import re
from pathlib import Path

from PIL import Image

HUB = Path(__file__).resolve().parents[2]
SOURCES = {'AURA': 'CONTROL/SOURCES/2026-10-10_карусели-instagram/04_Aura_карусели_Instagram_20.docx',
           'GTT': 'CONTROL/SOURCES/2026-10-10_карусели-instagram/02_GTT_карусели_Instagram_74.docx'}
CTA = {'AURA': 'Пишите в личные сообщения или оставляйте заявку на сайте — рассчитаем стоимость и окупаемость.\n\n'
                'aura-robotics.ru — выбрать робота под вашу задачу',   # AURA/RULES.md: «на вы», в конце строка с сайтом
       'GTT': 'За подробностями пиши в личные сообщения или заходи на globaltechtour.ru и оставляй заявку — свяжемся в течение 2 минут.'}
TAGS = {'AURA': '#технологии #AI #Роботы #Роботизация #Гуманоиды #AGV',   # AURA/RULES.md, раздел 7
        'GTT': '#GTT #GlobalTechTour #Техтуризм'}
AUTO = 'собрана из слайдов (v2: все слайды), на согласовании'
VH = Path('/home/user/VIDEO-HUB')


def plain(t):
    return re.sub(r'\s+', ' ', (t or '').replace('**', '')).strip()


COUNTRY = {'Китай': '#Китай', 'Япония': '#Япония', 'Таиланд': '#Таиланд', 'Вьетнам': '#Вьетнам', 'Гонконг': '#Гонконг'}
# тема карусели (часть имени) → хештеги темы; первое совпадение
TOPIC_TAGS = [('fintech', '#Финтех #Платежи'), ('bubble-tea', '#БаблТи #Кофе'),
              ('robotics', '#Роботы #Робототехника'), ('tech-parks', '#Технопарки #Инновации'),
              ('tech-giants', '#Техгиганты #Технологии'), ('tech-internet', '#ИИ #ИнтернетКомпании'), ('-ai', '#ИИ #Нейросети'),
              ('tea-coffee', '#Кофейня #Чай'), ('beauty', '#Косметика #Бьюти'),
              ('longevity', '#Лонгевити #Биотех'), ('auto', '#Электромобили #Автопром'), ('appliances', '#БытоваяТехника #УмныйДом'),
              ('dark-kitchen', '#Доставка #DarkKitchen'), ('retail', '#Ритейл #Ретейл'), ('food-dairy', '#ПищеваяПромышленность #Молочка'),
              ('logistics', '#Логистика #Ecommerce'), ('petrochem', '#Нефтехимия #Промышленность'), ('waste', '#Переработка #Экология'),
              ('film', '#Кино #Киноиндустрия'), ('global-brands', '#Бренды #Экспорт'),
              ('hotel', '#Отели #Гостиничныйбизнес'), ('hospitality', '#Отели #Гостиничныйбизнес'), ('luxury', '#Люкс #Отели'),
              ('ticketing', '#Ивенты #Тревел'), ('confectionery', '#Кондитерская #Десерты'),
              ('agibot', '#AgiBot'), ('matrix', '#MATRIX'), ('robotera', '#Robotera')]
AUTO_PREFIX = 'собрана из слайдов'
# Aura: характеристики остаются на слайдах, в подписи — кто делает, цифры, «честно», применение, цена и поставка
AURA_SKIP = {'Размеры', 'Начинка', 'Характеристики', 'Проходимость', 'Открытость', 'Две версии', 'Два поколения',
             'Колёсные AgiBot', 'Мозги'}


AURA_BRAND = [('agibot', '#AgiBot'), ('matrix', '#MATRIX'), ('robotera', '#Robotera'), ('unitree', '#Unitree')]
AURA_DOGS = ('agibot-d1', 'go2', 'b2')                                # робопсы — без #Гуманоиды


def tags(project, slides, topic):
    if project == 'AURA':                                            # AURA/RULES.md, раздел 7: 1–2 из набора по смыслу + тема
        base = ['#Роботы', '#Роботизация'] if any(k in topic for k in AURA_DOGS) else ['#Гуманоиды', '#Роботы']
        brand = [t for k, t in AURA_BRAND if k in topic][:1]
        return ' '.join(base + brand + ['#РоботыИзКитая'])
    if project != 'GTT':
        return TAGS[project]
    out = []
    kick = plain(slides[0].get('kicker'))
    out += [t for c, t in COUNTRY.items() if c in kick][:1]
    out += next((t.split() for k, t in TOPIC_TAGS if k in f'-{topic}'), [])
    out += ['#БизнесЭкспедиция', *TAGS[project].split()]
    return ' '.join(dict.fromkeys(out))


def caption(project, slides, topic=''):
    dot = lambda t: t if not t or t[-1] in '.!?…:' else t + '.'
    cover = slides[0]
    blocks = [[dot(plain(cover.get('title'))), dot(plain(cover.get('text'))), 'Листай карусель →']]
    for sl in slides[1:-1]:
        b = []
        if project == 'AURA' and plain(sl.get('kicker')) in AURA_SKIP:
            continue
        if sl.get('value') and project == 'AURA':                      # «Скорость: 3,5 м/с — это больше 12 км/ч.»
            v, t = plain(sl['value']), plain(sl.get('title'))
            joint = ' — ' if t.startswith('это ') or ':' in t else ' '      # «3,5 м/с — это…», но «5 кг на каждую руку»
            line = f"{plain(sl['kicker'])}: {v}{joint}{t}" if sl.get('kicker') else f'{v}{joint}{t}'
            b.append(dot(line) + (' ' + dot(plain(sl.get('text'))) if sl.get('text') else ''))
        elif sl.get('value'):                                          # цифра
            src = f" (источник: {plain(sl['source'])})" if sl.get('source') else ''
            where = f" ({plain(sl['kicker'])})" if sl.get('kicker') and plain(sl['kicker']).lower() not in plain(sl.get('title')).lower() else ''
            b.append(dot(f"{plain(sl['value'])} {plain(sl.get('title'))}{where}") + (' ' + dot(plain(sl.get('text'))) if sl.get('text') else '') + src)
        elif sl.get('kind') == 'photoPair':                            # сравнение: пункты стороны «с нами»
            imgs = [i for i in sl.get('images', []) if isinstance(i, dict)]
            ours = imgs[-1].get('items', []) if imgs else []
            if ours:
                b += [(plain(sl.get('kicker')) or plain(sl.get('title'))) + ':'] + [f'• {plain(i)}' for i in ours]
        elif sl.get('items'):                                          # список, шаги, маршрут
            b += [(plain(sl.get('kicker')) or plain(sl.get('title'))) + ':'] + [f'• {plain(i)}' for i in sl['items']]
        elif sl.get('text'):                                           # текст
            b.append(f"{dot(plain(sl.get('title')))} {dot(plain(sl['text']))}")
        if b:
            blocks.append(b)
    blocks += [[CTA[project]], [tags(project, slides, topic)]]
    text = '\n\n'.join('\n'.join(l for l in b if l) for b in blocks)
    while len(text) > 2200 and len(blocks) > 4:                         # длинная — убираем блоки с конца описания
        blocks.pop(-3)
        text = '\n\n'.join('\n'.join(l for l in b if l) for b in blocks)
    return text


def find_existing(ch, number):
    """Файл подписи карусели с этим номером (имя может быть уже с датой) или None."""
    for f in sorted((ch / 'TEXT').glob('*.md')):
        if re.search(rf'^number: {number}$', f.read_text(encoding='utf-8'), re.M):
            return f
    return None


def read_meta(txt):
    head, body = txt.read_text(encoding='utf-8').split('---\n', 2)[1:]
    return {k: v for k, v in (l.split(': ', 1) for l in head.strip().split('\n'))}, body


def captions_all(project):
    ch = HUB / project / 'INSTAGRAM/CAROUSEL'
    n = 0
    for txt in sorted((ch / 'TEXT').glob('*.md')):
        meta, body = read_meta(txt)
        if not json.loads(meta.get('caption_status', '""')).startswith(AUTO_PREFIX):
            continue
        props = json.loads((VH / json.loads(meta['video_hub'])).read_text(encoding='utf-8'))
        topic = re.sub(r'^.*?carousels/\d{4}-\d{2}-\d{2}-(foto-)?', '', json.loads(meta['video_hub'])).removesuffix('.json')
        meta['caption_status'] = json.dumps(AUTO, ensure_ascii=False)
        txt.write_text('---\n' + '\n'.join(f'{k}: {v}' for k, v in meta.items()) + '\n---\n'
                       + caption(project, props['slides'], topic) + '\n', encoding='utf-8')
        n += 1
    print(f'{project}: подписи пересобраны — {n}')


def fm_value(v):
    return json.dumps(v, ensure_ascii=False) if isinstance(v, str) else str(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('project', choices=['AURA', 'GTT'])
    ap.add_argument('number', type=int, nargs='?')
    ap.add_argument('name', nargs='?', help='имя карусели в VIDEO-HUB, например 2026-10-10-foto-agibot-a2-w')
    ap.add_argument('--captions', action='store_true', help='пересобрать подписи всех каруселей проекта')
    ap.add_argument('--video-hub', default='/home/user/VIDEO-HUB')
    a = ap.parse_args()
    global VH
    VH = vh = Path(a.video_hub)
    if a.captions:
        return captions_all(a.project)
    props = json.loads((vh / 'reels-studio/props/carousels' / f'{a.name}.json').read_text(encoding='utf-8'))
    pngs = sorted((vh / 'finished-videos/карусели' / a.name).glob('[0-9][0-9].png'))
    assert len(pngs) == len(props['slides']), f'{a.name}: слайдов {len(pngs)}, в props {len(props["slides"])} — сначала npm run carousel'
    topic = re.sub(r'^\d{4}-\d{2}-\d{2}-(foto-)?', '', a.name)
    ch = HUB / a.project / 'INSTAGRAM/CAROUSEL'
    txt = find_existing(ch, a.number)
    base = txt.stem if txt else f'{a.number:02d}_{topic}'          # в расписании — ГГГГ-ММ-ДД_ЧЧММ_тема
    pdir = ch / 'PHOTO' / base
    pdir.mkdir(parents=True, exist_ok=True)
    for p in pngs:
        Image.open(p).convert('RGB').save(pdir / f'{p.stem}.jpg', 'JPEG', quality=90, optimize=True, progressive=True)
    gen = vh / 'source-videos/карусели' / a.name / '_генерации.json'
    g = json.loads(gen.read_text(encoding='utf-8')) if gen.exists() else {}
    meta = {'number': a.number, 'title': plain(props['slides'][0].get('title')), 'source': SOURCES[a.project],
            'slides': len(pngs), 'image': base, 'image_status': 'на согласовании', 'image_model': 'gpt_image_2_5 medium 1k',
            'image_cost': f"{sum(float(x.get('cost', 0)) for x in g.values()):g}", 'image_count': len(g),
            'video_hub': f'reels-studio/props/carousels/{a.name}.json', 'caption_status': AUTO}
    body = caption(a.project, props['slides'], topic)
    txt = txt or ch / 'TEXT' / f'{base}.md'
    if txt.exists():
        old_meta, old_body = read_meta(txt)
        if not json.loads(old_meta.get('caption_status', '""')).startswith(AUTO_PREFIX):   # подпись уже правили — оставляем
            body, meta['caption_status'] = old_body.strip('\n'), json.loads(old_meta['caption_status'])
        if 'image_status' in old_meta:
            meta['image_status'] = json.loads(old_meta['image_status'])
        # расписание и связка (date, time, rubric, week, anons, reels, launch) — как было, в том же порядке
        merged = {}
        for k, v in old_meta.items():
            merged[k] = meta.pop(k) if k in meta else (json.loads(v) if v.startswith('"') else int(v) if v.isdigit() else v)
        meta = {**merged, **meta}
    txt.parent.mkdir(parents=True, exist_ok=True)
    txt.write_text('---\n' + '\n'.join(f'{k}: {fm_value(v)}' for k, v in meta.items()) + '\n---\n' + body + '\n', encoding='utf-8')
    print(txt.relative_to(HUB), '+', len(pngs), 'слайдов')


if __name__ == '__main__':
    main()
