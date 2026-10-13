"""Адаптер Telegram для `publish.py`: Bot API, бот — администратор канала проекта.

Переключено на POST-HUB по решению пользователя 13.10.2026 («давай начнем по шагам» — перенос всех публикаций в один
репозиторий). Очередь POST-HUB начинается 01.11.2026; до 30.10 каналы ведёт старая очередь claude-control — даты не
пересекаются, двойных постов нет.
Доступ — секрет GitHub `TG_BOT_TOKEN_<ПРОЕКТ>` (ключ бота из @BotFather; бот — администратор канала). Канал — `CHATS`.
Пост — `<ПРОЕКТ>/TELEGRAM/READY/<ГГГГ-ММ-ДД_ЧЧММ_тема>/post.md` + файл картинки (`image` в шапке, лежит в папке поста):
одно сообщение — фото с подписью до 1024 знаков (правило проектов — до 1000), без картинки — текст до 4096,
`video` в шапке — видео с подписью. Markdown поста (**жирный**, *курсив*, [текст](ссылка)) переводится в HTML Telegram.
Проверка без публикации в канал — `publish.py --test TELEGRAM`: первый пост очереди уходит в личку тому, кто последним
нажал «Старт» у бота.
"""
import html
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
import uuid

API = 'https://api.telegram.org/bot{token}/{method}'
CHATS = {'AURA': '@aura_robots', 'GTT': '-1003942618148'}          # те же каналы, что у claude-control
CAPTION_MAX, TEXT_MAX = 1024, 4096


class TGError(Exception):
    pass


class NotConnected(Exception):
    pass


def _call(token, method, params=None, files=None, timeout=120):
    """Запрос к Bot API; files = {'photo': (имя, байты, тип)} — тогда multipart."""
    params = {k: v for k, v in (params or {}).items() if v is not None}
    url = API.format(token=token, method=method)
    if files:
        boundary = uuid.uuid4().hex
        parts = []
        for k, v in params.items():
            parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
        for k, (name, data, ctype) in files.items():
            parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"; filename="{name}"\r\n'
                         f'Content-Type: {ctype}\r\n\r\n'.encode() + data + b'\r\n')
        body = b''.join(parts) + f'--{boundary}--\r\n'.encode()
        req = urllib.request.Request(url, data=body, headers={'Content-Type': f'multipart/form-data; boundary={boundary}'})
    else:
        req = urllib.request.Request(url, data=urllib.parse.urlencode(params).encode())
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            res = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try:
            res = json.loads(e.read().decode())
        except Exception:
            raise TGError(f'{method}: HTTP {e.code}') from None
    if not res.get('ok'):
        raise TGError(f"{method}: {res.get('description', res)}")
    return res['result']


def to_html(md):
    """Markdown поста → HTML Telegram: экранирование, ссылки, **жирный**, *курсив*."""
    s = html.escape(md.strip(), quote=False)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', lambda m: f'<a href="{m.group(2).replace(chr(34), "%22")}">{m.group(1)}</a>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![*\w])\*(?![\s*])(.+?)(?<![\s*])\*(?![*\w])', r'<i>\1</i>', s)
    return s


def visible_len(h):
    """Длина текста так, как её считает Telegram (без тегов, с раскрытыми &amp; и т.п.)."""
    return len(html.unescape(re.sub(r'<[^>]+>', '', h)))


def creds(project):
    token = os.environ.get(f'TG_BOT_TOKEN_{project}')
    return (token, CHATS.get(project)) if token else (None, None)


