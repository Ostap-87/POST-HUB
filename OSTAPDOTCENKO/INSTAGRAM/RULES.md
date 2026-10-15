# OSTAPDOTCENKO · INSTAGRAM — Instagram

## Канал
@ostap.dotsenko — https://www.instagram.com/ostap.dotsenko/ [П, 10.10.2026]. Очередь MyFirst `content/instagram/personal/` — пустая.

## Особенности сети
- Подпись — до 2200 символов и до 30 хештегов; ссылки в подписи не кликабельны.
- Фото в ленту — 4:5 (1080×1350), Reels — вертикальные 9:16.

## Форматы
У каждого формата своя очередь: внутри формата папки TEXT, PHOTO, VIDEO, READY, PUBLISHED.

- `POST/` — одно фото или одно видео в ленту; фото 4:5 (1080×1350), подпись до 2200 символов
- `CAROUSEL/` — пост из нескольких фото или видео (слайды), подпись до 2200 символов
- `REELS/` — вертикальное видео 9:16 с подписью
- `STORIES/` — фото или видео 9:16, исчезают через 24 часа; текст — на самом изображении

## Время публикаций
[настроим позже]

## Подключение
Публикатор POST-HUB (`CONTROL/TOOLS/net_instagram.py`, Actions «Публикация»): приложение Meta «POST-HUB Publisher», Instagram API со входом через Instagram, аккаунт @ostap.dotsenko (BUSINESS) — тестировщик приложения. Секреты GitHub `IG_TOKEN_OSTAPDOTCENKO` и `IG_USER_OSTAPDOTCENKO` добавил пользователь 15.10.2026, проверка `mode=check` — доступ есть [П].
Токен живёт 60 дней — продлить до 13.12.2026 (как у GTT и Aura).

## Stories серией
Несколько Stories подряд выкладываются **в прямом порядке**: первой — часть 01, последней — последняя. Instagram показывает Stories от ранней к поздней, зритель начинает с 01 [П, 15.10.2026]. Публикатор выкладывает файлы из `video_hub` строго по списку; длинную серию делим на посты по 5–6 Stories и запускаем друг за другом. Файл Stories — до 100 МБ и до 60 с.

## Правила проекта для этой сети
Общие правила проекта — `../RULES.md`.

> Источники: [ЕП] — `claude-control/data/editorial-policy.md`; [AURA-CP] — `AURA/CONTENT-PUBLISHING.md`; [SINOTECH] — `SINOTECH/CLAUDE.md`; [OD] — документы `Ostap-87/ostapdotcenko` (PULT.md, PROTOCOL_ARTICLES.md); [FB] — `claude-control/data/fb-config/webhooks.json`; [П] — решение пользователя в POST-HUB.
