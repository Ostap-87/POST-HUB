# Шаблоны GlobalTechTour

Код шаблонов — в `Ostap-87/VIDEO-HUB`; здесь примеры и описание.

| Шаблон | Где код | Пример здесь |
|---|---|---|
| **Карусель Instagram** 1080×1350, `"brand": "gtt"`: тёмно-синий фон со свечением и сеткой точек, Unbounded, синий акцент, пирамида GLOBAL TECH TOUR | `reels-studio`, композиция `Carousel` | `carousel-example.json`, `carousel-example.jpg` |
| **Ролик «говорящая голова»** | `TalkReelPro` (по умолчанию для говорящих голов) | см. `../../VIDEO.md` |
| **Ролики-слайды** «светлый framed»: разбор, топ-список, репортаж с производства, факт или цитата | `Reel`, `TextReel` | см. `../../VIDEO.md` |
| **Презентация** 1920×1080 → PDF | `VIDEO-HUB/презентации/шаблон/` (`build.py`, JSON-контент) | `presentation-example.jpg` |
| **Картинка к посту** с бейджем логотипа компании | Higgsfield + наложение бейджа | — |

## Как сделать карусель

В VIDEO-HUB: скопировать `reels-studio/props/carousels/пример-gtt.json` → `props/carousels/ГГГГ-ММ-ДД-тема.json`, заменить тексты,
`npm run carousel -- ГГГГ-ММ-ДД-тема` → слайды `finished-videos/карусели/<имя>/01.png…` и лист `_лист.jpg` (показать пользователю).
Готовые слайды — в POST-HUB: `GTT/INSTAGRAM/CAROUSEL/PHOTO/` или сразу в `READY/<дата>_<время>_<тема>/`.

## Как сделать презентацию

`python3 VIDEO-HUB/презентации/шаблон/build.py VIDEO-HUB/презентации/контент/ГГГГ-ММ-ДД-тема.json` — формат JSON и типы слайдов
в `VIDEO-HUB/презентации/README.md`. Тур с сайта собирается автоматически: `from_site.py <tour_id> --build`.
