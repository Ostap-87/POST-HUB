"""Адаптер Threads для `publish.py`: официальный Threads API (graph.threads.net), токен пользователя Threads.

Подключено по решению пользователя 12.10.2026 («тредс подключить, чтобы он дублировал информацию»).
Доступ — секрет GitHub `THREADS_TOKEN_<ПРОЕКТ>` (долгий токен Threads, 60 дней), ID — `THREADS_USER_<ПРОЕКТ>` или из токена.
Как получить — `<ПРОЕКТ>/THREADS/RULES.md`, «Подключение». Очередь — `<ПРОЕКТ>/THREADS/READY/<ГГГГ-ММ-ДД_ЧЧММ_тема>/post.md`.
Вид поста — по содержимому: видео (`video_hub`) → VIDEO; картинки (`media_urls`, публичные ссылки VIDEO-HUB) → IMAGE или
CAROUSEL (2–20); иначе — TEXT. Текст — поле `threads_text` в шапке, а без него — подпись поста, ужатая до 500 знаков
(абзацы целиком, хештеги убираются, последней строкой — сайт проекта).
"""
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request

from net_instagram import VH_LFS, VIDEO_EXT, _probe, caption_of

API = 'https://graph.threads.net/' + os.environ.get('THREADS_API_VERSION', 'v1.0')
TEXT_MAX = 500
SITE = {'AURA': 'aura-robotics.ru', 'GTT': 'globaltechtour.ru', 'OSTAPDOTCENKO': 'ostapdotcenko.ru'}


class THError(Exception):
    pass


class NotConnected(Exception):
    pass


def _http(method, url, params=None, timeout=60):
    data = urllib.parse.urlencode(params or {}).encode() if method == 'POST' else None
    if method == 'GET' and params:
        url += ('&' if '?' in url else '?') + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=data, method=method), timeout=timeout) as r:
            return json.loads(r.read().decode() or '{}')
    except urllib.error.HTTPError as e:
        try:
            err = json.loads(e.read().decode()).get('error', {})
            msg = f"{err.get('message', e.reason)} (code {err.get('code')}, subcode {err.get('error_subcode')})"
        except Exception:
            msg = str(e)
        tok = os.environ.get('_TH_TOKEN')
        raise THError(msg.replace(tok, '***') if tok else msg) from None


def creds(project):
    token = os.environ.get(f'THREADS_TOKEN_{project}')
    if not token:
        return None, None
    os.environ['_TH_TOKEN'] = token
    user = os.environ.get(f'THREADS_USER_{project}') or str(_http('GET', f'{API}/me', {'fields': 'id', 'access_token': token})['id'])
    return token, user


def check(project):
    if not os.environ.get(f'THREADS_TOKEN_{project}'):
        return None, f'нет секрета THREADS_TOKEN_{project} — не подключено'
    try:
        token, user = creds(project)
        me = _http('GET', f'{API}/me', {'fields': 'id,username', 'access_token': token})
        lim = _http('GET', f'{API}/{user}/threads_publishing_limit', {'fields': 'quota_usage,config', 'access_token': token})
        q = (lim.get('data') or [{}])[0]
        return True, (f"доступ есть: @{me.get('username')} (id {me.get('id')}); "
                      f"публикаций за сутки {q.get('quota_usage', '?')} из {q.get('config', {}).get('quota_total', '?')}")
    except THError as e:
        return False, f'ошибка доступа: {e}'


