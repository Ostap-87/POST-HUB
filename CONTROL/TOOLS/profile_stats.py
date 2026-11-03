"""Сводка по профилю Instagram для разбора оформления и контента (только чтение).

python3 CONTROL/TOOLS/profile_stats.py OSTAPDOTCENKO [--limit 150]
Печатает публичные данные: описание, число подписчиков/публикаций, последние посты (тип, дата, лайки, комментарии,
просмотры Reels — их видно и в сетке профиля), первая строка подписи, ссылка на картинку-превью и на файл ролика (для чистых кадров обложек),
фото и видео внутри каруселей (CHILD) и живые сторис (STORY, только последние 24 часа — архив и хайлайты API не отдаёт).
Закрытые метрики (охват, сохранения, переходы) не печатаем: лог Actions в публичном репозитории виден всем.
Секреты — те же, что у публикатора: IG_TOKEN_<ПРОЕКТ>, IG_USER_<ПРОЕКТ>.
"""
import json
import os
import sys
import urllib.parse
import urllib.request

API = 'https://graph.instagram.com/' + os.environ.get('IG_API_VERSION', 'v25.0')
project = sys.argv[1] if len(sys.argv) > 1 else 'OSTAPDOTCENKO'
limit = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else 150
token = os.environ[f'IG_TOKEN_{project}']
user = os.environ.get(f'IG_USER_{project}') or 'me'


def get(path, **params):
    params['access_token'] = token
    url = path if path.startswith('http') else f'{API}/{path}?' + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


me = get(user, fields='username,name,biography,website,followers_count,follows_count,media_count')
print('PROFILE', json.dumps({k: me.get(k) for k in ('username', 'name', 'biography', 'website', 'followers_count', 'follows_count', 'media_count')}, ensure_ascii=False))
fields = 'id,caption,media_type,media_product_type,timestamp,like_count,comments_count,permalink,thumbnail_url,media_url'
page, posts = get(f'{user}/media', fields=fields, limit=50), []
while page and len(posts) < limit:
    posts += page.get('data', [])
    nxt = page.get('paging', {}).get('next')
    page = get(nxt) if nxt and len(posts) < limit else None
for p in posts[:limit]:
    views = None
    if p.get('media_product_type') == 'REELS':
        try:
            ins = get(f"{p['id']}/insights", metric='views')
            views = (ins.get('data') or [{}])[0].get('values', [{}])[0].get('value')
        except Exception:
            views = None
    cap = (p.get('caption') or '').strip().split('\n')[0][:140]
    thumb = p.get('thumbnail_url') or (p.get('media_url') if p.get('media_type') != 'VIDEO' else '')
    print('POST', json.dumps({'t': p.get('timestamp', '')[:16], 'type': p.get('media_product_type') or p.get('media_type'),
                              'kind': p.get('media_type'), 'likes': p.get('like_count'), 'comments': p.get('comments_count'),
                              'views': views, 'cap': cap, 'link': p.get('permalink'), 'thumb': thumb,
                              # ссылка на сам ролик (публичный файл поста) — чистые кадры для новых обложек
                              'video': p.get('media_url') if p.get('media_type') == 'VIDEO' else None}, ensure_ascii=False))
    # фото и видео внутри карусели — для роликов-нарезок из публикаций (03.11.2026: «взять все моменты, что я выкладывал»)
    if p.get('media_type') == 'CAROUSEL_ALBUM':
        try:
            kids = get(f"{p['id']}/children", fields='id,media_type,media_url,thumbnail_url').get('data', [])
        except Exception:
            kids = []
        for k in kids:
            print('CHILD', json.dumps({'t': p.get('timestamp', '')[:16], 'link': p.get('permalink'), 'kind': k.get('media_type'),
                                       'url': k.get('media_url'), 'thumb': k.get('thumbnail_url')}, ensure_ascii=False))
print('TOTAL', len(posts[:limit]))
# сторис, которые сейчас висят (API отдаёт только живые 24 часа; архив и хайлайты — нет)
try:
    for s_ in get(f'{user}/stories', fields='id,media_type,media_url,thumbnail_url,timestamp,permalink').get('data', []):
        print('STORY', json.dumps({'t': s_.get('timestamp', '')[:16], 'kind': s_.get('media_type'), 'url': s_.get('media_url'),
                                   'thumb': s_.get('thumbnail_url')}, ensure_ascii=False))
except Exception as e:
    print('STORY_ERR', str(e)[:120])
