#!/usr/bin/env python3
"""Публикация по расписанию — команда пульта `publish` (CONTROL/AGENT.md, раздел 6). Работает без агента: её каждый час
запускает GitHub Actions (`.github/workflows/publish.yml`); любой агент или человек запускает её так же руками.

python3 CONTROL/TOOLS/publish.py --check                 # проверить доступы (токены) всех подключённых сетей
python3 CONTROL/TOOLS/publish.py --due --dry-run         # что вышло бы сейчас — ничего не публикует, токены не нужны
python3 CONTROL/TOOLS/publish.py --due                   # опубликовать всё, чему наступило время
python3 CONTROL/TOOLS/publish.py --post GTT/INSTAGRAM/CAROUSEL/READY/2026-11-02_1900_tur-robotics [--dry-run]

Очередь — папки `<ПРОЕКТ>/<СЕТЬ>[/<ФОРМАТ>]/READY/ГГГГ-ММ-ДД_ЧЧММ_тема/` (время — Москва, в имени папки), в папке —
`post.md` (шапка + текст) и файлы поста. Сеть публикует адаптер `net_<сеть>.py` (сейчас — `net_instagram.py` и
`net_facebook.py`, страницы Facebook — с 12.10.2026, `net_threads.py` — Threads);
сеть без адаптера пропускается. Вышедший пост переносится в `PUBLISHED/ГГГГ-ММ/<имя>/` и получает `info.json`
(когда вышло, ссылка, id). Ошибка — `publish-error.json` в папке поста; после 3 ошибок пост ждёт человека.
Стоп-кран — `CONTROL/PUBLISHING.yaml`: `pause: true` останавливает публикации по расписанию (`--due`); один утверждённый пост
по прямой команде пользователя выходит вручную: `--post <папка>` (Actions → «Публикация» → publish + путь).
Пост, опоздавший больше чем на `--max-late` часов (по умолчанию 36), сам не выходит — только через `--post`.
"""
import argparse
import datetime as dt
import importlib
import json
import re
import shutil
import subprocess
import sys
import traceback
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
MSK = dt.timezone(dt.timedelta(hours=3))
NAME = re.compile(r'^(\d{4}-\d{2}-\d{2})_(\d{4})_.+$')
ADAPTERS = {'INSTAGRAM': 'net_instagram', 'FACEBOOK': 'net_facebook', 'THREADS': 'net_threads'}
FEED_FIRST = {'POST': 0, 'CAROUSEL': 0, 'REELS': 0, 'VIDEO': 0, 'STORIES': 1}
MAX_ATTEMPTS = 3


def parse_meta(text):
    """Шапка между `---` → dict (строки в кавычках и списки — JSON, числа — int) и текст ниже шапки."""
    _, head, body = text.split('---\n', 2)
    meta = {}
    for line in head.strip().split('\n'):
        if ': ' not in line:
            continue
        k, v = line.split(': ', 1)
        v = v.strip()
        try:
            meta[k] = json.loads(v) if v[:1] in '"[{' else int(v) if v.isdigit() else v
        except json.JSONDecodeError:
            meta[k] = v
    return meta, body


def paused():
    f = HUB / 'CONTROL/PUBLISHING.yaml'
    return f.exists() and re.search(r'^pause:\s*true\b', f.read_text(encoding='utf-8'), re.M) is not None


def queue():
    """Все посты в READY: (время, проект, сеть, формат, папка)."""
    out = []
    for ready in sorted(HUB.glob('*/*/READY')) + sorted(HUB.glob('*/*/*/READY')):
        rel = ready.relative_to(HUB).parts
        project, network = rel[0], rel[1]
        fmt = rel[2] if len(rel) == 4 else network
        for d in sorted(p for p in ready.iterdir() if p.is_dir() and NAME.match(p.name)):
            m = NAME.match(d.name)
            t = dt.datetime.strptime(f'{m.group(1)} {m.group(2)}', '%Y-%m-%d %H%M').replace(tzinfo=MSK)
            out.append((t, project, network, fmt, d))
    out.sort(key=lambda x: (x[0], FEED_FIRST.get(x[3], 0), str(x[4])))
    return out


def adapter(network):
    name = ADAPTERS.get(network)
    return importlib.import_module(name) if name else None


def errors_of(d):
    f = d / 'publish-error.json'
    return json.loads(f.read_text(encoding='utf-8')) if f.exists() else {'attempts': 0}


