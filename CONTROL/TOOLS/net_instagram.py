"""Адаптер Instagram для `publish.py`: официальный API Instagram (вход через Instagram, graph.instagram.com).

Доступ — секреты GitHub `IG_TOKEN_<ПРОЕКТ>` (токен) и `IG_USER_<ПРОЕКТ>` (ID аккаунта; без него берётся из токена),
как получить — `<ПРОЕКТ>/INSTAGRAM/RULES.md`, «Подключение».
Instagram забирает файлы сам по публичной ссылке, а POST-HUB закрытый, поэтому ссылки — на публичный VIDEO-HUB:
- картинки: поле `media_urls` в шапке поста (их пишет `to_ready.py` — копирует JPG поста в VIDEO-HUB
  `finished-videos/publish/<проект>-instagram/<имя поста>/`); перед публикацией файл по ссылке сверяется с файлом в READY;
- видео: поле `video_hub` (путь мастера в VIDEO-HUB, строка или список) → ссылка Git LFS media.githubusercontent.com.
Форматы: CAROUSEL (2–10 картинок/видео + подпись), REELS (видео + подпись, `share_to_feed`), STORIES (каждый файл —
отдельная сторис, по порядку), POST (одно фото с подписью; одно видео уходит как Reels).
Обложка Reels: `cover_url` (картинка) или `thumb_offset` (кадр ролика, мс; без поля — первый кадр).
API не умеет: музыку из библиотеки Instagram, стикеры и ссылки в Stories, отметки товаров.
Отметка аккаунтов в Stories (`user_tags`, Instagram API с 09.07.2025): поле `story_mentions` в шапке — список @имён
публичных аккаунтов. Отмеченный аккаунт получает уведомление и кнопку «Добавить в свою историю» — так делается репост
(решение пользователя 12.10.2026: «Сделай пост сторис для Ауры, чтобы я репост мог сделать далее»). Если Instagram
отметку не принял (аккаунт закрытый, имя с ошибкой), сторис выходит без неё, в результате — `warning`.
"""
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = 'https://graph.instagram.com/' + os.environ.get('IG_API_VERSION', 'v25.0')
VH_REPO = os.environ.get('MEDIA_REPO', 'Ostap-87/VIDEO-HUB')
VH_BRANCH = os.environ.get('MEDIA_BRANCH', 'main')
VH_RAW = f'https://raw.githubusercontent.com/{VH_REPO}/{VH_BRANCH}/'
VH_LFS = f'https://media.githubusercontent.com/media/{VH_REPO}/{VH_BRANCH}/'
VIDEO_EXT = ('.mp4', '.mov', '.m4v')
CAPTION_MAX, TAGS_MAX = 2200, 30


class IGError(Exception):
    pass


class NotConnected(Exception):
    pass


# Лимиты запросов Instagram (code 4 — лимит приложения, 17 — пользователя, 32 — страницы, 613 — частота вызовов).
# 17 и 18.10.2026 так не вышли карусели Aura по 10 слайдов: после роликов и карусели GTT лимит за час был выбран,
# и media_publish отвечал «Application request limit reached (code 4, subcode 2207051)». Лимит считается за
# скользящий час, поэтому ждём и повторяем тот же вызов (до ~20 минут), а не тратим попытку публикации.
# Исключение — подкод 2207051 («публикация похожа на спам», официальная таблица ошибок Meta): его не повторяем.
# 2207085 («Fatal», code -1) — по описанию Ayrshare, ошибка состояния аккаунта, а не поста: тоже не повторяем.
RATE_CODES = ('code 4,', 'code 17,', 'code 32,', 'code 613,')
RATE_WAITS = (60, 60, 120, 120, 180, 180, 240, 240)


def _http(method, url, params=None, timeout=60):
    for wait in RATE_WAITS + (None,):
        try:
            return _http_once(method, url, params, timeout)
        except IGError as e:
            # 2207051 — Instagram заподозрил спам и закрыл публикацию для аккаунта: повторы только усугубят, ждём человека
            if wait is None or 'subcode 2207051' in str(e) or not any(c in str(e) for c in RATE_CODES):
                raise
            print(f'  … Instagram: лимит запросов ({e}), жду {wait} с и повторяю', flush=True)
            time.sleep(wait)


def _http_once(method, url, params=None, timeout=60):
    data = urllib.parse.urlencode(params or {}).encode() if method == 'POST' else None
    if method == 'GET' and params:
        url += ('&' if '?' in url else '?') + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode() or '{}')
    except urllib.error.HTTPError as e:
        try:
            err = json.loads(e.read().decode()).get('error', {})
            msg = f"{err.get('message', e.reason)} (code {err.get('code')}, subcode {err.get('error_subcode')})"
        except Exception:
            msg = str(e)
        raise IGError(msg.replace(os.environ.get('_IG_TOKEN', '§'), '***')) from None


