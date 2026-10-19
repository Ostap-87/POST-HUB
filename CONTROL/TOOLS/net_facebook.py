"""Адаптер Facebook (страницы) для `publish.py`: официальный Graph API Facebook (graph.facebook.com), токен страницы.

Подключено по решению пользователя 12.10.2026 («мы же можем публиковать эти ролики в аккаунтах Фейсбук — Аура и Глобалтех тур?»).
Доступ — секрет GitHub `FB_PAGE_TOKEN_<ПРОЕКТ>` (токен страницы, бессрочный), ID страницы — `FB_PAGE_<ПРОЕКТ>` или из токена
(`/me` токена страницы — сама страница). Как получить — `<ПРОЕКТ>/FACEBOOK/RULES.md`, «Подключение».
В отличие от Instagram, Facebook принимает файлы загрузкой: картинки из папки поста уходят напрямую (POST-HUB закрытый — это
не мешает), видео — по публичной ссылке Git LFS VIDEO-HUB (поле `video_hub`, как у Instagram).
Форматы:
- POST — текст (+ ссылка внутри текста); одна картинка — фото-пост; несколько — один пост с несколькими фото;
  видео (`video_hub`) — видео-пост страницы;
- REELS — вертикальное видео 9:16 (`video_hub`) + подпись — Reels страницы (3 шага: start → загрузка по ссылке → finish);
  Reels Facebook через API — от 3 до 90 с; ролик длиннее (поле `duration`, например «108,7 с») выходит видео-постом
  страницы (`/videos`) — тот же ролик и подпись (14.10.2026: «Техгиганты» GTT 108,7 с);
- STORIES — каждый файл отдельной историей по порядку (картинка — photo_stories, видео — video_stories).
"""
import json
import mimetypes
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

from net_instagram import VH_LFS, VIDEO_EXT, _probe, caption_of

VER = os.environ.get('FB_API_VERSION', 'v26.0')
API = f'https://graph.facebook.com/{VER}'
IMG_EXT = ('.jpg', '.jpeg', '.png')
REELS_MAX_SEC = 90                                                  # предел Reels Facebook через API (3–90 с)
PAGE_IDS = {'AURA': '1275368875661067', 'GTT': '1254540414416697'}     # страницы из RULES.md (проверка, что токен от той страницы)


class FBError(Exception):
    pass


class NotConnected(Exception):
    pass


def _mask(s):
    tok = os.environ.get('_FB_TOKEN')
    return s.replace(tok, '***') if tok else s


def _req(req, timeout):
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode() or '{}')
    except urllib.error.HTTPError as e:
        try:
            err = json.loads(e.read().decode()).get('error', {})
            msg = f"{err.get('message', e.reason)} (code {err.get('code')}, subcode {err.get('error_subcode')})"
        except Exception:
            msg = str(e)
        raise FBError(_mask(msg)) from None


def _http(method, url, params=None, headers=None, timeout=120):
    data = urllib.parse.urlencode(params or {}).encode() if method == 'POST' else None
    if method == 'GET' and params:
        url += ('&' if '?' in url else '?') + urllib.parse.urlencode(params)
    return _req(urllib.request.Request(url, data=data, method=method, headers=headers or {}), timeout)


def _multipart(url, fields, file_field, path, timeout=300):
    """POST multipart/form-data: поля + один файл (картинка из папки поста)."""
    b = uuid.uuid4().hex
    parts = []
    for k, v in fields.items():
        parts.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    ctype = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    parts.append(f'--{b}\r\nContent-Disposition: form-data; name="{file_field}"; filename="{path.name}"\r\nContent-Type: {ctype}\r\n\r\n'.encode())
    parts.append(path.read_bytes())
    parts.append(f'\r\n--{b}--\r\n'.encode())
    req = urllib.request.Request(url, data=b''.join(parts), method='POST', headers={'Content-Type': f'multipart/form-data; boundary={b}'})
    return _req(req, timeout)


def creds(project):
    token = os.environ.get(f'FB_PAGE_TOKEN_{project}')
    if not token:
        return None, None
    os.environ['_FB_TOKEN'] = token
    page = os.environ.get(f'FB_PAGE_{project}') or str(_http('GET', f'{API}/me', {'fields': 'id', 'access_token': token})['id'])
    return token, page