def short_text(project, body, meta, video=False):
    """Текст для Threads: `threads_text` или подпись, ужатая до 500 знаков абзацами, без хештегов, с сайтом в конце.

    Видео — без «Листай карусель →»; Reels-версия карусели (в подписи есть «Листай карусель») берёт только первый абзац,
    чтобы в ленте Threads не было двух одинаковых длинных текстов за день (полный текст уйдёт с каруселью).
    """
    if meta.get('threads_text'):
        return meta['threads_text'][:TEXT_MAX]
    paras = [p.strip() for p in caption_of(body).split('\n\n') if p.strip()]
    paras = [p for p in paras if not re.fullmatch(r'(#\S+\s*)+', p) and not p.startswith('Музыка:')]
    site = SITE.get(project, '')
    paras = [p for p in paras if site not in p] if site else paras
    if video and any('Листай карусель' in p for p in paras):
        paras = ['\n'.join(l for l in paras[0].split('\n') if 'Листай карусель' not in l).strip()]
    out = ''
    for p in paras:
        cand = (out + '\n\n' + p).strip()
        if len(cand) + len(site) + 2 > TEXT_MAX:
            break
        out = cand
    if not out and paras:                                            # первый абзац длинный — режем по предложениям
        out = paras[0][: TEXT_MAX - len(site) - 4].rsplit('. ', 1)[0] + '.'
    return (out + ('\n\n' + site if site else '')).strip()


def media_of(meta):
    urls = meta.get('media_urls') or []
    urls = [urls] if isinstance(urls, str) else urls
    vids = meta.get('video_hub') or []
    vids = [vids] if isinstance(vids, str) else vids
    videos = [VH_LFS + urllib.parse.quote(v) for v in vids if v.lower().endswith(VIDEO_EXT)]
    return [u for u in urls if not u.lower().endswith(VIDEO_EXT)], videos


def _wait(token, cid, timeout):
    t0 = time.time()
    while True:
        st = _http('GET', f'{API}/{cid}', {'fields': 'status,error_message', 'access_token': token})
        if st.get('status') in ('FINISHED', 'PUBLISHED'):
            return
        if st.get('status') in ('ERROR', 'EXPIRED'):
            raise THError(f"Threads не принял файл: {st.get('error_message') or st.get('status')}")
        if time.time() - t0 > timeout:
            raise THError(f'файл обрабатывается дольше {timeout} с (контейнер {cid})')
        time.sleep(5)


def publish(project, fmt, d, meta, body, dry=False):
    imgs, vids = media_of(meta)
    text = short_text(project, body, meta, video=bool(vids))
    kind = 'VIDEO' if vids else 'CAROUSEL' if len(imgs) > 1 else 'IMAGE' if imgs else 'TEXT'
    for u in vids + imgs:
        try:
            _probe(u)
        except urllib.error.HTTPError as e:
            raise THError(f'ссылка не открывается ({e.code}): {u}') from None
    if len(imgs) > 20:
        imgs = imgs[:20]
    plan = f'{kind}: картинок {len(imgs)}, видео {len(vids)}, текст {len(text)} знаков'
    if dry:
        return {'plan': plan}
    token, user = creds(project)
    if not token:
        raise NotConnected(f'Threads {project} не подключён (нет секрета THREADS_TOKEN_{project})')
    base = {'access_token': token}
    if kind == 'CAROUSEL':
        kids = [_http('POST', f'{API}/{user}/threads', {**base, 'media_type': 'IMAGE', 'image_url': u, 'is_carousel_item': 'true'})['id'] for u in imgs]
        for k in kids:
            _wait(token, k, 120)
        cid = _http('POST', f'{API}/{user}/threads', {**base, 'media_type': 'CAROUSEL', 'children': ','.join(kids), 'text': text})['id']
    elif kind == 'VIDEO':
        cid = _http('POST', f'{API}/{user}/threads', {**base, 'media_type': 'VIDEO', 'video_url': vids[0], 'text': text})['id']
    elif kind == 'IMAGE':
        cid = _http('POST', f'{API}/{user}/threads', {**base, 'media_type': 'IMAGE', 'image_url': imgs[0], 'text': text})['id']
    else:
        cid = _http('POST', f'{API}/{user}/threads', {**base, 'media_type': 'TEXT', 'text': text})['id']
    _wait(token, cid, 900 if kind == 'VIDEO' else 120)
    mid = _http('POST', f'{API}/{user}/threads_publish', {**base, 'creation_id': cid})['id']
    try:
        link = _http('GET', f'{API}/{mid}', {'fields': 'permalink', 'access_token': token}).get('permalink')
    except THError:
        link = None
    return {'post_id': mid, 'url': link, 'format': kind}
