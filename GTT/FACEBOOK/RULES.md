# GTT · FACEBOOK — Страница Facebook

## Канал
Страница Global Tech Tour (page id 1254540414416697). Make, сценарий `FB-POST-AURA-GTT`, `project: "globaltechtour"`. [FB]

## Особенности сети
- Длинные тексты допустимы. Подключение — через Make (вебхук).

## Форматы
У каждого формата своя очередь: внутри формата папки TEXT, PHOTO, VIDEO, READY, PUBLISHED.

- `POST/` — фото, видео или текст; несколько фото в одном посте — тоже сюда
- `REELS/` — вертикальное видео 9:16
- `STORIES/` — фото или видео 9:16, исчезают через 24 часа

## Время публикаций
12:00 по Москве, вторник и пятница (по плану в шапке поста) [П] — решение пользователя 10.10.2026.

**Дубль Instagram** (решение пользователя 12.10.2026: «чтобы и в инсте и в фб публикации делались»): утверждённые посты Instagram проекта переносятся в очередь командой `to_ready.py <ПРОЕКТ>/INSTAGRAM/<ФОРМАТ> --facebook` — копия сразу ложится в `FACEBOOK/REELS|STORIES|POST/READY/` с тем же именем и выходит в то же время (карусель — пост со всеми слайдами). Собственные посты Facebook (серия по 25 постов, вт и пт 12:00) идут как раньше.

## Подключение
**Публикатор POST-HUB** (`CONTROL/TOOLS/net_facebook.py`, решение пользователя 12.10.2026: «мы же можем публиковать эти ролики
в аккаунтах Фейсбук — Аура и Глобалтех тур?»): посты из `FACEBOOK/<ФОРМАТ>/READY/` выходят по времени из имени папки, как Instagram
(`publish.yml`, стоп-кран `CONTROL/PUBLISHING.yaml`). Форматы: POST (текст, фото, несколько фото, видео), REELS (`video_hub`),
STORIES. Картинки загружаются из папки поста напрямую, видео — по публичной ссылке Git LFS VIDEO-HUB.
Доступ — секрет `FB_PAGE_TOKEN_GTT` (токен страницы). Токен получает пользователь, в чат и в файлы он не попадает:
0. На facebook.com у пользователя полный контроль над страницей (Страница → Настройки → Доступ к Странице).
1. developers.facebook.com → Мои приложения → POST-HUB Publisher → Сценарии использования → Добавить сценарий →
   «Управлять всем на вашей Странице» → Настроить → разрешения `pages_show_list`, `pages_read_engagement`, `pages_manage_posts`.
   (Если сценарий не добавляется — новое приложение типа «Бизнес» с этим сценарием.)
2. developers.facebook.com/tools/explorer → приложение → «Получить маркер доступа пользователя» → те же три разрешения →
   Generate Access Token → в окне входа отметить обе страницы.
3. developers.facebook.com/tools/debug/accesstoken → вставить токен → «Продлить маркер доступа» → длинный токен (60 дней).
4. В Graph API Explorer с длинным токеном: `me/accounts?fields=name,id,access_token` → `access_token` страницы Global Tech Tour
   (id 1254540414416697); в отладчике у него «Срок действия: Никогда».
5. POST-HUB → Settings → Secrets and variables → Actions → New repository secret: `FB_PAGE_TOKEN_GTT`.
Проверить доступ: GitHub → Actions → «Публикация» → Run workflow → режим `check`. Токен страницы бессрочный, но сбрасывается
при смене пароля Facebook или удалении приложения — тогда шаги 2–5 заново. Если посты приложения видны только администраторам
(режим «Разработка»), приложение переводится в режим «Опубликовано» (политика конфиденциальности, иконка, категория).
Make-сценарий `FB-POST-AURA-GTT` (claude-control) POST-HUB не трогает.

## Правила проекта для этой сети
- **Только оригинальный контент**, русский язык, фото-пост. [ЕП]
- Серия «Индустрии Азии» (26 постов, `claude-control/data/globaltechtour-fb-series/`) — уже вышедшие темы не повторять. [ЕП]

Общие правила проекта — `../RULES.md`.

> Источники: [ЕП] — `claude-control/data/editorial-policy.md`; [AURA-CP] — `AURA/CONTENT-PUBLISHING.md`; [SINOTECH] — `SINOTECH/CLAUDE.md`; [OD] — документы `Ostap-87/ostapdotcenko` (PULT.md, PROTOCOL_ARTICLES.md); [FB] — `claude-control/data/fb-config/webhooks.json`; [П] — решение пользователя в POST-HUB.
