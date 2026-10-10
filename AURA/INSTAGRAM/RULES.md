# AURA · INSTAGRAM — Instagram

## Канал
@aura_robotics_ru — https://www.instagram.com/aura_robotics_ru/ [П, 10.10.2026]. Сейчас очередь — `Ostap-87/MyFirst/content/instagram/aura/` (GitHub Actions, секреты `IG_TOKEN_AURA`, `IG_USER_AURA`); публикаций пока не было.

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
[настроим позже] — пока расписания нет, карусели лежат в запасе как `<NN>_<тема>` (номер в сценарии пользователя).

## Подключение
[коннектор добавим позже]

## Правила проекта для этой сети
- Карусели — шаблон `Carousel` с `"brand": "aura"` (`../BRAND/TEMPLATES/README.md`).
- Карусели по сценариям пользователя (`CONTROL/SOURCES/2026-10-10_карусели-instagram/`): фото Higgsfield на каждом слайде,
  не дороже 0,5 кредита за фото; подпись «Иллюстрация» на фото не ставим нигде [П, 10.10.2026].
- Финальный слайд: «Пиши в личные сообщения или оставляй заявку на сайте» + «Рассчитаем стоимость и окупаемость»,
  кнопка — aura-robotics.ru [П, 10.10.2026].
- Reels и Stories — по `../VIDEO.md` и `CONTROL/VIDEO-RULES.md`.

Общие правила проекта — `../RULES.md`.

> Источники: [ЕП] — `claude-control/data/editorial-policy.md`; [AURA-CP] — `AURA/CONTENT-PUBLISHING.md`; [SINOTECH] — `SINOTECH/CLAUDE.md`; [OD] — документы `Ostap-87/ostapdotcenko` (PULT.md, PROTOCOL_ARTICLES.md); [FB] — `claude-control/data/fb-config/webhooks.json`; [П] — решение пользователя в POST-HUB.
