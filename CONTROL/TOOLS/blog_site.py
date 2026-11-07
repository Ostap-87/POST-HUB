"""Блоги globaltechtour.ru (GTT) и aura-robotics.ru (AURA) из очереди POST-HUB — без агента.

Решение пользователя 07.11.2026: «Утверждаю, делай. И сделай так, чтобы статьи самостоятельно выходили без твоего участия».
Старый публикатор сервера (claude-control, /opt/publishers/publish-{gtt,aura}-article.py) брал статьи из своих пачек
по 73 штуки; пачки кончились (GTT — 02.11, Aura — 04.11). Новые статьи лежат здесь, в <ПРОЕКТ>/BLOG/READY.

Кто запускает:
  * сайт — свой GitHub Actions «Блог из POST-HUB» в репозитории сайта (SINOTECH, AURA): несколько раз в день берёт эту
    папку из публичного POST-HUB и запускает `--due --site .`, затем коммитит и пушит сайт своим GITHUB_TOKEN
    (пуш в ветку деплоя → вебхук сервера пересобирает сайт). Токены не нужны: POST-HUB и оба сайта публичные.
  * учёт — workflow POST-HUB «Блоги сайтов — учёт»: `--sync` переносит вышедшие статьи READY → PUBLISHED/ГГГГ-ММ/
    с info.json (статья считается вышедшей, когда её slug уже есть в репозитории сайта на GitHub).

  python3 CONTROL/TOOLS/blog_site.py --project GTT --queue                  # очередь: дата, время, slug
  python3 CONTROL/TOOLS/blog_site.py --project GTT --redate 2026-11-07      # даты подряд, по статье в день (git mv + date)
  python3 CONTROL/TOOLS/blog_site.py --project GTT --site ../sinotech --post <папка> [--dry-run]  # одна статья сейчас
  python3 CONTROL/TOOLS/blog_site.py --project GTT --site ../sinotech --due [--dry-run]           # всё, чьё время наступило
  python3 CONTROL/TOOLS/blog_site.py --project GTT --sync [--dry-run]       # READY → PUBLISHED для вышедших (по GitHub)

`--due`/`--post` только меняют файлы сайта (коммит и пуш делает workflow сайта или человек) и печатают
`PUBLISHED_SLUG=<slug>` на каждую статью. Стоп-кран — CONTROL/PUBLISHING.yaml (`<ПРОЕКТ>/BLOG` в pause_except).

Разметка md → сайт (рендер обоих сайтов понимает только абзацы через пустую строку, `## ` и внутренние ссылки
`[текст](/путь)`): заголовок любого уровня → `## `; жирный и курсив — без звёздочек; пункты списков и строки таблиц —
отдельными абзацами («— пункт», «1. пункт», «ячейка — ячейка»); внешние ссылки и картинки — только текст;
внутренние ссылки без префикса `/en` (язык сайты добавляют сами); у GTT ссылка на несуществующую компанию или
программу превращается в обычный текст.
"""
import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
MSK = dt.timezone(dt.timedelta(hours=3))
AUTHOR = 'Ostap Dotcenko'
MAX_PER_RUN = 3

PROJECTS = {
    'GTT': {
        'domain': 'https://globaltechtour.ru',
        'repo': 'Ostap-87/SINOTECH',
        'branch': 'claude/sinotech-voyage-setup',      # ветку деплоя слушает вебхук сервера
        'data': 'src/data/site_content.example.json',
    },
    'AURA': {
        'domain': 'https://aura-robotics.ru',
        'repo': 'Ostap-87/AURA',
        'branch': 'main',
        'data': 'content/blog',
    },
}


# ---------- очередь ----------

def blog_dir(project):
    return HUB / project / 'BLOG'


def folders(project):
    ready = blog_dir(project) / 'READY'
    return sorted(d for d in ready.iterdir() if d.is_dir() and (d / 'post.ru.md').exists())


def parse(path):
    text = path.read_text(encoding='utf-8')
    _, head, body = text.split('---\n', 2)
    meta = {}
    for line in head.strip().split('\n'):
        if ': ' not in line:
            continue
        k, v = line.split(': ', 1)
        try:
            meta[k] = json.loads(v)
        except json.JSONDecodeError:
            meta[k] = v
    return meta, body


def when_of(d):
    meta, _ = parse(d / 'post.ru.md')
    hhmm = meta.get('publish_time', '15:00')
    return dt.datetime.fromisoformat(f"{meta['date']}T{hhmm}").replace(tzinfo=MSK), meta