def check(project):
    """(True / False / None, сообщение): None — секрета нет, сеть не подключена."""
    if not os.environ.get(f'FB_PAGE_TOKEN_{project}'):
        return None, f'нет секрета FB_PAGE_TOKEN_{project} — не подключено'
    try:
        token, page = creds(project)
        me = _http('GET', f'{API}/{page}', {'fields': 'id,name,link,followers_count', 'access_token': token})
        want = PAGE_IDS.get(project)
        if want and me.get('id') != want:
            return False, f"токен от другой страницы: «{me.get('name')}» (id {me.get('id')}), а нужна id {want}"
        _http('GET', f'{API}/{page}/published_posts', {'limit': 1, 'fields': 'id', 'access_token': token})
        return True, f"доступ есть: страница «{me.get('name')}» (id {me.get('id')}, подписчиков {me.get('followers_count', '?')})"
    except FBError as e:
        return False, f'ошибка доступа: {e}'


def files_of(d, meta):
    """(картинки из папки поста, ссылки на видео VIDEO-HUB)."""
    imgs = sorted(p for p in d.iterdir() if p.suffix.lower() in IMG_EXT)    # все картинки папки по порядку (карусель → пост с фото)
    vids = meta.get('video_hub') or []
    vids = [vids] if isinstance(vids, str) else vids
    return imgs, [VH_LFS + urllib.parse.quote(v) for v in vids if v.lower().endswith(VIDEO_EXT)]


def seconds_of(meta):
    """Длительность ролика из поля `duration` («108,7 с», «85.7», 49) — или None."""
    m = re.search(r'\d+(?:[.,]\d+)?', str(meta.get('duration') or ''))
    return float(m.group(0).replace(',', '.')) if m else None


def verify(fmt, imgs, vids, text):
    if fmt == 'REELS' and len(vids) != 1:
        raise FBError(f'для Reels нужно одно видео (video_hub), а их {len(vids)}')
    if fmt == 'STORIES' and not (imgs or vids):
        raise FBError('в истории нет ни картинки, ни видео')
    if fmt == 'POST' and not (imgs or vids or text):
        raise FBError('пустой пост: нет ни текста, ни файлов')
    for u in vids:
        try:
            code, ctype, size = _probe(u)
        except urllib.error.HTTPError as e:
            raise FBError(f'ссылка на видео не открывается ({e.code}): {u}') from None
        if size is not None and size < 100_000:
            raise FBError(f'видео по ссылке подозрительно маленькое ({size} байт) — проверь Git LFS: {u}')


def _upload_by_url(upload_url, token, file_url):
    r = _http('POST', upload_url, headers={'Authorization': f'OAuth {token}', 'file_url': file_url}, timeout=600)
    if not r.get('success'):
        raise FBError(f'Facebook не принял видео по ссылке: {r}')


def _wait_video(token, vid, timeout=900):
    # Сразу после загрузки по ссылке Facebook может отвечать «объект не существует» (code 100, subcode 33), пока сам
    # скачивает файл: 19.10.2026 так «упал» видео-пост GTT «ИИ Китая». Несколько минут считаем это «ещё не готово».
    t0 = time.time()
    while True:
        try:
            st = _http('GET', f'{API}/{vid}', {'fields': 'status', 'access_token': token}).get('status', {})
        except FBError as e:
            if 'subcode 33' not in str(e) or time.time() - t0 > 600:
                raise
            time.sleep(20)
            continue
        if st.get('video_status') == 'error' or (st.get('processing_phase') or {}).get('status') == 'error':
            raise FBError(f'Facebook не обработал видео: {json.dumps(st, ensure_ascii=False)[:400]}')
        if st.get('video_status') == 'ready' and (st.get('publishing_phase') or {}).get('status') in (None, 'complete'):
            return
        if time.time() - t0 > timeout:
            raise FBError(f'видео обрабатывается дольше {timeout} с (id {vid})')
        time.sleep(10)


def _pending(d):
    """id видео, созданного прошлой попыткой (pending-video.json): повтор ждёт его, а не загружает ролик заново — без дублей."""
    f = d / 'pending-video.json'
    return json.loads(f.read_text(encoding='utf-8')).get('video_id') if f.exists() else None


