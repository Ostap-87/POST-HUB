# Шаблоны Aura Robotics

Код шаблонов живёт в `Ostap-87/VIDEO-HUB` (Remotion, `reels-studio/`) — здесь примеры и описание, чтобы любой агент
понимал, из чего собирать.

| Шаблон | Где код | Пример здесь |
|---|---|---|
| **Карусель Instagram** 1080×1350 (4:5), `"brand": "aura"`: пергамент с сеткой, Inter, лимонный маркер под акцентом, монограмма AR, 3D-робот на обложке и последнем слайде, печать AR на последнем слайде | композиция `Carousel` (`src/compositions/Carousel.tsx`) | `carousel-example.json` (данные), `carousel-example.jpg` (лист слайдов) |
| **Ролик «говорящая голова»** с темой Aura | композиция `TalkReelPro`, `"brand": "aura"` | см. `../../VIDEO.md` |
| **Финальный кадр ролика** — как первый экран сайта: тёплый фон с сеткой, лимонное свечение, заголовок с маркером, чёрная кнопка-«пилюля» `aura-robotics.ru`, телефон с главной и каталогом гуманоидов | `TalkReelPro` | — |
| **Обложка статьи блога** | Higgsfield + `cover`, `coverCaption_ru`, `coverCaption_en` | см. `../BRAND.md` |
| **Картинка к посту** с бейджем логотипа компании (снизу слева) | Higgsfield + наложение бейджа (паттерн из claude-control) | — |

## Как сделать карусель

1. В VIDEO-HUB: скопировать `reels-studio/props/carousels/пример-aura.json` в `props/carousels/ГГГГ-ММ-ДД-тема.json`.
2. Заменить тексты. Типы слайдов: `cover`, `text`, `list` (галочки), `steps` (номера), `stat` (крупная цифра), `photo`,
   `quote`, `compare` («обычно / с нами»), `logos`, `cta`. `**слово**` — акцент. Робот: `mascot`.
3. `npm run carousel -- ГГГГ-ММ-ДД-тема` → `finished-videos/карусели/<имя>/01.png…` и лист `_лист.jpg` — показать пользователю.
4. Готовые слайды — в POST-HUB: `AURA/INSTAGRAM/CAROUSEL/PHOTO/` (запас) или сразу в `READY/<дата>_<время>_<тема>/01.png…`.
