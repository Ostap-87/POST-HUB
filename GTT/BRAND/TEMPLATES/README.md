# Шаблоны GlobalTechTour

Код шаблонов — в `Ostap-87/VIDEO-HUB`; здесь примеры и описание.

| Шаблон | Где код | Пример здесь |
|---|---|---|
| **Карусель Instagram** 1080×1350, `"brand": "gtt"`: тёмно-синий фон со свечением и сеткой точек, Unbounded, синий акцент, пирамида GLOBAL TECH TOUR | `reels-studio`, композиция `Carousel` | `carousel-example.json`, `carousel-example.jpg` |
| **Stories-анонс карусели** 1080×1920: обложка карусели стопкой со следующими слайдами, «Новый пост», заголовок, плашка-подсказка | `reels-studio`, композиция `StoryAnnounce` | `story-announce-example.jpg` |
| **Ролик «говорящая голова»** | `TalkReelPro` (по умолчанию для говорящих голов) | см. `../../VIDEO.md` |
| **Ролики-слайды** «светлый framed»: разбор, топ-список, репортаж с производства, факт или цитата | `Reel`, `TextReel` | см. `../../VIDEO.md` |
| **Презентация** 1920×1080 → PDF | `VIDEO-HUB/презентации/шаблон/` (`build.py`, JSON-контент) | `presentation-example.jpg` |
| **Картинка к посту** с бейджем логотипа компании | Higgsfield + наложение бейджа | — |

## Как сделать карусель

В VIDEO-HUB: скопировать `reels-studio/props/carousels/пример-gtt.json` → `props/carousels/ГГГГ-ММ-ДД-тема.json`, заменить тексты,
`npm run carousel -- ГГГГ-ММ-ДД-тема` → слайды `finished-videos/карусели/<имя>/01.png…` и лист `_лист.jpg` (показать пользователю).
Готовые слайды — в POST-HUB: `GTT/INSTAGRAM/CAROUSEL/PHOTO/` или сразу в `READY/<дата>_<время>_<тема>/`.

## Как сделать Stories-анонс карусели

В VIDEO-HUB: `reels-studio/props/announces/<имя>.json` (`{"brand": "gtt", "stories": [{"cover", "back", "title", "note"}]}`,
пример — `пример-gtt.json`), `npm run announce -- <имя>` → `finished-videos/анонсы/<имя>/01.png…`, лист `_лист.jpg`;
`--guides` — проверка безопасной зоны Stories (250 px сверху, 380 px снизу). В POST-HUB — `GTT/INSTAGRAM/STORIES/PHOTO/<дата>_<время>_anons-<тема>/01.jpg`.

## Как сделать презентацию

`python3 VIDEO-HUB/презентации/шаблон/build.py VIDEO-HUB/презентации/контент/ГГГГ-ММ-ДД-тема.json` — формат JSON и типы слайдов
в `VIDEO-HUB/презентации/README.md`. Тур с сайта собирается автоматически: `from_site.py <tour_id> --build`.
