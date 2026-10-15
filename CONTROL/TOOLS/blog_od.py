"""Блог ostapdotcenko.ru из пула POST-HUB (решение пользователя 15.10.2026: «с сегодняшнего дня начнем использовать пул статей»).

  python3 CONTROL/TOOLS/blog_od.py --queue                         # очередь READY: дата, время, заголовок
  python3 CONTROL/TOOLS/blog_od.py --redate 2026-10-15             # даты пула подряд, по статье в день с этой даты (git mv + date)
  python3 CONTROL/TOOLS/blog_od.py --post <папка READY> --dry-run  # показать, что уйдёт на сайт (ничего не меняет)
  python3 CONTROL/TOOLS/blog_od.py --post <папка READY>            # опубликовать одну статью сейчас (команда пользователя)
  python3 CONTROL/TOOLS/blog_od.py --due                           # опубликовать статьи, время которых наступило (стоп-кран учитывается)

Публикация = статья в конец `blog.articles[]` трёх файлов сайта `src/i18n/{ru,en,zh}.ts` (порядок полей как в
PROTOCOL_ARTICLES.md сайта) + обложка `public/img/<slug>-cover.jpg` → коммит «Publish blog article: <slug> (POST-HUB)»
и пуш в `main` репозитория `Ostap-87/ostapdotcenko` (`--site`, по умолчанию ../ostapdotcenko рядом с POST-HUB).
Сервер собирает сайт каждые 2 минуты и сам постит новую статью в Facebook (RU) и LinkedIn (EN).
Папка статьи уезжает в `PUBLISHED/ГГГГ-ММ/` с `info.json` (ссылка на статью).

Разметка md → сайт (рендер сайта понимает только `## `, `![подпись](путь)`, списки `* `, метку «строка:» и ссылки):
эпиграф `> …` → абзац; `**…**` отдельной строкой → `## …`; жирный и курсив внутри текста — без звёздочек;
нумерованные источники «N. Название — https://…» → список ссылок `* [N. Название](url)`; строки одного абзаца —
отдельными абзацами; обложка — перед первым `##` (после лида).
"""
import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
BLOG = HUB / 'OSTAPDOTCENKO' / 'BLOG'
READY = BLOG / 'READY'
MSK = dt.timezone(dt.timedelta(hours=3))
LANGS = ('ru', 'en', 'zh')
ANCHOR = '\n    ],\n    videos: ['
URL_RE = re.compile(r'https?://[^\s)>\]]+')


def parse(path):
    text = path.read_text(encoding='utf-8')
    _, head, body = text.split('---\n', 2)
    meta = {}
    for line in head.strip().split('\n'):
        k, v = line.split(': ', 1)
        try:
            meta[k] = json.loads(v)
        except json.JSONDecodeError:
            meta[k] = v
    return meta, body


def set_date(path, date):
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'^date: ".*"$', f'date: "{date}"', text, count=1, flags=re.M)
    path.write_text(text, encoding='utf-8')