def set_date(path, date):
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'^date: ".*"$', f'date: "{date}"', text, count=1, flags=re.M)
    path.write_text(text, encoding='utf-8')


def allowed(project):
    """Стоп-кран CONTROL/PUBLISHING.yaml: на паузе блог выходит, только если <ПРОЕКТ>/BLOG в pause_except."""
    text = (HUB / 'CONTROL' / 'PUBLISHING.yaml').read_text(encoding='utf-8')
    if not re.search(r'^pause:\s*true', text, re.M):
        return True
    exc = re.search(r'^pause_except:\s*\[(.*)\]', text, re.M)
    names = [x.strip().strip('"\'') for x in exc.group(1).split(',')] if exc else []
    return f'{project}/BLOG' in names


def git(*args, cwd):
    return subprocess.run(['git', *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


# ---------- разметка ----------

MD_LINK = re.compile(r'(!?)\[([^\]]+)\]\(([^)\s]+)\)')


def strip_marks(s):
    s = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'__(.+?)__', r'\1', s)
    return re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', s)


def make_link_fixer(valid):
    def fix(s):
        def repl(m):
            bang, text, url = m.groups()
            if bang:
                return ''
            if not url.startswith('/'):
                return text
            path = re.sub(r'^/en(?=/|$)', '', url) or '/'
            if valid and not valid(path):
                return text
            return f'[{text}]({path})'
        return MD_LINK.sub(repl, s)
    return fix


def to_site_body(md, fix_links):
    out = []

    def inline(s):
        return fix_links(strip_marks(s.strip()))

    for block in re.split(r'\n\s*\n', md.strip()):
        lines = [l.rstrip() for l in block.split('\n') if l.strip()]
        if not lines:
            continue
        if all(l.lstrip().startswith('>') for l in lines):                     # цитата / эпиграф
            lines = [l.lstrip().lstrip('>').strip() for l in lines]
        if all(re.fullmatch(r'\s*[-*_]{3,}\s*', l) for l in lines):             # горизонтальная черта
            continue
        if len(lines) == 1 and re.match(r'^#{1,6}\s', lines[0]):                # заголовок любого уровня → ##
            out.append('## ' + inline(re.sub(r'^#{1,6}\s+', '', lines[0])))
            continue
        if len(lines) == 1 and re.fullmatch(r'\*\*[^*]+\*\*:?', lines[0].strip()):
            out.append('## ' + inline(lines[0].strip().strip(':')))
            continue
        para = []
        for l in lines:
            s = l.strip()
            if s.startswith('|'):                                                # строка таблицы
                cells = [c.strip() for c in s.strip('|').split('|')]
                if all(re.fullmatch(r':?-{2,}:?', c) or not c for c in cells):
                    continue
                if para:
                    out.append(inline(' '.join(para)))
                    para = []
                out.append(inline(' — '.join(c for c in cells if c)))
            elif re.match(r'^[-*•]\s+', s):                                     # маркированный пункт
                if para:
                    out.append(inline(' '.join(para)))
                    para = []
                out.append('— ' + inline(re.sub(r'^[-*•]\s+', '', s)))
            elif re.match(r'^\d+[.)]\s+', s):                                   # нумерованный пункт
                if para:
                    out.append(inline(' '.join(para)))
                    para = []
                num = re.match(r'^(\d+)', s).group(1)
                out.append(f'{num}. ' + inline(re.sub(r'^\d+[.)]\s+', '', s)))
            else:
                para.append(s)
        if para:
            out.append(inline(' '.join(para)))
    return '\n\n'.join(b for b in out if b.strip() and b.strip() != '##')


# ---------- сайты ----------

def gtt_validator(site):
    try:
        comp = json.loads((site / 'src/data/companies.json').read_text(encoding='utf-8'))
        tours = json.loads((site / 'src/data/tours.json').read_text(encoding='utf-8'))
    except FileNotFoundError:
        return None
    companies = {c['id'] for c in comp.get('companies', [])}
    tour_ids = {t['tour_id'] for t in tours.get('tours', [])}

    def valid(path):
        m = re.match(r'^/companies/([^/?#]+)', path)
        if m:
            return m.group(1) in companies
        m = re.match(r'^/expeditions/([^/?#]+)', path)
        if m and m.group(1) != 'recommended':
            return m.group(1) in tour_ids
        return True
    return valid


def article(d, fix_links):
    ru, body_ru = parse(d / 'post.ru.md')
    en_path = d / 'post.en.md'
    en, body_en = parse(en_path) if en_path.exists() else (ru, body_ru)
    tags = [t.strip() for t in str(ru.get('image_logos') or '').split(',') if t.strip()]
    return {
        'slug': ru['slug'], 'date': ru['date'],
        'title_ru': ru['title'], 'title_en': en['title'],
        'excerpt_ru': ru.get('meta_description', ''), 'excerpt_en': en.get('meta_description', ''),
        'body_ru': to_site_body(body_ru, fix_links), 'body_en': to_site_body(body_en, fix_links),
        'tags': tags, 'photo': d / ru.get('image', 'photo.jpg'),
    }


def on_site(project, site, slug):
    p = PROJECTS[project]
    if project == 'GTT':
        data = json.loads((site / p['data']).read_text(encoding='utf-8'))
        return any(b.get('slug') == slug for b in data.get('blog', []))
    return (site / p['data'] / f'{slug}.json').exists()


def write_site(project, site, a, today):
    """Статья и обложка в файлах сайта. Дата на сайте — день публикации."""
    p = PROJECTS[project]
    slug = a['slug']
    cover_rel = f'public/covers/{slug}.jpg'
    cover_url = f"{p['domain']}/covers/{slug}.jpg"
    dst = site / cover_rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(a['photo'], dst)
    dst.chmod(0o644)
    if project == 'GTT':
        path = site / p['data']
        raw = path.read_text(encoding='utf-8')
        data = json.loads(raw)
        item = {
            'id': slug, 'slug': slug, 'title_en': a['title_en'], 'title_ru': a['title_ru'], 'cover': cover_url,
            'date': today, 'excerpt_en': a['excerpt_en'], 'excerpt_ru': a['excerpt_ru'],
            'body_en': a['body_en'], 'body_ru': a['body_ru'], 'tags': a['tags'], 'author': AUTHOR,
        }
        data['blog'].append(item)
        out = json.dumps(data, ensure_ascii=False, indent=2) + ('\n' if raw.endswith('\n') else '')
        path.write_text(out, encoding='utf-8')
        return [p['data'], cover_rel]
    item = {
        'slug': slug, 'title_ru': a['title_ru'], 'title_en': a['title_en'], 'cover': cover_url,
        'publishedAt': today, 'published': True,
        'excerpt_ru': a['excerpt_ru'], 'excerpt_en': a['excerpt_en'], 'tags': a['tags'], 'author': AUTHOR,
        # подпись обязательна: без неё MediaSlot сайта Aura обложку не показывает
        'coverCaption_ru': a['title_ru'], 'coverCaption_en': a['title_en'],
        'body_ru': a['body_ru'], 'body_en': a['body_en'],
    }
    rel = f"{p['data']}/{slug}.json"
    (site / rel).write_text(json.dumps(item, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return [rel, cover_rel]


def check(a):
    for k in ('title_ru', 'title_en', 'excerpt_ru', 'excerpt_en', 'body_ru', 'body_en'):
        assert a[k] and a[k].strip(), f"{a['slug']}: пустое поле {k}"
    assert a['photo'].exists(), f"{a['slug']}: нет обложки {a['photo'].name}"
    kb = a['photo'].stat().st_size // 1024
    assert kb <= 800, f"{a['slug']}: обложка {kb} КБ — больше 800 КБ"
    for k in ('body_ru', 'body_en'):
        left = re.findall(r'\*\*|^#{3,}\s|\]\(https?://', a[k], re.M)
        assert not left, f"{a['slug']}: в {k} осталась разметка {left[:3]}"


def publish(project, d, site, dry):
    fix = make_link_fixer(gtt_validator(site) if project == 'GTT' else None)
    a = article(d, fix)
    check(a)
    today = dt.datetime.now(MSK).date().isoformat()
    if on_site(project, site, a['slug']):
        print(f"  · {a['slug']}: уже на сайте — пропуск")
        return None
    if dry:
        print(f"{d.name} → {PROJECTS[project]['domain']}/blog/{a['slug']}  (дата на сайте {today})")
        print(a['body_ru'][:1500])
        return None
    files = write_site(project, site, a, today)
    print(f"PUBLISHED_SLUG={a['slug']}")
    print(f"PUBLISHED_FILES={' '.join(files)}")
    return a['slug']


# ---------- учёт в POST-HUB ----------

def site_slugs(project):
    """Какие статьи уже есть в репозитории сайта на GitHub (публичные raw-файлы, без токена)."""
    p = PROJECTS[project]
    if project == 'GTT':
        url = f"https://raw.githubusercontent.com/{p['repo']}/{p['branch']}/{p['data']}"
        data = json.loads(urllib.request.urlopen(url, timeout=60).read().decode('utf-8'))
        return {b.get('slug') for b in data.get('blog', [])}
    return None   # у Aura проверяем по одному файлу


def aura_has(slug):
    p = PROJECTS['AURA']
    url = f"https://raw.githubusercontent.com/{p['repo']}/{p['branch']}/{p['data']}/{slug}.json"
    try:
        urllib.request.urlopen(urllib.request.Request(url, method='HEAD'), timeout=30)
        return True
    except Exception:
        return False


def sync(project, dry):
    slugs = site_slugs(project)
    moved = []
    now = dt.datetime.now(MSK)
    for d in folders(project):
        when, meta = when_of(d)
        if when > now + dt.timedelta(days=1):
            break                              # дальше — будущие статьи, их на сайте быть не может
        slug = meta['slug']
        live = (slug in slugs) if slugs is not None else aura_has(slug)
        if not live:
            continue
        base = blog_dir(project) / 'PUBLISHED' / meta['date'][:7]
        print(f'  ✓ {d.name} → PUBLISHED/{base.name}/')
        if dry:
            continue
        base.mkdir(parents=True, exist_ok=True)
        git('mv', str(d), str(base / d.name), cwd=HUB)
        info = {'published_at': meta['date'], 'url': f"{PROJECTS[project]['domain']}/blog/{slug}",
                'published_by': f"workflow «Блог из POST-HUB» репозитория {PROJECTS[project]['repo']} (blog_site.py)"}
        (base / d.name / 'info.json').write_text(json.dumps(info, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        moved.append(slug)
    print(f'{project}: перенесено в PUBLISHED — {len(moved)}')
    return moved


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--project', required=True, choices=sorted(PROJECTS))
    ap.add_argument('--queue', action='store_true')
    ap.add_argument('--redate')
    ap.add_argument('--post')
    ap.add_argument('--due', action='store_true')
    ap.add_argument('--sync', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--site')
    a = ap.parse_args()
    pr = a.project
    site = Path(a.site).resolve() if a.site else None
    if a.queue:
        for d in folders(pr):
            when, meta = when_of(d)
            print(f"{when:%d.%m.%Y %H:%M}  {meta['slug']:<60} {meta['title'][:60]}")
    elif a.redate:
        start = dt.date.fromisoformat(a.redate)
        for i, d in enumerate(folders(pr)):
            date = (start + dt.timedelta(days=i)).isoformat()
            when, meta = when_of(d)
            hhmm = meta.get('publish_time', '15:00')
            name = f"{date}_{hhmm.replace(':', '')}_{d.name.split('_', 2)[2]}"
            for lang in ('ru', 'en', 'zh'):
                if (d / f'post.{lang}.md').exists():
                    set_date(d / f'post.{lang}.md', date)
            if name != d.name:
                git('mv', str(d), str(d.parent / name), cwd=HUB)
        print(f'{pr}: {len(folders(pr))} статей с {start:%d.%m.%Y}, по одной в день')
    elif a.post:
        assert site, '--site обязателен'
        d = Path(a.post)
        d = d if d.is_absolute() else (HUB / d if (HUB / d).exists() else blog_dir(pr) / 'READY' / d)
        publish(pr, d.resolve(), site, a.dry_run)
    elif a.due:
        assert site, '--site обязателен'
        if not allowed(pr):
            print(f'{pr}/BLOG: стоп-кран CONTROL/PUBLISHING.yaml — ничего не публикую')
            return
        now = dt.datetime.now(MSK)
        done = 0
        for d in folders(pr):
            when, meta = when_of(d)
            if when > now:
                break
            if done >= MAX_PER_RUN:
                print(f'  · лимит {MAX_PER_RUN} статьи за прогон — остальные в следующий раз')
                break
            if publish(pr, d, site, a.dry_run):
                done += 1
        if not done:
            print(f'{pr}: публиковать нечего (следующая — {when_of(folders(pr)[0])[0]:%d.%m %H:%M} МСК)' if folders(pr) else f'{pr}: очередь пуста')
    elif a.sync:
        sync(pr, a.dry_run)
    else:
        ap.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
