# GTT · BLOG — Блог сайта

## Канал
https://globaltechtour.ru/blog — статьи в `Ostap-87/SINOTECH`, массив `blog[]` в `src/data/site_content.example.json`.

## Особенности сети
- Полная статья и обложка. Посты в соцсетях опираются на статьи блога и ссылаются на них.

## Время публикаций
15:00 по Москве, в день из даты статьи [П] — решение пользователя 10.10.2026.

## Подключение
С 07.11.2026 — автоматически, без агента [П, 07.11.2026: «сделай так, чтобы статьи самостоятельно выходили без твоего участия»].
- Очередь — `GTT/BLOG/READY/<дата>_1500_<slug>/` (`post.ru.md`, `post.en.md`, `photo.jpg`), по статье в день; даты подряд — `python3 CONTROL/TOOLS/blog_site.py --project GTT --redate <дата>`, очередь — `--queue`.
- Публикует workflow «Блог из POST-HUB» репозитория `Ostap-87/SINOTECH` (`.github/workflows/blog-from-post-hub.yml`): несколько раз в день берёт этот публичный репозиторий, запускает `blog_site.py --project GTT --due` и пушит статью и обложку (`public/covers/<slug>.jpg`) в ветку `claude/sinotech-voyage-setup` — вебхук сервера пересобирает сайт. Одна статья вне очереди — Actions → «Блог из POST-HUB» → Run workflow → папка.
- Учёт — workflow POST-HUB «Блоги сайтов — учёт» (`blog-sites.yml`): вышедшие статьи уезжают в `PUBLISHED/ГГГГ-ММ/` с `info.json`.
- Стоп-кран — `CONTROL/PUBLISHING.yaml` (`GTT/BLOG` в `pause_except`).
- До 02–04.11.2026 статьи выкладывал сервер (claude-control, `/opt/publishers/publish-*-article.py`) из своей пачки — она закончилась.

## Правила проекта для этой сети
- **Объём статьи и число подзаголовков — на усмотрение автора**: блог — площадка пользователя, здесь его правила [П, 10.10.2026]. (Прежняя норма редполитики «600–1000 слов, 3–6 подзаголовков» для блога не действует.)
- Подзаголовки `## …`; ru и en; дата — фактическая, не в будущем. [ЕП]
- Список источников в конце статьи — как у автора, **с адресами** [П, 10.10.2026]. Внутри текста внешний источник — названием, без гиперссылки. [ЕП]
- Обложка `cover` (не плейсхолдер): `.webp` для сайта и `.png` для постов в `public/covers/<slug>`. [ЕП]
- 1–3 внутренние ссылки: `/expeditions/<tour_id>`, `/companies/<id>`, `/expeditions` — только реальные id; анкор из слов самой статьи, новых слов не добавляем. [ЕП, П 10.10.2026]
- Действующая публикация: объект в `blog[]` → пуш **в обе ветки** SINOTECH (`main` и `claude/sinotech-voyage-setup` — деплой запускает вторая); перед пушем только `npx tsc -b && npx vite build`. [ЕП]

Общие правила проекта — `../RULES.md`.

> Источники: [ЕП] — `claude-control/data/editorial-policy.md`; [AURA-CP] — `AURA/CONTENT-PUBLISHING.md`; [SINOTECH] — `SINOTECH/CLAUDE.md`; [OD] — документы `Ostap-87/ostapdotcenko` (PULT.md, PROTOCOL_ARTICLES.md); [FB] — `claude-control/data/fb-config/webhooks.json`; [П] — решение пользователя в POST-HUB.