def creds(project):
    token = os.environ.get(f'IG_TOKEN_{project}')
    if not token:
        return None, None
    os.environ['_IG_TOKEN'] = token
    user = os.environ.get(f'IG_USER_{project}') or str(_http('GET', f'{API}/me', {'fields': 'user_id', 'access_token': token})['user_id'])
    return token, user


def check(project):
    """(True / False / None, сообщение): None — секретов нет, сеть не подключена."""
    if not os.environ.get(f'IG_TOKEN_{project}'):
        return None, f'нет секрета IG_TOKEN_{project} — не подключено'
    try:
        token, user = creds(project)
        me = _http('GET', f'{API}/me', {'fields': 'user_id,username,account_type', 'access_token': token})
        lim = _http('GET', f'{API}/{user}/content_publishing_limit', {'fields': 'quota_usage,config', 'access_token': token})
        q = (lim.get('data') or [{}])[0]
        return True, (f"доступ есть: @{me.get('username')} ({me.get('account_type')}, id {me.get('user_id')}); "
                      f"публикаций за сутки {q.get('quota_usage', '?')} из {q.get('config', {}).get('quota_total', '?')}")
    except IGError as e:
        return False, f'ошибка доступа: {e}'


def caption_of(body):
    """Текст поста (Markdown) → подпись Instagram: без разметки, ссылки — текстом."""
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 \2', body)
    t = re.sub(r'\*\*([^*]+)\*\*', r'\1', t)
    t = re.sub(r'(?m)^#{1,6}\s+', '', t)                          # заголовки Markdown (хештеги #GTT без пробела не трогаем)
    return t.strip()


def _probe(url):
    """Проверить, что ссылка публичная: (код, тип, длина), первые 2 МБ для картинок."""
    req = urllib.request.Request(url, headers={'Range': 'bytes=0-0'})
    with urllib.request.urlopen(req, timeout=60) as r:
        size = r.headers.get('Content-Range', '').split('/')[-1] or r.headers.get('Content-Length')
        return r.status, r.headers.get('Content-Type', ''), int(size) if size and size.isdigit() else None


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def media_of(project, fmt, d, meta):
    """Список (вид, ссылка, локальный файл или None) для поста."""
    out = []
    urls = meta.get('media_urls') or []
    if isinstance(urls, str):
        urls = [urls]
    for u in urls:
        local = d / Path(urllib.parse.urlparse(u).path).name
        out.append(('video' if u.lower().endswith(VIDEO_EXT) else 'image', u, local if local.exists() else None))
    vids = meta.get('video_hub') or []
    if isinstance(vids, str):
        vids = [vids]
    for p in vids:
        if p.lower().endswith(VIDEO_EXT):
            out.append(('video', VH_LFS + urllib.parse.quote(p), None))
    if not out:
        local = sorted(x for x in d.iterdir() if x.suffix.lower() in ('.jpg', '.jpeg') + VIDEO_EXT)
        if local:
            raise IGError('у файлов поста нет публичных ссылок (media_urls) — перенеси пост в READY через to_ready.py')
        raise IGError('в посте нет ни картинок, ни видео')
    return out


def verify(media, caption, fmt):
    """Проверки до публикации: ссылки открываются, картинки — JPEG и совпадают с файлами в READY, лимиты подписи."""
    if len(caption) > CAPTION_MAX:
        raise IGError(f'подпись {len(caption)} знаков — больше {CAPTION_MAX}')
    if len(re.findall(r'(?<!\w)#\w', caption)) > TAGS_MAX:
        raise IGError(f'хештегов больше {TAGS_MAX}')
    if fmt == 'CAROUSEL' and not 2 <= len(media) <= 10:
        raise IGError(f'в карусели {len(media)} файлов, можно 2–10')
    for kind, url, local in media:
        try:
            code, ctype, size = _probe(url)
        except urllib.error.HTTPError as e:
            raise IGError(f'ссылка не открывается ({e.code}): {url}') from None
        if kind == 'image':
            if 'jpeg' not in ctype and 'jpg' not in ctype:
                raise IGError(f'картинка не JPEG ({ctype}): {url}')
            if local is not None:
                with urllib.request.urlopen(url, timeout=60) as r:
                    if _sha(r.read()) != _sha(local.read_bytes()):
                        raise IGError(f'файл по ссылке отличается от утверждённого {local.name} — перезапусти to_ready.py')
        elif size is not None and size < 100_000:
            raise IGError(f'видео по ссылке подозрительно маленькое ({size} байт) — проверь Git LFS: {url}')


def _container(token, user, params):
    return _http('POST', f'{API}/{user}/media', {**params, 'access_token': token})['id']