def strip_marks(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    return re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', s)


def source_item(line):
    """«N.  Название, дата — https://url (заметка)» → «* [N. Название, дата](url) (заметка)»."""
    m = re.match(r'^(\d+)\.\s+(.*)$', line)
    num, rest = m.group(1), m.group(2)
    u = URL_RE.search(rest)
    if not u:
        return f'* {num}. {strip_marks(rest)}'
    name = rest[:u.start()].rstrip(' —–-:,').strip() or u.group(0)
    note = rest[u.end():].strip()
    name = strip_marks(name).replace('[', '(').replace(']', ')')
    return f'* [{num}. {name}]({u.group(0)})' + (f' {note}' if note else '')


def to_site_body(md, cover, caption):
    out = []
    for block in re.split(r'\n\s*\n', md.strip()):
        lines = [l.rstrip() for l in block.split('\n') if l.strip()]
        if not lines:
            continue
        if all(l.startswith('>') for l in lines):                      # эпиграф
            lines = [l.lstrip('>').strip() for l in lines]
        if len(lines) == 1 and re.match(r'^#{1,6}\s', lines[0]):          # заголовок любого уровня → ##
            out.append('## ' + strip_marks(re.sub(r'^#{1,6}\s+', '', lines[0])))
            continue
        if len(lines) == 1 and re.fullmatch(r'\*\*[^*]+\*\*:?', lines[0]):  # строка целиком жирным → подзаголовок
            out.append('## ' + lines[0].strip('*:').strip().rstrip('*').strip())
            continue
        group = []                                                     # подряд идущие пункты списка — один блок
        for l in lines:
            if re.match(r'^\d+\.\s', l):
                group.append(source_item(l) if URL_RE.search(l) else '* ' + strip_marks(re.sub(r'^\d+\.\s+', '', l)))
            elif re.match(r'^[*\-•]\s', l):
                group.append('* ' + strip_marks(l[2:].strip()))
            else:
                if group:
                    out.append('\n'.join(group))
                    group = []
                out.append(strip_marks(l))
        if group:
            out.append('\n'.join(group))
    hero = f'![{caption}]({cover})'
    first_h2 = next((i for i, b in enumerate(out) if b.startswith('## ')), min(2, len(out)))
    out.insert(first_h2, hero)
    return '\n\n'.join(out)


def entry(meta, body):
    fields = [('category', meta.get('category', 'tech')), ('slug', meta['slug']), ('date', meta['date']),
              ('tag', meta.get('tag', '')), ('time', meta.get('time', '')), ('title', meta['title']),
              ('excerpt', meta.get('excerpt', '')), ('body', body), ('link', '')]
    lines = [f'        {k}: {json.dumps(v, ensure_ascii=False)},' for k, v in fields]
    lines.append('        sideImages: {"left": [], "right": []}')
    return '      {\n' + '\n'.join(lines) + '\n      }'


def insert(ts_path, item, slug):
    s = ts_path.read_text(encoding='utf-8')
    assert s.count(ANCHOR) == 1, f'{ts_path.name}: якорь массива статей не найден или не один'
    assert f'slug: "{slug}"' not in s, f'{ts_path.name}: статья {slug} уже есть на сайте'
    head, tail = s.split(ANCHOR)
    head = head.rstrip()
    if not head.endswith(','):
        head += ','
    ts_path.write_text(head + '\n' + item + ANCHOR + tail, encoding='utf-8')


def folders():
    return sorted(d for d in READY.iterdir() if d.is_dir() and (d / 'post.ru.md').exists())


def when_of(d):
    meta, _ = parse(d / 'post.ru.md')
    hhmm = meta.get('publish_time', '15:00')
    return dt.datetime.fromisoformat(f"{meta['date']}T{hhmm}").replace(tzinfo=MSK), meta


def git(*args, cwd):
    return subprocess.run(['git', *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def allowed(d):
    """Стоп-кран CONTROL/PUBLISHING.yaml: на паузе выходят только BLOG из pause_except или папки из pause_allow."""
    text = (HUB / 'CONTROL' / 'PUBLISHING.yaml').read_text(encoding='utf-8')
    if not re.search(r'^pause:\s*true', text, re.M):
        return True
    exc = re.search(r'^pause_except:\s*\[(.*)\]', text, re.M)
    if exc and 'BLOG' in [x.strip() for x in exc.group(1).split(',')]:
        return True
    rel = str(d.relative_to(HUB))
    return any(line.strip() == f'- {rel}' for line in text.split('\n'))


def publish(d, site, dry):
    metas = {lang: parse(d / f'post.{lang}.md') for lang in LANGS}
    ru = metas['ru'][0]
    slug, today = ru['slug'], dt.datetime.now(MSK).date().isoformat()
    cover_name = f'{slug}-cover.jpg'
    cover = f'/img/{cover_name}'
    items = {}
    for lang, (meta, body) in metas.items():
        meta = {**meta, 'date': today}
        items[lang] = entry(meta, to_site_body(body, cover, meta['title']))
    photo = d / ru.get('image', 'photo.jpg')
    kb = photo.stat().st_size // 1024
    if dry:
        print(f'{d.name} → https://ostapdotcenko.ru/blog/{slug}/  (дата на сайте {today}, обложка {cover_name}, {kb} КБ)')
        print(items['ru'][:3000])
        return None
    assert kb <= 500, f'обложка {kb} КБ — больше 500 КБ'
    git('pull', '-q', '--rebase', 'origin', 'main', cwd=site)
    for lang in LANGS:
        insert(site / 'src' / 'i18n' / f'{lang}.ts', items[lang], slug)
    dst = site / 'public' / 'img' / cover_name
    shutil.copy(photo, dst)
    dst.chmod(0o644)
    git('add', 'src/i18n/ru.ts', 'src/i18n/en.ts', 'src/i18n/zh.ts', f'public/img/{cover_name}', cwd=site)
    git('commit', '-q', '-m', f'Publish blog article: {slug} (POST-HUB)', cwd=site)
    for attempt in range(4):
        try:
            git('push', '-q', 'origin', 'HEAD:main', cwd=site)
            break
        except subprocess.CalledProcessError:
            if attempt == 3:
                raise
            git('pull', '-q', '--rebase', 'origin', 'main', cwd=site)
    sha = git('rev-parse', '--short', 'HEAD', cwd=site).strip()
    when = dt.datetime.now(MSK)
    base = BLOG / 'PUBLISHED' / when.strftime('%Y-%m')
    base.mkdir(parents=True, exist_ok=True)
    git('mv', str(d), str(base / d.name), cwd=HUB)
    url = f'https://ostapdotcenko.ru/blog/{slug}/'
    info = {'published_at': when.isoformat(timespec='seconds'), 'url': url, 'site_commit': sha, 'published_by': 'blog_od.py',
            'autopost': 'сервер сайта: Facebook (RU) и LinkedIn (EN) через auto-post-new-articles.mjs'}
    (base / d.name / 'info.json').write_text(json.dumps(info, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    git('add', '-A', str(BLOG), cwd=HUB)
    print(f'опубликовано: {url} (коммит сайта {sha})')
    return url


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--queue', action='store_true')
    ap.add_argument('--redate')
    ap.add_argument('--post')
    ap.add_argument('--due', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--site', default=str(HUB.parent / 'ostapdotcenko'))
    a = ap.parse_args()
    site = Path(a.site)
    if a.queue:
        for d in folders():
            when, meta = when_of(d)
            print(f"{when:%d.%m %H:%M}  {meta['slug']:<45} {meta['title']}")
    elif a.redate:
        start = dt.date.fromisoformat(a.redate)
        for i, d in enumerate(folders()):
            date = (start + dt.timedelta(days=i)).isoformat()
            when, meta = when_of(d)
            name = f"{date}_{meta.get('publish_time', '15:00').replace(':', '')}_{d.name.split('_', 2)[2]}"
            for lang in LANGS:
                set_date(d / f'post.{lang}.md', date)
            if name != d.name:
                git('mv', str(d), str(READY / name), cwd=HUB)
        print(f'пул: {len(folders())} статей с {start:%d.%m.%Y}, по одной в день')
    elif a.post:
        d = Path(a.post)
        d = d if d.is_absolute() else (HUB / d if (HUB / d).exists() else READY / d)
        publish(d.resolve(), site, a.dry_run)
    elif a.due:
        now = dt.datetime.now(MSK)
        for d in folders():
            when, meta = when_of(d)
            if when > now:
                continue
            if not allowed(d):
                print(f'  · {d.name}: стоп-кран (нет в pause_allow) — пропуск')
                continue
            publish(d, site, a.dry_run)
    else:
        ap.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
