#!/usr/bin/env python3
"""Перенести утверждённые посты из запаса в очередь READY (CONTROL/AGENT.md, раздел 3; CONTROL/IMAGE-RULES.md, раздел 6).

python3 CONTROL/TOOLS/to_ready.py AURA/TELEGRAM [--dry-run]
python3 CONTROL/TOOLS/to_ready.py AURA/BLOG --time 15:00 [--dry-run]
python3 CONTROL/TOOLS/to_ready.py GTT/INSTAGRAM/CAROUSEL [--only 2026-11-02_1900_tur-robotics] [--dry-run]
Берёт тексты из <сеть>/TEXT (или <сеть>/<формат>/TEXT) с именем ГГГГ-ММ-ДД_ЧЧММ_тема, если пост утверждён, и переносит
их через `git mv`: текст → READY/<имя>/post.md, картинку из PHOTO → READY/<имя>/photo.jpg, в шапке `image` → "photo.jpg".
Файлы не копируются и не удаляются — только переносятся. Тексты без времени в имени (ГГГГ-ММ-ДД_тема) не трогает.

Утверждён — все поля статуса в шапке («status», «image_status», «caption_status») равны «утверждено» и хотя бы одно есть.
Instagram (решение пользователя 11.10.2026, автопубликация):
- карусель и сторис — папка в PHOTO (`01.jpg`, `02.jpg` …) → файлы едут в READY/<имя>/ как есть; Reels и сторис из
  роликов — без файлов: видео берётся по `video_hub` из публичного VIDEO-HUB;
- картинки поста копируются в публичный VIDEO-HUB `finished-videos/publish/<проект>-instagram/<имя>/`, ссылки — в шапку
  (`media_urls`): Instagram забирает файлы только по публичной ссылке. После переноса закоммить и запушь VIDEO-HUB
  (скрипт напомнит), иначе публикатор увидит битые ссылки ещё на проверке.

Статья блога — несколько языковых файлов (`тема.ru.md`, `тема.en.md`, `тема.zh.md`) с одной обложкой: они едут в одну папку
READY/ГГГГ-ММ-ДД_ЧЧММ_тема/ как post.ru.md, post.en.md, post.zh.md + photo.jpg. Время выхода блога в имени не стоит —
его даёт `--time` (время канала из RULES.md), в шапку пишется `publish_time` (поле `time` у блога — время чтения).
"""
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
NAME = re.compile(r'^\d{4}-\d{2}-\d{2}_\d{4}_.+$')
DATED = re.compile(r'^(\d{4}-\d{2}-\d{2})_(.+)$')
LANG = re.compile(r'^(.+)\.(ru|en|zh)$')
STATUS = ('status', 'image_status', 'caption_status')
MEDIA_REPO, MEDIA_BRANCH = 'Ostap-87/VIDEO-HUB', 'main'


def meta(text):
    fm = text.split('---\n', 2)[1]
    return {k: json.loads(v) if v.startswith('"') else v
            for k, v in (l.split(': ', 1) for l in fm.strip().split('\n'))}


def approved(m):
    st = [m[k] for k in STATUS if k in m]
    return bool(st) and all(v == 'утверждено' for v in st)


def git_mv(src, dst):
    subprocess.run(['git', 'mv', str(src), str(dst)], cwd=HUB, check=True)


def set_field(post, key, value, after='date'):
    s = post.read_text(encoding='utf-8')
    head, body = s.split('---\n', 2)[1:]
    v = json.dumps(value, ensure_ascii=False)
    lines = head.rstrip('\n').split('\n')
    for i, l in enumerate(lines):
        if l.startswith(f'{key}: '):
            lines[i] = f'{key}: {v}'
            break
    else:
        idx = next((i + 1 for i, l in enumerate(lines) if l.startswith(f'{after}: ')), len(lines))
        lines.insert(idx, f'{key}: {v}')
    post.write_text('---\n' + '\n'.join(lines) + '\n---\n' + body, encoding='utf-8')


def set_image(post, old, publish_time=None):
    s = post.read_text(encoding='utf-8').replace(f'image: "{old}"', 'image: "photo.jpg"', 1)
    if publish_time and '\npublish_time:' not in s.split('---\n', 2)[1]:
        s = re.sub(r'(\ndate: [^\n]*\n)', rf'\1publish_time: "{publish_time}"\n', s, count=1)
    post.write_text(s, encoding='utf-8')