def _wait(token, cid, timeout):
    t0 = time.time()
    while True:
        st = _http('GET', f'{API}/{cid}', {'fields': 'status_code,status', 'access_token': token})
        code = st.get('status_code')
        if code in ('FINISHED', 'PUBLISHED'):
            return
        if code in ('ERROR', 'EXPIRED'):
            raise IGError(f'Instagram не принял файл: {st.get("status")}')
        if time.time() - t0 > timeout:
            raise IGError(f'файл обрабатывается дольше {timeout} с (контейнер {cid})')
        time.sleep(5 if timeout <= 120 else 15)                 # видео обрабатывается минутами — опрашиваем реже, это экономит лимит


def _publish(token, user, cid):
    # Instagram иногда отвечает «Media ID is not available (9007/2207027)», хотя контейнер уже FINISHED: медиа ещё
    # не доехало до публикации. Ждём и повторяем тот же контейнер (17.10.2026 так не вышла карусель Aura MATRIX-3).
    for attempt in range(4):
        try:
            mid = _http('POST', f'{API}/{user}/media_publish', {'creation_id': cid, 'access_token': token})['id']
            break
        except IGError as e:
            if 'code 9007' not in str(e) or attempt == 3:
                raise
            time.sleep(20)
    try:
        link = _http('GET', f'{API}/{mid}', {'fields': 'permalink', 'access_token': token}).get('permalink')
    except IGError:
        link = None
    return mid, link


def publish(project, fmt, d, meta, body, dry=False):
    caption = caption_of(body)
    media = media_of(project, fmt, d, meta)
    if fmt == 'POST' and media[0][0] == 'video':
        fmt = 'REELS'
    verify(media, caption if fmt != 'STORIES' else '', fmt)
    plan = f"{fmt}: {len(media)} файл(ов), подпись {len(caption)} знаков" if fmt != 'STORIES' else f'STORIES: {len(media)} шт.' + (f" · отметка {meta['story_mentions']}" if meta.get('story_mentions') else '')
    if dry:
        return {'plan': plan}
    token, user = creds(project)
    if not token:
        raise NotConnected(f'Instagram {project} не подключён (нет секрета IG_TOKEN_{project})')
    vid_wait = 900
    if fmt == 'CAROUSEL':
        kids = []
        for kind, url, _ in media:
            p = {'is_carousel_item': 'true', **({'image_url': url} if kind == 'image' else {'media_type': 'VIDEO', 'video_url': url})}
            kids.append(_container(token, user, p))
        for k, (kind, _, _) in zip(kids, media):
            _wait(token, k, vid_wait if kind == 'video' else 120)
        cid = _container(token, user, {'media_type': 'CAROUSEL', 'children': ','.join(kids), 'caption': caption})
        _wait(token, cid, 120)
        mid, link = _publish(token, user, cid)
        return {'post_id': mid, 'url': link, 'format': fmt, 'files': len(media)}
    if fmt == 'REELS':
        p = {'media_type': 'REELS', 'video_url': media[0][1], 'caption': caption, 'share_to_feed': 'true'}
        if meta.get('cover_url'):
            p['cover_url'] = meta['cover_url']
        elif meta.get('thumb_offset') is not None:                # обложка — кадр ролика на этой миллисекунде
            p['thumb_offset'] = str(meta['thumb_offset'])
        cid = _container(token, user, p)
        _wait(token, cid, vid_wait)
        mid, link = _publish(token, user, cid)
        return {'post_id': mid, 'url': link, 'format': fmt}
    if fmt == 'STORIES':
        ids, warn = [], None
        tags = meta.get('story_mentions') or []
        tags = [tags] if isinstance(tags, str) else tags
        tags = json.dumps([{'username': t.lstrip('@')} for t in tags]) if tags else None
        for kind, url, _ in media:                                  # по порядку: часть 1, часть 2 …
            p = {'media_type': 'STORIES', **({'image_url': url} if kind == 'image' else {'video_url': url})}
            if tags:
                p['user_tags'] = tags                               # отметка аккаунта → у него кнопка «Добавить в свою историю»
            try:
                cid = _container(token, user, p)
            except IGError as e:
                if not tags:
                    raise
                warn = f'отметку {meta.get("story_mentions")} Instagram не принял ({e}) — сторис вышла без неё'
                tags = None
                p.pop('user_tags')
                cid = _container(token, user, p)
            _wait(token, cid, vid_wait if kind == 'video' else 120)
            ids.append(_publish(token, user, cid)[0])
        res = {'post_id': ids[0], 'url': None, 'format': fmt, 'story_ids': ids}
        if meta.get('story_mentions'):
            res['mentions'] = [] if warn else meta['story_mentions']
        if warn:
            res['warning'] = warn
        return res
    if fmt == 'POST':
        cid = _container(token, user, {'image_url': media[0][1], 'caption': caption})
        _wait(token, cid, 120)
        mid, link = _publish(token, user, cid)
        return {'post_id': mid, 'url': link, 'format': fmt}
    raise IGError(f'формат {fmt} адаптер не знает')
