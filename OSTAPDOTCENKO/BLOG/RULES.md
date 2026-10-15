# OSTAPDOTCENKO · BLOG — Блог сайта

## Канал
https://ostapdotcenko.ru — статьи в `Ostap-87/ostapdotcenko`, `blog.articles[]` в `src/i18n/ru.ts`, `en.ts`, `zh.ts`. [OD]

## Особенности сети
- Полная статья и обложка. Посты в соцсетях опираются на статьи блога и ссылаются на них.

## Время публикаций
15:00 по Москве, в день из даты статьи [П] — решение пользователя 10.10.2026.

## Подключение
[коннектор добавим позже]

## Правила проекта для этой сети
- Три языка синхронно: RU основной, EN (уходит в LinkedIn — важен `excerpt`), ZH — сжатый стиль. Новая статья — в конец массива. [OD]
- Поля: `category` (tech | life | reflection), `slug` (латиница, kebab-case), `date`, `tag` (серия), `time` (время чтения), `title`, `excerpt`, `body`. [OD]
- Обложка = первая картинка в тексте = og:image = картинка поста в Facebook и LinkedIn; ставится перед первым `##`. [OD]
- Картинки: JPG 82–85, длинная сторона 1600 px, до 500 КБ; графики — PNG до 1400 px, до 200 КБ; имена латиницей; языковые версии `-ru/-en/-zh`. [OD]
- Прежняя публикация (до 14.10.2026): очередь `claude-control/data/ostap-queue/` → коммит → сервер собирает сайт каждые 2 минуты → автопост в Facebook и LinkedIn. [OD]
- С 15.10.2026 статьи идут из пула `READY/` (решение пользователя: «с сегодняшнего дня начнем использовать пул статей»):
  по одной в день в 15:00 МСК, 70 статей — с 15.10 по 23.12.2026. Публикует `CONTROL/TOOLS/blog_od.py`
  (`--queue` очередь, `--post <папка> --dry-run` проверка, `--post <папка>` публикация, `--due` — всё, чьё время наступило,
  со стоп-краном `CONTROL/PUBLISHING.yaml`): статья в конец `blog.articles[]` трёх языков сайта + обложка
  `public/img/<slug>-cover.jpg` → пуш в `main` `Ostap-87/ostapdotcenko` → сервер собирает сайт за 2 минуты и **сам постит
  статью в Facebook (RU) и LinkedIn (EN)**. Вышедшая статья — `PUBLISHED/ГГГГ-ММ/<папка>/` + `info.json` со ссылкой. [П]

Общие правила проекта — `../RULES.md`.

> Источники: [ЕП] — `claude-control/data/editorial-policy.md`; [AURA-CP] — `AURA/CONTENT-PUBLISHING.md`; [SINOTECH] — `SINOTECH/CLAUDE.md`; [OD] — документы `Ostap-87/ostapdotcenko` (PULT.md, PROTOCOL_ARTICLES.md); [FB] — `claude-control/data/fb-config/webhooks.json`; [П] — решение пользователя в POST-HUB.