def _remember(d, vid):
    (d / 'pending-video.json').write_text(json.dumps({'video_id': vid, 'at': time.strftime('%Y-%m-%dT%H:%M:%S%z')}) + '\n', encoding='utf-8')


def _forget(d):
    (d / 'pending-video.json').unlink(missing_ok=True)


def _photo(token, page, path, published=True, message=None):
    fields = {'access_token': token, 'published': 'true' if published else 'false'}
    if message:
        fields['message'] = message
    return _multipart(f'{API}/{page}/photos', fields, 'source', path)


def publish(project, fmt, d, meta, body, dry=False):
    text = caption_of(body)
    imgs, vids = files_of(d, meta)
    verify(fmt, imgs, vids, text)
    sec = seconds_of(meta)
    as_video = fmt == 'REELS' and sec is not None and sec > REELS_MAX_SEC    # длинный ролик — видео-постом, Reels не примет
    plan = f"{fmt}: картинок {len(imgs)}, видео {len(vids)}, текст {len(text)} знаков"
    if as_video:
        plan += f' — ролик {sec:g} с длиннее {REELS_MAX_SEC} с: выйдет видео-постом страницы'
    if dry:
        return {'plan': plan}
    token, page = creds(project)
    if not token:
        raise NotConnected(f'Facebook {project} не подключён (нет секрета FB_PAGE_TOKEN_{project})')
    if fmt == 'REELS' and not as_video:
        vid = _pending(d)
        if not vid:
            st = _http('POST', f'{API}/{page}/video_reels', {'upload_phase': 'start', 'access_token': token})
            vid = st['video_id']
            _upload_by_url(st.get('upload_url') or f'https://rupload.facebook.com/video-upload/{VER}/{vid}', token, vids[0])
            _http('POST', f'{API}/{page}/video_reels', {'upload_phase': 'finish', 'video_id': vid, 'video_state': 'PUBLISHED',
                                                         'description': text, 'access_token': token})
            _remember(d, vid)
        _wait_video(token, vid)
        _forget(d)
        return {'post_id': vid, 'url': f'https://www.facebook.com/reel/{vid}', 'format': fmt}
    if fmt == 'STORIES':
        ids = []
        for p in imgs:
            ph = _photo(token, page, p, published=False)
            ids.append(_http('POST', f'{API}/{page}/photo_stories', {'photo_id': ph['id'], 'access_token': token}).get('post_id'))
        for u in vids:
            st = _http('POST', f'{API}/{page}/video_stories', {'upload_phase': 'start', 'access_token': token})
            _upload_by_url(st.get('upload_url') or f"https://rupload.facebook.com/video-upload/{VER}/{st['video_id']}", token, u)
            ids.append(_http('POST', f'{API}/{page}/video_stories', {'upload_phase': 'finish', 'video_id': st['video_id'],
                                                                     'access_token': token}).get('post_id'))
        return {'post_id': ids[0] if ids else None, 'url': None, 'format': fmt, 'story_ids': ids}
    # POST (и Reels длиннее 90 с)
    if vids:
        vid = _pending(d)
        if not vid:
            vid = _http('POST', f'{API}/{page}/videos', {'file_url': vids[0], 'description': text, 'access_token': token}, timeout=600)['id']
            _remember(d, vid)
        _wait_video(token, vid)
        _forget(d)
        return {'post_id': vid, 'url': f'https://www.facebook.com/{page}/videos/{vid}', 'format': 'VIDEO'}
    if len(imgs) == 1:
        r = _photo(token, page, imgs[0], message=text)
        pid = r.get('post_id') or r.get('id')
        return {'post_id': pid, 'url': f'https://www.facebook.com/{pid}', 'format': 'PHOTO'}
    params = {'message': text, 'access_token': token}
    for i, p in enumerate(imgs):
        params[f'attached_media[{i}]'] = json.dumps({'media_fbid': _photo(token, page, p, published=False)['id']})
    r = _http('POST', f'{API}/{page}/feed', params)
    return {'post_id': r['id'], 'url': f"https://www.facebook.com/{r['id']}", 'format': 'POST', 'files': len(imgs)}