def mirror(dst, project, vh):
    """Картинки поста → публичный VIDEO-HUB; ссылки — в шапку post.md (media_urls)."""
    files = sorted(p for p in dst.iterdir() if p.suffix.lower() in ('.jpg', '.jpeg'))
    if not files:
        return 0
    rel = Path('finished-videos/publish') / f'{project.lower()}-instagram' / dst.name
    out = vh / rel
    out.mkdir(parents=True, exist_ok=True)
    for f in files:
        shutil.copy2(f, out / f.name)
    subprocess.run(['git', 'add', str(rel)], cwd=vh, check=True)
    urls = [f'https://raw.githubusercontent.com/{MEDIA_REPO}/{MEDIA_BRANCH}/{rel.as_posix()}/{f.name}' for f in files]
    set_field(dst / 'post.md', 'media_urls', urls, after='time')
    return len(files)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('channel', help='например AURA/TELEGRAM, GTT/FACEBOOK/POST, GTT/INSTAGRAM/CAROUSEL или OSTAPDOTCENKO/BLOG')
    ap.add_argument('--time', help='время выхода ЧЧ:ММ по Москве для текстов без времени в имени (блоги)')
    ap.add_argument('--only', action='append', help='перенести только этот пост (имя без .md), можно несколько')
    ap.add_argument('--video-hub', default='/home/user/VIDEO-HUB', help='клон VIDEO-HUB (для Instagram)')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    ch = HUB / a.channel
    instagram = '/INSTAGRAM' in f'/{a.channel}'
    project = Path(a.channel).parts[0]
    hhmm = a.time.replace(':', '') if a.time else None
    groups = {}                                   # тема → [(язык или None, файл)]
    for txt in sorted((ch / 'TEXT').glob('*.md')):
        m = LANG.match(txt.stem)
        stem, lang = (m.group(1), m.group(2)) if m else (txt.stem, None)
        if a.only and stem not in a.only:
            continue
        groups.setdefault(stem, []).append((lang, txt))
    moved, mirrored, skipped = 0, 0, []
    for stem, files in groups.items():
        metas = [meta(t.read_text(encoding='utf-8')) for _, t in files]
        if not all(approved(m) for m in metas):
            if a.only:
                skipped.append(f'{stem}: не утверждён (status / image_status / caption_status)')
            continue
        name = stem
        if not NAME.match(stem):
            d = DATED.match(stem)
            if not (hhmm and d):
                skipped.append(f'{stem}: нет времени выхода в имени (для блога — --time)')
                continue
            name = f'{d.group(1)}_{hhmm}_{d.group(2)}'
        img = metas[0].get('image')
        photo = ch / 'PHOTO' / img if img else None
        if photo is not None and not photo.exists():
            skipped.append(f'{stem}: нет картинки {photo.name}')
            continue
        dst = ch / 'READY' / name
        if dst.exists():
            skipped.append(f'{stem}: уже есть в READY')
            continue
        if a.dry_run:
            what = 'папка картинок' if photo and photo.is_dir() else 'photo.jpg' if photo else 'без файлов (видео по video_hub)'
            print('→', dst.relative_to(HUB), ', '.join(f'post.{l}.md' if l else 'post.md' for l, _ in files), '+', what)
            moved += 1
            continue
        dst.mkdir(parents=True)
        for (lang, txt), m in zip(files, metas):
            post = dst / (f'post.{lang}.md' if lang else 'post.md')
            git_mv(txt, post)
            if photo is not None and photo.is_file():
                set_image(post, m['image'], a.time if name != stem else None)
        if photo is not None and photo.is_dir():                     # карусель, сторис: файлы по порядку
            for f in sorted(photo.iterdir()):
                git_mv(f, dst / f.name)
            set_field(dst / 'post.md', 'image', sorted(p.name for p in dst.iterdir() if p.suffix.lower() in ('.jpg', '.jpeg', '.png'))[0])
        elif photo is not None:
            git_mv(photo, dst / 'photo.jpg')
        if instagram:
            mirrored += mirror(dst, project, Path(a.video_hub))
            subprocess.run(['git', 'add', str(dst)], cwd=HUB, check=True)
        moved += 1
    print(f'перенесено: {moved}')
    if mirrored:
        print(f'картинок в публичный VIDEO-HUB: {mirrored} — закоммить и запушь VIDEO-HUB (finished-videos/publish/)')
    for line in skipped:
        print('пропущено —', line)


if __name__ == '__main__':
    main()
