#!/usr/bin/env python3
"""Положить готовую карусель из VIDEO-HUB в запас Instagram проекта (CONTROL/AGENT.md, раздел 3).

python3 CONTROL/TOOLS/carousel_import.py AURA 1 2026-10-10-foto-agibot-a2-w [--video-hub /home/user/VIDEO-HUB]
Берёт слайды `finished-videos/карусели/<имя>/NN.png` и props `reels-studio/props/carousels/<имя>.json` из VIDEO-HUB и пишет:
  <ПРОЕКТ>/INSTAGRAM/CAROUSEL/PHOTO/<NN>_<тема>/01.jpg, 02.jpg …   — слайды 1080×1350, JPG
  <ПРОЕКТ>/INSTAGRAM/CAROUSEL/TEXT/<NN>_<тема>.md                  — шапка + подпись к посту
NN — номер карусели в сценарии пользователя (CONTROL/SOURCES/2026-10-10_карусели-instagram/). Дата и время выхода
появятся в имени, когда пользователь задаст расписание Instagram (тогда файлы переименовываются через `git mv`).
Подпись собирается из текста слайдов (обложка, цифры, финал) + хештеги проекта; статус — «на согласовании».
Повторный запуск обновляет слайды и шапку, подпись не трогает, если её уже правили (caption_status не «собрана…»).
"""
import argparse
import json
import re
from pathlib import Path

from PIL import Image

HUB = Path(__file__).resolve().parents[2]
SOURCES = {'AURA': 'CONTROL/SOURCES/2026-10-10_карусели-instagram/04_Aura_карусели_Instagram_20.docx',
           'GTT': 'CONTROL/SOURCES/2026-10-10_карусели-instagram/02_GTT_карусели_Instagram_74.docx'}
CTA = {'AURA': 'Пиши в личные сообщения или оставляй заявку на сайте aura-robotics.ru — рассчитаем стоимость и окупаемость.',
       'GTT': 'За подробностями пиши в личные сообщения или заходи на globaltechtour.ru и оставляй заявку — свяжемся в течение 2 минут.'}
TAGS = {'AURA': '#технологии #AI #Роботы #Роботизация #Гуманоиды #AGV',   # AURA/RULES.md, раздел 7
        'GTT': '#GTT #GlobalTechTour #Техтуризм'}
AUTO = 'собрана из слайдов, на согласовании'


def plain(t):
    return re.sub(r'\s+', ' ', (t or '').replace('**', '')).strip()


def caption(project, slides):
    cover = slides[0]
    dot = lambda t: t if not t or t[-1] in '.!?…' else t + '.'
    lines = [dot(plain(cover.get('title'))), dot(plain(cover.get('text')))]
    facts = []
    for s in slides[1:-1]:
        if s.get('value'):
            facts.append(f"{plain(s['value'])} {plain(s.get('title'))}")
        if len(facts) == 3:
            break
    if facts:
        lines += [''] + [f'• {f}' for f in facts]
    lines += ['', CTA[project], '', TAGS[project]]
    return '\n'.join(l for i, l in enumerate(lines) if l or (i and lines[i - 1]))


def fm_value(v):
    return json.dumps(v, ensure_ascii=False) if isinstance(v, str) else str(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('project', choices=['AURA', 'GTT'])
    ap.add_argument('number', type=int)
    ap.add_argument('name', help='имя карусели в VIDEO-HUB, например 2026-10-10-foto-agibot-a2-w')
    ap.add_argument('--video-hub', default='/home/user/VIDEO-HUB')
    a = ap.parse_args()
    vh = Path(a.video_hub)
    props = json.loads((vh / 'reels-studio/props/carousels' / f'{a.name}.json').read_text(encoding='utf-8'))
    pngs = sorted((vh / 'finished-videos/карусели' / a.name).glob('[0-9][0-9].png'))
    assert len(pngs) == len(props['slides']), f'{a.name}: слайдов {len(pngs)}, в props {len(props["slides"])} — сначала npm run carousel'
    topic = re.sub(r'^\d{4}-\d{2}-\d{2}-(foto-)?', '', a.name)
    base = f'{a.number:02d}_{topic}'
    ch = HUB / a.project / 'INSTAGRAM/CAROUSEL'
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
    txt = ch / 'TEXT' / f'{base}.md'
    body = caption(a.project, props['slides'])
    if txt.exists():
        old = txt.read_text(encoding='utf-8').split('---\n', 2)
        old_meta = dict(l.split(': ', 1) for l in old[1].strip().split('\n'))
        if json.loads(old_meta.get('caption_status', '""')) != AUTO:      # подпись уже правили — оставляем
            body, meta['caption_status'] = old[2].strip('\n'), json.loads(old_meta['caption_status'])
        if 'image_status' in old_meta:
            meta['image_status'] = json.loads(old_meta['image_status'])
    txt.parent.mkdir(parents=True, exist_ok=True)
    txt.write_text('---\n' + '\n'.join(f'{k}: {fm_value(v)}' for k, v in meta.items()) + '\n---\n' + body + '\n', encoding='utf-8')
    print(txt.relative_to(HUB), '+', len(pngs), 'слайдов')


if __name__ == '__main__':
    main()