def check(project):
    if not os.environ.get(f'TG_BOT_TOKEN_{project}'):
        return None, f'нет секрета TG_BOT_TOKEN_{project} — не подключено'
    token, chat = creds(project)
    if not chat:
        return False, f'для {project} не задан канал (CHATS в net_telegram.py)'
    try:
        me = _call(token, 'getMe')
        info = _call(token, 'getChat', {'chat_id': chat})
        member = _call(token, 'getChatMember', {'chat_id': chat, 'user_id': me['id']})
    except TGError as e:
        return False, f'ошибка доступа: {e}'
    can_post = member.get('status') == 'creator' or (member.get('status') == 'administrator' and member.get('can_post_messages', True))
    where = f"«{info.get('title')}»" + (f" (@{info['username']})" if info.get('username') else '')
    if not can_post:
        return False, f"бот @{me.get('username')} в канале {where} не может публиковать (статус {member.get('status')})"
    return True, f"доступ есть: бот @{me.get('username')} публикует в канал {where}"


def _media(d, meta):
    """(метод, поле, путь к файлу) или None — картинка или видео из шапки поста."""
    for key, method, field in (('video', 'sendVideo', 'video'), ('image', 'sendPhoto', 'photo')):
        name = meta.get(key)
        if name:
            p = d / name
            if not p.exists():
                raise TGError(f'нет файла {name} в папке поста')
            return method, field, p
    return None


def _send(token, chat, text, media):
    if media:
        method, field, p = media
        ctype = 'video/mp4' if field == 'video' else 'image/png' if p.suffix.lower() == '.png' else 'image/jpeg'
        return _call(token, method, {'chat_id': chat, 'caption': text, 'parse_mode': 'HTML'},
                     files={field: (p.name, p.read_bytes(), ctype)}, timeout=600 if field == 'video' else 120)
    return _call(token, 'sendMessage', {'chat_id': chat, 'text': text, 'parse_mode': 'HTML'})


def _validate(d, meta, body):
    text = to_html(body)
    media = _media(d, meta)
    limit = CAPTION_MAX if media else TEXT_MAX
    n = visible_len(text)
    if n > limit:
        raise TGError(f'текст {n} знаков — больше лимита Telegram {limit} для {"подписи" if media else "сообщения"}')
    return text, media, n


def publish(project, fmt, d, meta, body, dry=False):
    text, media, n = _validate(d, meta, body)
    plan = f"{'фото' if media and media[1] == 'photo' else 'видео' if media else 'текст'} + текст {n} знаков → {CHATS.get(project)}"
    if dry:
        return {'plan': plan}
    token, chat = creds(project)
    if not token:
        raise NotConnected(f'Telegram {project} не подключён (нет секрета TG_BOT_TOKEN_{project})')
    msg = _send(token, chat, text, media)
    ch = msg.get('chat', {})
    if ch.get('username'):
        url = f"https://t.me/{ch['username']}/{msg['message_id']}"
    else:
        url = f"https://t.me/c/{str(ch.get('id', chat)).removeprefix('-100')}/{msg['message_id']}"
    return {'post_id': msg['message_id'], 'url': url, 'format': 'TELEGRAM', 'chat': chat}


def test(project, d, meta, body):
    """Пробный пост в личку (не в канал): тому, кто последним написал боту (нажал «Старт»)."""
    token, _ = creds(project)
    if not token:
        return None, f'нет секрета TG_BOT_TOKEN_{project} — не подключено'
    text, media, n = _validate(d, meta, body)
    try:
        ups = _call(token, 'getUpdates', {'limit': 100, 'allowed_updates': json.dumps(['message'])})
    except TGError as e:
        return False, f'не прочитать сообщения бота ({e}) — нажмите «Старт» у бота и повторите'
    chats = [u['message']['chat'] for u in ups if u.get('message', {}).get('chat', {}).get('type') == 'private']
    if not chats:
        return False, 'боту никто не писал — откройте бота в Telegram, нажмите «Старт» и повторите'
    me = _call(token, 'getMe')
    head = f'🧪 ТЕСТ POST-HUB — так выйдет пост {d.name} в {CHATS.get(project)}. В канал ничего не ушло.\n\n'
    room = (CAPTION_MAX if media else TEXT_MAX) - n
    _send(token, chats[-1]['id'], (html.escape(head) if len(head) <= room else '') + text, media)
    return True, f"пробный пост от @{me.get('username')} отправлен в личку ({chats[-1].get('first_name', '')})"
