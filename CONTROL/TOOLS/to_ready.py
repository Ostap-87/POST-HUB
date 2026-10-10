#!/usr/bin/env python3
"""Перенести утверждённые посты из запаса в очередь READY (CONTROL/AGENT.md, раздел 3; CONTROL/IMAGE-RULES.md, раздел 6).

python3 CONTROL/TOOLS/to_ready.py AURA/TELEGRAM [--dry-run]
python3 CONTROL/TOOLS/to_ready.py AURA/BLOG --time 15:00 [--dry-run]
Берёт тексты из <сеть>/TEXT (или <сеть>/<формат>/TEXT) с `image_status: "утверждено"` и именем ГГГГ-ММ-ДД_ЧЧММ_тема,
переносит их через `git mv`: текст → READY/<имя>/post.md, картинку из PHOTO → READY/<имя>/photo.jpg,
в шапке `image` становится "photo.jpg". Файлы не копируются и не удаляются — только переносятся.
Тексты без времени в имени (ГГГГ-ММ-ДД_тема) не трогает: для папки в READY нужно время выхода.

Статья блога — несколько языковых файлов (`тема.ru.md`, `тема.en.md`, `тема.zh.md`) с одной обложкой: они едут в одну папку
READY/ГГГГ-ММ-ДД_ЧЧММ_тема/ как post.ru.md, post.en.md, post.zh.md + photo.jpg. Время выхода блога в имени не стоит —
его даёт `--time` (время канала из RULES.md), в шапку пишется `publish_time` (поле `time` у блога — время чтения).
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
NAME = re.compile(r'^\d{4}-\d{2}-\d{2}_\d{4}_.+$')
DATED = re.compile(r'^(\d{4}-\d{2}-\d{2})_(.+)$')
LANG = re.compile(r'^(.+)\.(ru|en|zh)$')


def meta(text):
    fm = text.split('---\n', 2)[1]
    return {k: json.loads(v) if v.startswith('"') else v
            for k, v in (l.split(': ', 1) for l in fm.strip().split('\n'))}


def git_mv(src, dst):
    subprocess.run(['git', 'mv', str(src), str(dst)], cwd=HUB, check=True)


def set_image(post, old, publish_time=None):
    s = post.read_text(encoding='utf-8').replace(f'image: "{old}"', 'image: "photo.jpg"', 1)
    if publish_time and '\npublish_time:' not in s.split('---\n', 2)[1]:
        s = re.sub(r'(\ndate: [^\n]*\n)', rf'\1publish_time: "{publish_time}"\n', s, count=1)
    post.write_text(s, encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('channel', help='например AURA/TELEGRAM, GTT/FACEBOOK/POST или OSTAPDOTCENKO/BLOG')
    ap.add_argument('--time', help='время выхода ЧЧ:ММ по Москве для текстов без времени в имени (блоги)')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    ch = HUB / a.channel
    hhmm = a.time.replace(':', '') if a.time else None
    groups = {}                                   # тема → [(язык или None, файл)]
    for txt in sorted((ch / 'TEXT').glob('*.md')):
        m = LANG.match(txt.stem)
        stem, lang = (m.group(1), m.group(2)) if m else (txt.stem, None)
        groups.setdefault(stem, []).append((lang, txt))
    moved, skipped = 0, []
    for stem, files in groups.items():
        metas = [meta(t.read_text(encoding='utf-8')) for _, t in files]
        if any(m.get('image_status') != 'утверждено' for m in metas):
            continue
        name = stem
        if not NAME.match(stem):
            d = DATED.match(stem)
            if not (hhmm and d):
                skipped.append(f'{stem}: нет времени выхода в имени (для блога — --time)')
                continue
            name = f'{d.group(1)}_{hhmm}_{d.group(2)}'
        photo = ch / 'PHOTO' / metas[0]['image']
        if not photo.exists():
            skipped.append(f'{stem}: нет картинки {photo.name}')
            continue
        dst = ch / 'READY' / name
        if dst.exists():
            skipped.append(f'{stem}: уже есть в READY')
            continue
        if a.dry_run:
            print('→', dst.relative_to(HUB), ', '.join(f'post.{l}.md' if l else 'post.md' for l, _ in files))
            moved += 1
            continue
        dst.mkdir(parents=True)
        for (lang, txt), m in zip(files, metas):
            post = dst / (f'post.{lang}.md' if lang else 'post.md')
            git_mv(txt, post)
            set_image(post, m['image'], a.time if name != stem else None)
        git_mv(photo, dst / 'photo.jpg')
        moved += 1
    print(f'перенесено: {moved}')
    for line in skipped:
        print('пропущено —', line)


if __name__ == '__main__':
    main()
