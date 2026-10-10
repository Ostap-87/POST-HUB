#!/usr/bin/env python3
"""Сохранить сгенерированные картинки к постам (CONTROL/IMAGE-RULES.md, разделы 2 и 6).

python3 CONTROL/TOOLS/save_images.py список.json
Список — JSON-массив:
  [{"text": "AURA/TELEGRAM/TEXT/2026-11-07_0900_тема.md", "url": "https://…png", "job": "id генерации",
    "model": "gpt_image_2_5 medium 1k 16:9", "cost": "0.5", "prompt": "…",
    "logos": [{"brand": "Unitree", "file": "/путь/unitree.png", "source": "откуда"}]}]
Для каждого: скачивает картинку, накладывает логотипы (logo_badge.py), кладёт JPG в PHOTO/ под именем текста,
пишет в шапку текста поля image*, статус «на согласовании». Логотипы не из CONTROL/LOGOS копируются туда,
источник дописывается в CONTROL/LOGOS/ИСТОЧНИКИ.md.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
LOGOS = HUB / 'CONTROL/LOGOS'
SOURCES = LOGOS / 'ИСТОЧНИКИ.md'


TR = dict(zip('абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
              ['a', 'b', 'v', 'g', 'd', 'e', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
               'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']))


def slug(name):
    s = ''.join(TR.get(c, c) for c in name.lower())
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s or 'logo'


def ensure_logo(item):
    src = Path(item['file'])
    if src.parent.resolve() == LOGOS.resolve():
        return src
    dst = LOGOS / f"{slug(item['brand'])}{src.suffix.lower()}"
    if not dst.exists():
        shutil.copy(src, dst)
        line = f"| `{dst.name}` | {item['brand']} | {item.get('source', str(src))} |\n"
        text = SOURCES.read_text(encoding='utf-8')
        marker = '\nНе найдено'
        text = text.replace(marker, line.rstrip('\n') + '\n' + marker, 1) if marker in text else text + line
        SOURCES.write_text(text, encoding='utf-8')
    return dst


def set_meta(text_path, fields):
    head, fm, body = text_path.read_text(encoding='utf-8').split('---\n', 2)
    lines = [l for l in fm.strip().split('\n') if not l.startswith('image')]
    lines += [f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in fields.items()]
    text_path.write_text('---\n' + '\n'.join(lines) + '\n---\n' + body, encoding='utf-8')


def main(list_path):
    items = json.loads(Path(list_path).read_text(encoding='utf-8'))
    tmp = Path(tempfile.mkdtemp())
    for it in items:
        text = HUB / it['text']
        photo_dir = text.parent.parent / 'PHOTO'
        name = text.name[:-3]
        for lang in ('.ru', '.en', '.zh'):           # обложка статьи — одна на все языки
            if name.endswith(lang):
                name = name[:-len(lang)]
        raw = tmp / f'{name}.png'
        subprocess.run(['curl', '-sSL', '--retry', '4', '--retry-all-errors', '-o', str(raw), it['url']], check=True)
        logos = [ensure_logo(l) for l in it.get('logos', [])]
        out = photo_dir / f'{name}.jpg'
        subprocess.run([sys.executable, str(HUB / 'CONTROL/TOOLS/logo_badge.py'), str(raw), *map(str, logos), '-o', str(out)],
                       check=True, capture_output=True)
        fields = {'image': out.name, 'image_status': 'на согласовании', 'image_model': it.get('model', ''),
                  'image_job': it.get('job', ''), 'image_cost': it.get('cost', ''),
                  'image_logos': ', '.join(l['brand'] for l in it.get('logos', [])), 'image_prompt': it.get('prompt', '')}
        versions = [text]
        if name != text.name[:-3]:                  # статья блога: обложка одна на все языки
            versions = sorted(text.parent.glob(f'{name}.*.md'))
        for v in versions:
            set_meta(v, fields)
        print(out.relative_to(HUB))


if __name__ == '__main__':
    main(sys.argv[1])