def archive(d, project, network, fmt, result, when):
    """READY/<имя> → PUBLISHED/ГГГГ-ММ/<имя> + info.json (файлы только переносятся)."""
    base = d.parent.parent / 'PUBLISHED' / when.strftime('%Y-%m')
    base.mkdir(parents=True, exist_ok=True)
    dst = base / d.name
    (d / 'publish-error.json').unlink(missing_ok=True)
    try:
        subprocess.run(['git', 'mv', str(d), str(dst)], cwd=HUB, check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        shutil.move(str(d), str(dst))
    info = {'published_at': when.isoformat(timespec='seconds'), 'url': result.get('url'), 'post_id': result.get('post_id'),
            'published_by': 'script', **{k: v for k, v in result.items() if k not in ('url', 'post_id')}}
    (dst / 'info.json').write_text(json.dumps(info, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return dst


def run_one(t, project, network, fmt, d, dry):
    ad = adapter(network)
    rel = d.relative_to(HUB)
    if not ad:
        print(f'  · {rel}: сеть {network} пока не подключена — пропуск')
        return 'skip'
    meta, body = parse_meta((d / 'post.md').read_text(encoding='utf-8'))
    try:
        result = ad.publish(project, fmt, d, meta, body, dry=dry)
    except getattr(ad, 'NotConnected', ()) as e:                     # нет токена — сеть проекта не подключена
        print(f'  · {rel}: {e} — пропуск')
        return 'skip'
    except Exception as e:                                           # ошибка сети или данных — пишем и идём дальше
        msg = f'{type(e).__name__}: {e}'
        print(f'  ✗ {rel}: {msg}')
        if not dry:
            err = errors_of(d)
            err.update({'attempts': err['attempts'] + 1, 'last_error': msg,
                        'at': dt.datetime.now(MSK).isoformat(timespec='seconds'), 'trace': traceback.format_exc()[-2000:]})
            (d / 'publish-error.json').write_text(json.dumps(err, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        return 'error'
    if dry:
        print(f'  ✓ {rel}: готов к выходу ({result.get("plan", "")})')
        return 'ok'
    dst = archive(d, project, network, fmt, result, dt.datetime.now(MSK))
    print(f'  ✓ {rel} → {dst.relative_to(HUB)} · {result.get("url")}')
    return 'ok'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='проверить доступы всех подключённых сетей')
    ap.add_argument('--due', action='store_true', help='посты, чьё время наступило')
    ap.add_argument('--post', help='папка одного поста (публикуется сразу, независимо от времени)')
    ap.add_argument('--dry-run', action='store_true', help='только показать и проверить, ничего не публиковать')
    ap.add_argument('--max-late', type=float, default=36, help='часов опоздания, после которых пост сам не выходит')
    ap.add_argument('--now', help='считать «сейчас» этим временем (ГГГГ-ММ-ДД ЧЧ:ММ, Москва) — для проверки плана')
    a = ap.parse_args()

    if a.check:
        bad = 0
        projects = sorted(p.name for p in HUB.iterdir() if p.is_dir() and (p / 'RULES.md').exists())
        for network, mod in ADAPTERS.items():
            ad = importlib.import_module(mod)
            for project in projects:
                if not (HUB / project / network).exists():
                    continue
                ok, msg = ad.check(project)
                bad += ok is False
                print(f'{"✓" if ok else "·" if ok is None else "✗"} {project}/{network}: {msg}')
        sys.exit(1 if bad else 0)

    if paused() and not a.dry_run and not a.post:                   # пауза держит расписание; один утверждённый пост — вручную
        print('⏸ публикации по расписанию на паузе (CONTROL/PUBLISHING.yaml: pause: true) — ничего не публикую')
        return
    now = dt.datetime.strptime(a.now, '%Y-%m-%d %H:%M').replace(tzinfo=MSK) if a.now else dt.datetime.now(MSK)
    items = queue()
    if a.post:
        target = (HUB / a.post).resolve()
        items = [x for x in items if x[4].resolve() == target]
        if not items:
            sys.exit(f'нет такого поста в READY: {a.post}')
    elif a.due:
        other = [x for x in items if x[2] not in ADAPTERS and x[0] <= now]
        items = [x for x in items if x[2] in ADAPTERS]
        if other:
            print(f'  · в сетях без публикатора POST-HUB: {len(other)} (их пока публикуют другие системы — не трогаю)')
        due, late = [], []
        for x in items:
            if x[0] > now:
                continue
            (late if now - x[0] > dt.timedelta(hours=a.max_late) else due).append(x)
        for x in late:
            print(f'  ! {x[4].relative_to(HUB)}: опоздал больше чем на {a.max_late:g} ч — сам не выйдет (запусти --post)')
        items = [x for x in due if errors_of(x[4])['attempts'] < MAX_ATTEMPTS]
        for x in due:
            if errors_of(x[4])['attempts'] >= MAX_ATTEMPTS:
                print(f'  ! {x[4].relative_to(HUB)}: {MAX_ATTEMPTS} ошибки подряд — ждёт человека (publish-error.json)')
    else:
        ahead = [x for x in items if x[0] > now][:10]
        print(f'В READY: {len(items)}. Ближайшие:')
        for t, project, network, fmt, d in ahead:
            print(f'  {t:%d.%m %H:%M} {project}/{network}/{fmt}: {d.name}')
        return
    print(f'{"Проверка" if a.dry_run else "Публикация"}: {len(items)} пост(ов), сейчас {now:%d.%m.%Y %H:%M} МСК')
    res = [run_one(*x, dry=a.dry_run) for x in items]
    print(f'итог: вышло/готово {res.count("ok")}, ошибок {res.count("error")}, пропущено {res.count("skip")}')
    sys.exit(1 if 'error' in res else 0)


if __name__ == '__main__':
    main()
