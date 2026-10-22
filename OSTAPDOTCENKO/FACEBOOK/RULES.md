# OSTAPDOTCENKO · FACEBOOK — Страница Facebook

## Канал
Личная страница (page id 1209545262252175). Make, сценарий `FB-LINKEDIN-OSTAPDOTCENKO`. [FB]

## Особенности сети
- Длинные тексты допустимы. Подключение — через Make (вебхук).
- Картинка поста (с 22.10.2026) — обложка статьи из `OSTAPDOTCENKO/BLOG/PUBLISHED/…/photo.jpg` по ссылке GitHub (POST-HUB
  публичный), а не с ostapdotcenko.ru: оттуда Facebook картинки больше не скачивает (ошибка 324 в Make). Ссылки — в
  `scripts/social-images.json` сайта, их пишет `blog_od.py`.

## Форматы
У каждого формата своя очередь: внутри формата папки TEXT, PHOTO, VIDEO, READY, PUBLISHED.

- `POST/` — фото, видео или текст; несколько фото в одном посте — тоже сюда
- `REELS/` — вертикальное видео 9:16
- `STORIES/` — фото или видео 9:16, исчезают через 24 часа

## Время публикаций
[настроим позже]

## Подключение
[коннектор добавим позже]

## Правила проекта для этой сети
- **Повторяет статью блога** — утверждённое исключение из правила уникальности [П, 10.10.2026]: после новой статьи сервер сам отправляет русский заголовок, примерно половину текста и все картинки статьи (галерея). Отдельные посты сюда не пишем. [FB]

Общие правила проекта — `../RULES.md`.

> Источники: [ЕП] — `claude-control/data/editorial-policy.md`; [AURA-CP] — `AURA/CONTENT-PUBLISHING.md`; [SINOTECH] — `SINOTECH/CLAUDE.md`; [OD] — документы `Ostap-87/ostapdotcenko` (PULT.md, PROTOCOL_ARTICLES.md); [FB] — `claude-control/data/fb-config/webhooks.json`; [П] — решение пользователя в POST-HUB.
