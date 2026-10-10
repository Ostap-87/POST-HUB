# GTT · BLOG — Блог сайта

## Канал
https://globaltechtour.ru/blog — статьи в `Ostap-87/SINOTECH`, массив `blog[]` в `src/data/site_content.example.json`.

## Особенности сети
- Полная статья и обложка. Посты в соцсетях опираются на статьи блога и ссылаются на них.

## Время публикаций
[настроим позже]

## Подключение
[коннектор добавим позже]

## Правила проекта для этой сети
- Объём 600–1000 слов, 3–6 подзаголовков `## …`; ru и en; дата — фактическая, не в будущем. [ЕП]
- Обложка `cover` (не плейсхолдер): `.webp` для сайта и `.png` для постов в `public/covers/<slug>`. [ЕП]
- 1–3 внутренние ссылки: `/expeditions/<tour_id>`, `/companies/<id>`, `/expeditions` — только реальные id. [ЕП]
- Действующая публикация: объект в `blog[]` → пуш **в обе ветки** SINOTECH (`main` и `claude/sinotech-voyage-setup` — деплой запускает вторая); перед пушем только `npx tsc -b && npx vite build`. [ЕП]

Общие правила проекта — `../RULES.md`.

> Источники: [ЕП] — `claude-control/data/editorial-policy.md`; [AURA-CP] — `AURA/CONTENT-PUBLISHING.md`; [SINOTECH] — `SINOTECH/CLAUDE.md`; [OD] — документы `Ostap-87/ostapdotcenko` (PULT.md, PROTOCOL_ARTICLES.md); [FB] — `claude-control/data/fb-config/webhooks.json`; [П] — решение пользователя в POST-HUB.
