#!/usr/bin/env python3
"""Перенести утверждённые посты из запаса в очередь READY (CONTROL/AGENT.md, раздел 3; CONTROL/IMAGE-RULES.md, раздел 6).

python3 CONTROL/TOOLS/to_ready.py AURA/TELEGRAM [--dry-run]
Берёт тексты из <сеть>/TEXT (или <сеть>/<формат>/TEXT) с `image_status: "утверждено"` и именем ГГГГ-ММ-ДД_ЧЧММ_тема,
переносит их через `git mv`: текст → READY/<имя>/post.md, картинку из PHOTO → READY/<имя>/photo.jpg,
в шапке `image` становится "photo.jpg". Файлы не копируются и не удаляются — только переносятся.
Тексты без времени в имени (ГГГГ-ММ-ДД_тема) не трогает: для папки в READY нужно время выхода.
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
NAME = re.compile(r'^\d{4}-\d{2}-\d{2}_\d{4}_.+$')


def meta(text):
    fm = text.split('---\n', 2)[1]
    return {k: json.loads(v) if v.startswith('"') else v
            for k, v in (l.split(': ', 1) for l in fm.strip().split('\n'))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('channel', help='например AURA/TELEGRAM или GTT/FACEBOOK/POST')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    ch = HUB / a.channel
    moved, skipped = 0, []
    for txt in sorted((ch / 'TEXT').glob('*.md')):
        s = txt.read_text(encoding='utf-8')
        m = meta(s)
        if m.get('image_status') != 'утверждено':
            continue
        stem = txt.stem
        if not NAME.match(stem):
            skipped.append(f'{stem}: нет времени выхода в имени')
            continue
        photo = ch / 'PHOTO' / m['image']
        if not photo.exists():
            skipped.append(f'{stem}: нет картинки {photo.name}')
            continue
        dst = ch / 'READY' / stem
        if dst.exists():
            skipped.append(f'{stem}: уже есть в READY')
            continue
        if a.dry_run:
            print('→', dst.relative_to(HUB)); moved += 1
            continue
        dst.mkdir(parents=True)
        subprocess.run(['git', 'mv', str(txt), str(dst / 'post.md')], cwd=HUB, check=True)
        subprocess.run(['git', 'mv', str(photo), str(dst / 'photo.jpg')], cwd=HUB, check=True)
        post = dst / 'post.md'
        post.write_text(post.read_text(encoding='utf-8').replace(f'image: "{m["image"]}"', 'image: "photo.jpg"', 1),
                        encoding='utf-8')
        moved += 1
    print(f'перенесено: {moved}')
    for line in skipped:
        print('пропущено —', line)


if __name__ == '__main__':
    main()
