// Сборка Word-документа «POST-HUB — архитектура и правила»: node DOCS/исходники/make-docx.js
// Схемы берутся из DOCS/схемы/*.png (сначала node DOCS/исходники/render-schemes.mjs).
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, LevelFormat, PageBreak, Footer, PageNumber,
} = require('docx');

const HERE = __dirname;
const DOCS = path.join(HERE, '..');
const OUT = path.join(DOCS, 'POST-HUB_архитектура-и-правила.docx');
const BLUE = '1A73E8', INK = '1D2030', MUTE = '5E6170', PALE = 'EAF2FE', LINE = 'D7DFEB';
const FONT = 'Arial';
const TEXT_W = 9638; // ширина текста A4 при полях 2 см (DXA)

const p = (text, opts = {}) => new Paragraph({ spacing: { after: 120, line: 300 }, ...opts.para,
  children: runs(text, opts) });
function runs(text, opts = {}) {
  // **жирный** внутри строки
  return String(text).split(/(\*\*[^*]+\*\*)/).filter(Boolean).map((part) => {
    const b = part.startsWith('**') && part.endsWith('**');
    return new TextRun({ text: b ? part.slice(2, -2) : part, bold: b || opts.bold, color: opts.color || INK,
      size: opts.size || 22, font: opts.font || FONT, italics: opts.italics });
  });
}
const h1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 360, after: 160 }, children: [new TextRun({ text: t, font: FONT })] });
const h2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 120 }, children: [new TextRun({ text: t, font: FONT })] });
const bullet = (t, level = 0) => new Paragraph({ numbering: { reference: 'bul', level }, spacing: { after: 60, line: 290 }, children: runs(t) });
const num = (t, ref = 'num') => new Paragraph({ numbering: { reference: ref, level: 0 }, spacing: { after: 60, line: 290 }, children: runs(t) });
const note = (t) => new Paragraph({ spacing: { before: 60, after: 160 }, shading: { type: ShadingType.CLEAR, fill: PALE, color: 'auto' },
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: BLUE, space: 8 } }, indent: { left: 140 }, children: runs(t, { size: 21 }) });
function mono(lines) {
  return lines.split('\n').map((l, i, a) => new Paragraph({ spacing: { after: 0, line: 260 }, shading: { type: ShadingType.CLEAR, fill: 'F4F6F9', color: 'auto' },
    indent: { left: 140 }, children: [new TextRun({ text: l || ' ', font: 'Courier New', size: 18, color: INK })],
    ...(i === a.length - 1 ? { spacing: { after: 160, line: 260 } } : {}) }));
}
function image(file, caption) {
  const buf = fs.readFileSync(path.join(DOCS, 'схемы', file));
  const w = buf.readUInt32BE(16), h = buf.readUInt32BE(20); // размеры PNG из заголовка
  const width = 640, height = Math.round(640 * h / w);
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 60 }, children: [new ImageRun({ type: 'png', data: buf, transformation: { width, height } })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 }, children: runs(caption, { size: 18, color: MUTE, italics: true }) }),
  ];
}
function table(head, rows, widths) {
  const total = widths.reduce((a, b) => a + b, 0);
  const border = { style: BorderStyle.SINGLE, size: 4, color: LINE };
  const borders = { top: border, bottom: border, left: border, right: border };
  const cell = (t, i, isHead) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA }, borders,
    shading: isHead ? { type: ShadingType.CLEAR, fill: PALE, color: 'auto' } : undefined,
    margins: { top: 70, bottom: 70, left: 110, right: 110 },
    children: String(t).split('\n').map((line) => new Paragraph({ spacing: { after: 20, line: 270 }, children: runs(line, { size: 19, bold: isHead, color: isHead ? BLUE : INK }) })),
  });
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: head.map((t, i) => cell(t, i, true)) }),
      ...rows.map((r) => new TableRow({ children: r.map((t, i) => cell(t, i, false)) }))] });
}
const gap = () => new Paragraph({ spacing: { after: 120 }, children: [] });

const content = [
  // --- Титул
  new Paragraph({ spacing: { before: 2400, after: 120 }, children: [new TextRun({ text: 'POST-HUB', font: FONT, size: 72, bold: true, color: BLUE })] }),
  new Paragraph({ spacing: { after: 240 }, children: [new TextRun({ text: 'Архитектура и правила работы', font: FONT, size: 40, bold: true, color: INK })] }),
  p('Контент и публикации трёх проектов — Aura Robotics, GlobalTechTour и ostapdotcenko — во всех соцсетях. Как всё устроено, где что лежит, как работает любой агент и как переключать управление.', { size: 24, color: MUTE }),
  p('Репозиторий: github.com/Ostap-87/POST-HUB · версия от 10 октября 2026', { size: 20, color: MUTE }),
  new Paragraph({ children: [new PageBreak()] }),

  new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: 'Содержание', font: FONT, size: 32, bold: true, color: BLUE })] }),
  ...['1. Что такое POST-HUB', '2. Проекты, сети и форматы', '3. Структура папок', '4. Пять рабочих папок', '5. Путь поста',
    '6. Имена и состав папки поста', '7. Уникальность контента', '8. Правила и их порядок', '9. Пульт CONTROL',
    '10. Кнопка и смена агента', '11. Как работает агент', '12. Публикация', '13. Хранение файлов', '14. Картинки Higgsfield',
    '15. Ключи и доступы', '16. Действующие публикации в других репозиториях', '17. Что дальше']
    .map((t) => new Paragraph({ spacing: { after: 90 }, children: runs(t, { size: 24 }) })),
  new Paragraph({ children: [new PageBreak()] }),

  // --- 1
  h1('1. Что такое POST-HUB'),
  p('POST-HUB — единое место, где лежит весь контент для соцсетей трёх проектов и очередь его публикации. Здесь же — правила для каждого проекта и каждой сети и пульт, через который работает агент (Claude, ChatGPT или другой).'),
  h2('Три принципа'),
  num('**Агент — сменный исполнитель.** Всё важное (контент, очередь, задания, журнал, правила) хранится в репозитории, а не в памяти агента. Поэтому другой агент может продолжить работу с того же места.', 'num1'),
  num('**Публикуют скрипты по расписанию, без агента.** Даже если ни один агент не работает, одобренные посты из очереди выходят вовремя.', 'num1'),
  num('**Контент уникальный.** У каждого проекта и в каждой сети свои тексты и фото, ничего не повторяется.', 'num1'),
  ...image('01-общая-схема.png', 'Схема 1. Как устроен POST-HUB'),

  // --- 2
  h1('2. Проекты, сети и форматы'),
  h2('Три проекта'),
  table(['Папка', 'Проект', 'Сайт и тема'], [
    ['AURA', 'Aura Robotics', 'aura-robotics.ru — роботы и робототехника'],
    ['GTT', 'GlobalTechTour', 'globaltechtour.ru — рынок Китая, бизнес-туры'],
    ['OSTAPDOTCENKO', 'ostapdotcenko', 'личный сайт и каналы владельца'],
  ], [2200, 2400, 5038]),
  gap(),
  p('У каждого проекта уникальный контент и свои каналы в каждой соцсети.'),
  h2('Одиннадцать сетей в каждом проекте'),
  table(['Папка', 'Сеть', 'Форматы (своя очередь у каждого)'], [
    ['TELEGRAM', 'Telegram-канал (один на проект)', '—'],
    ['DZEN', 'Дзен', 'ARTICLE — статьи; POST — короткие посты; LONG — видео; SHORTS — ролики'],
    ['BLOG', 'Блог сайта', '—'],
    ['FACEBOOK', 'Страница Facebook', 'POST — фото, видео, текст, несколько фото; REELS; STORIES'],
    ['LINKEDIN', 'LinkedIn', '—'],
    ['INSTAGRAM', 'Instagram', 'POST — одно фото или видео; CAROUSEL — слайды; REELS; STORIES'],
    ['THREADS', 'Threads', '—'],
    ['X', 'X (Twitter)', '—'],
    ['YOUTUBE', 'YouTube', 'LONG — обычные ролики; SHORTS — вертикальные до 3 минут'],
    ['WECHAT', 'WeChat (официальный аккаунт)', '—'],
    ['XIAOHONGSHU', 'Xiaohongshu (小红书)', '—'],
  ], [1900, 2900, 4838]),
  gap(),
  ...image('02-проект-изнутри.png', 'Схема 2. Проект изнутри'),

  // --- 3
  h1('3. Структура папок'),
  p('Вся структура одинаковая у трёх проектов. Ниже — сокращённый вид на примере AURA.'),
  ...mono(`POST-HUB/
├── CONTROL/                 пульт (раздел 9)
├── AURA/
│   ├── RULES.md             правила проекта
│   ├── TELEGRAM/
│   │   ├── RULES.md         правила сети
│   │   ├── TEXT/  PHOTO/  VIDEO/  READY/  PUBLISHED/
│   ├── DZEN/
│   │   ├── RULES.md
│   │   ├── ARTICLE/  POST/  LONG/  SHORTS/
│   │   │   └── (в каждом) TEXT/ PHOTO/ VIDEO/ READY/ PUBLISHED/
│   ├── BLOG/  LINKEDIN/  THREADS/  X/  WECHAT/  XIAOHONGSHU/
│   │   └── (в каждой) RULES.md + TEXT/ PHOTO/ VIDEO/ READY/ PUBLISHED/
│   ├── FACEBOOK/            POST/ REELS/ STORIES/  (+ RULES.md)
│   ├── INSTAGRAM/           POST/ CAROUSEL/ REELS/ STORIES/  (+ RULES.md)
│   └── YOUTUBE/             LONG/ SHORTS/  (+ RULES.md)
├── GTT/                     то же самое
├── OSTAPDOTCENKO/           то же самое
├── DOCS/                    этот документ, промпт для агента, схемы
├── AGENTS.md, CLAUDE.md     входы для агентов → CONTROL/AGENT.md
└── .github/workflows/       кнопка «Переключить агента» (и позже — публикация)`),

  // --- 4
  h1('4. Пять рабочих папок'),
  p('Внутри каждой сети (а в Instagram, Facebook, YouTube и Дзене — внутри каждого формата) лежат одни и те же пять папок. Поэтому любой агент и любой скрипт работают со всеми сетями одинаково.'),
  table(['Папка', 'Что в ней', 'Пример'], [
    ['TEXT/', 'Запас текстов для этой сети', 'TEXT/2026-11-01_unitree-g1.md'],
    ['PHOTO/', 'Запас фото: сгенерированные (Higgsfield) и присланные владельцем', 'PHOTO/2026-11-01_unitree-g1.jpg'],
    ['VIDEO/', 'Запас видео; хранится через Git LFS', 'VIDEO/2026-11-05_factory-tour.mp4'],
    ['READY/', 'Очередь: готовые посты по дням, папка на пост — текст + фото или видео', 'READY/2026-11-01_0900_unitree-g1/'],
    ['PUBLISHED/', 'Архив вышедшего по месяцам — с датой, временем и ссылкой на пост', 'PUBLISHED/2026-11/2026-11-01_0900_unitree-g1/'],
  ], [1700, 4400, 3538]),

  // --- 5
  h1('5. Путь поста'),
  p('Материал движется в одну сторону: запас → очередь → архив. Файлы не удаляются и не копируются, а переносятся — поэтому всегда понятно, где лежит каждая вещь, и ничего не дублируется.'),
  ...image('03-путь-поста.png', 'Схема 3. Путь поста'),
  num('**Запас.** Тексты, фото и видео кладутся в TEXT, PHOTO и VIDEO нужной сети. Каждый материал уникален для своей сети и проекта.', 'num2'),
  num('**Сборка поста (prepare).** На конкретную дату и время создаётся папка в READY: текст поста + фото или видео. Файлы переносятся из запаса.', 'num2'),
  num('**Проверка (check).** Лимиты сети, наличие ссылки, уникальность — текст и фото не должны повторять другие сети и архив.', 'num2'),
  num('**Публикация (publish).** В назначенное время скрипт публикует пост — без участия агента.', 'num2'),
  num('**Архив (archive).** Вышедший пост переносится в PUBLISHED/ГГГГ-ММ/ и получает файл info.json: когда вышел, ссылка, кто опубликовал.', 'num2'),

  // --- 6
  h1('6. Имена и состав папки поста'),
  h2('Имена'),
  bullet('В запасе: **ГГГГ-ММ-ДД_тема.расширение**, например 2026-11-01_unitree-g1.jpg.'),
  bullet('В READY и PUBLISHED — папка **ГГГГ-ММ-ДД_ЧЧММ_тема**, например 2026-11-01_0900_unitree-g1. Время нужно, если в день больше одного поста.'),
  bullet('Тема — латиницей через дефис. **Одна тема в разных сетях называется одинаково** — так видно, что пост в соцсети и статья блога про одно и то же.'),
  bullet('Имена начинаются с даты, поэтому папка READY, отсортированная по имени, — это и есть расписание.'),
  h2('Что лежит в папке поста'),
  table(['Файл', 'Назначение'], [
    ['post.md', 'Текст поста. У сторис может быть пустым'],
    ['photo.jpg', 'Одно фото'],
    ['01.jpg, 02.jpg, 03.mp4 …', 'Карусель и сторис: медиа по порядку показа'],
    ['video.mp4', 'Видео (Reels, Shorts, ролики)'],
    ['cover.jpg', 'Обложка видео, если нужна (YouTube, Reels)'],
    ['meta.yaml', 'Необязательно: заголовок (YouTube, статья Дзена), ссылка, хештеги, заметки'],
    ['info.json', 'Только в PUBLISHED: дата и время выхода, ссылка, id поста, кто опубликовал'],
  ], [3000, 6638]),
  gap(),
  p('Пример info.json:', { bold: true }),
  ...mono('{"published_at": "2026-11-01T09:00:00+03:00", "url": "https://…", "post_id": "…", "published_by": "script"}'),

  // --- 7
  h1('7. Уникальность контента'),
  bullet('У каждого проекта свой контент: AURA, GTT и OSTAPDOTCENKO не повторяют друг друга.'),
  bullet('Внутри проекта у каждой сети свои тексты и фото: пост в Telegram, Instagram и LinkedIn на одну тему — это три разных текста и три разных изображения.'),
  bullet('Перед тем как положить материал в очередь, его сверяют с READY и PUBLISHED всех сетей — темы, тексты и фото не должны повторять уже вышедшее.'),
  bullet('Эту проверку будет делать команда check автоматически — одинаково для любого агента.'),

  // --- 8
  h1('8. Правила и их порядок'),
  p('Правила лежат на трёх уровнях. Если они расходятся — действует более частное.'),
  ...image('05-порядок-правил.png', 'Схема 4. Порядок правил'),
  table(['Файл', 'Что в нём'], [
    ['<ПРОЕКТ>/<СЕТЬ>/RULES.md', 'Канал (адрес), особенности сети (лимиты), форматы, время публикаций, подключение, правила проекта для этой сети'],
    ['<ПРОЕКТ>/RULES.md', 'О проекте и аудитория, тон и голос, темы и запреты, куда ведём читателя, стиль фото и видео, связь контента разных сетей'],
    ['CONTROL/AGENT.md', 'Общие правила: устройство репозитория, движение материала, уникальность, задания и журнал, ключи, картинки'],
  ], [3200, 6438]),
  gap(),
  note('Сейчас в RULES.md заполнены только известные особенности сетей; разделы с пометкой «[заполним вместе]» заполняются вместе с владельцем.'),

  // --- 9
  h1('9. Пульт CONTROL'),
  p('Пульт — единственная точка управления репозиторием. Любой агент работает через него одинаково.'),
  table(['Файл или папка', 'Назначение'], [
    ['CONTROL/AGENT.md', 'Единая инструкция для любого агента. Входы AGENTS.md (ChatGPT, Codex) и CLAUDE.md (Claude) ведут сюда'],
    ['CONTROL/ACTIVE-AGENT.yaml', 'Кнопка: кто сейчас управляет (claude, chatgpt или none), с какого времени, кем переключено'],
    ['CONTROL/TASKS/INBOX/', 'Новые задания — файл на задание'],
    ['CONTROL/TASKS/IN-WORK/', 'Задания в работе — с пометкой, какой агент взял и когда'],
    ['CONTROL/TASKS/DONE/', 'Выполненные задания — с итогом и ссылкой на результат'],
    ['CONTROL/JOURNAL/', 'Журнал по дням: время · агент · что сделано; agent-switches.md — история переключений'],
    ['CONTROL/TOOLS/', 'Команды пульта: queue, prepare, check, publish, archive, image-request (логику добавим следующим шагом)'],
  ], [3200, 6438]),
  gap(),
  h2('Команды пульта'),
  table(['Команда', 'Что делает'], [
    ['queue', 'Показывает очередь READY по всем проектам и сетям'],
    ['prepare', 'Собирает пост в READY из запаса на нужную дату и время'],
    ['check', 'Проверяет пост: лимиты сети, ссылка, уникальность'],
    ['publish', 'Публикует посты, время которых наступило (по расписанию, без агента)'],
    ['archive', 'Переносит вышедший пост в PUBLISHED и пишет info.json'],
    ['image-request', 'Заявка на картинку Higgsfield — генерация только после согласия на цену'],
  ], [2200, 7438]),

  // --- 10
  h1('10. Кнопка и смена агента'),
  ...image('04-кнопка-и-смена-агента.png', 'Схема 5. Кнопка и смена агента'),
  h2('Как переключить'),
  num('Открыть репозиторий на GitHub (можно в мобильном приложении).', 'num3'),
  num('Вкладка **Actions** → слева **«Переключить агента»** → кнопка **Run workflow**.', 'num3'),
  num('Выбрать агента: **claude**, **chatgpt** или **none** (никто), при желании написать комментарий → Run workflow.', 'num3'),
  num('Через несколько секунд в CONTROL/ACTIVE-AGENT.yaml появится новый агент, а в журнале переключений — строка с датой.', 'num3'),
  h2('Почему ничего не теряется'),
  bullet('Контент лежит в папках проектов, а не у агента.'),
  bullet('Незаконченные задания — в TASKS/IN-WORK, с пометкой, кто и когда их взял.'),
  bullet('Что уже сделано — в JOURNAL. Новый агент читает эти три места и продолжает.'),
  bullet('Агент, который не выбран, ничего не меняет — два агента не мешают друг другу.'),
  bullet('Агенты сохраняют работу мелкими шагами (коммит после каждого шага), поэтому при сбое теряется максимум один незаконченный шаг.'),

  // --- 11
  h1('11. Как работает агент'),
  num('Обновляет репозиторий и проверяет CONTROL/ACTIVE-AGENT.yaml. Если управление не у него — ничего не меняет и сообщает владельцу.', 'num4'),
  num('Читает CONTROL/AGENT.md, затем TASKS/IN-WORK и JOURNAL за последние дни.', 'num4'),
  num('Задание от владельца сначала записывает в TASKS/INBOX, затем переносит в IN-WORK со своей пометкой и сразу сохраняет.', 'num4'),
  num('Работает мелкими шагами: после каждого шага — коммит и пуш в main, строка в журнале.', 'num4'),
  num('Соблюдает правила: уникальность, порядок RULES.md, факты только из материалов владельца, картинки — только после согласия на цену.', 'num4'),
  num('Закончив, переносит задание в DONE с итогом и показывает результат владельцу (превью, список постов).', 'num4'),
  num('Общается с владельцем по-русски, просто и коротко.', 'num4'),
  note('Для быстрого старта любого агента есть отдельный документ — DOCS/POST-HUB_промпт-для-агента.md. Его можно целиком вставить в ChatGPT, Claude или другого агента.'),

  // --- 12
  h1('12. Публикация'),
  p('Публикацию будут делать скрипты по расписанию (GitHub Actions или сервер владельца) — без участия агента. Время публикаций и подключения (коннекторы) к каждой сети настраиваются позже, в RULES.md сети.'),
  table(['Сеть', 'Что известно о подключении'], [
    ['Telegram', 'Бот, добавленный админом в канал; подпись к фото до 1024 символов, разметка HTML'],
    ['Дзен', 'Может сам копировать посты из Telegram-канала (бот кросспостинга); заголовок карточки — первая строка поста'],
    ['Блог', 'Статья добавляется на сайт проекта; сайт пересобирается сам'],
    ['Facebook, LinkedIn', 'Через Make (вебхук). На бесплатном тарифе Make — до 2 активных сценариев'],
    ['Instagram', 'Официальный API для бизнес- и авторских аккаунтов; картинка нужна по публичной ссылке'],
    ['Threads', 'Свой API; пост до 500 символов'],
    ['X', 'API платный; пост до 280 символов на обычном аккаунте'],
    ['YouTube', 'API с суточной квотой загрузок (около 6 роликов в сутки на проект Google)'],
    ['WeChat', 'API официального аккаунта — у верифицированного аккаунта (проверить при подключении)'],
    ['Xiaohongshu', 'Открытого API для публикации, насколько известно, нет — вероятен полуавтомат: пост готов в READY, публикует владелец'],
  ], [2400, 7238]),

  // --- 13
  h1('13. Хранение файлов'),
  bullet('**Видео** (mp4, mov, m4v, webm, avi, mkv) и аудио хранятся через **Git LFS** — правило в файле .gitattributes.'),
  bullet('**Файлы никогда не удаляются** — только переносятся: запас → READY → PUBLISHED. Архив PUBLISHED хранится всегда.'),
  bullet('**Фото** хранятся в обычном git; лучше JPG размером до 1 МБ.'),
  bullet('Объём LFS на GitHub ограничен тарифом. Когда видео станет много — докупим место или вынесем старый архив видео в облако.'),

  // --- 14
  h1('14. Картинки Higgsfield'),
  bullet('Новые генерации — **только после того, как владелец увидел цену и согласился**.'),
  bullet('Сначала проба на нескольких постах, потом партиями. Перед одобрением — лист картинок в чат.'),
  bullet('На картинке нет текста и чужих логотипов: Higgsfield искажает надписи.'),
  bullet('Одна картинка используется один раз — во всех сетях и проектах.'),

  // --- 15
  h1('15. Ключи и доступы'),
  bullet('Все ключи и токены (Telegram-бот, Instagram, Make, ключи агентов) — **только в GitHub**: Settings → Secrets and variables → Actions.'),
  bullet('Ключи никогда не присылаются в чат и не записываются в файлы репозитория.'),
  bullet('Каждому агенту нужен свой доступ к GitHub; доступы к соцсетям — у скриптов публикации через секреты.'),

  // --- 16
  h1('16. Действующие публикации в других репозиториях'),
  p('Сейчас посты выходят из других мест. Их **не трогаем и не отключаем** — сначала строим новую архитектуру в POST-HUB, потом переключаем каналы по одному и только по решению владельца.'),
  table(['Канал', 'Где работает', 'Состояние на 10.10.2026'], [
    ['Telegram GTT и Telegram Aura (Aura зеркалится в Дзен)', 'claude-control → сервер владельца', 'последний пост 09.10, 18:00 МСК; очередь до 30.10 (по 2 поста в день)'],
    ['Блог globaltechtour.ru', 'автопубликация в SINOTECH', 'последняя статья 03.10; 32 готовые статьи не вышли'],
    ['Блог aura-robotics.ru', 'автопубликация в AURA', 'последняя статья 09.10; запас примерно до 04.11'],
    ['Facebook GTT и Aura', 'Make, из claude-control', 'последние посты 02.10 (GTT) и 06.10 (Aura); очередь пустая'],
    ['Facebook и LinkedIn (личные)', 'Make, из claude-control', 'вручную после статьи в личном блоге'],
    ['Личный блог', 'claude-control', 'последняя статья 10.10; в запасе ещё 4'],
    ['Instagram GTT и Aura', 'MyFirst (GitHub Actions)', 'публикаций не было; по 1 карусели висит в очереди с сентября'],
  ], [3000, 2800, 3838]),

  // --- 17
  h1('17. Что дальше'),
  table(['Шаг', 'Статус'], [
    ['Структура: 3 проекта × 11 сетей, форматы в Instagram, Facebook, YouTube и Дзене', 'готово'],
    ['Пульт CONTROL и кнопка «Переключить агента»', 'готово'],
    ['Правила проектов и сетей (RULES.md)', 'заполняем вместе'],
    ['Команды пульта: queue, prepare, check, publish, archive, image-request', 'следующий шаг'],
    ['Время публикаций по сетям', 'позже'],
    ['Коннекторы сетей', 'позже'],
    ['Перенос контента и переключение каналов из старых систем', 'по решению владельца'],
  ], [7000, 2638]),
];

const doc = new Document({
  creator: 'POST-HUB', title: 'POST-HUB — архитектура и правила',
  styles: {
    default: { document: { run: { font: FONT, size: 22, color: INK } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 32, bold: true, color: BLUE, font: FONT }, paragraph: { spacing: { before: 360, after: 160 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 26, bold: true, color: INK, font: FONT }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } } } }] },
    ...['num', 'num1', 'num2', 'num3', 'num4'].map((reference) => ({ reference, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 360 } } } }] })),
  ] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
      new TextRun({ text: 'POST-HUB · архитектура и правила · стр. ', font: FONT, size: 16, color: MUTE }),
      new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: MUTE })] })] }) },
    children: content,
  }],
});

Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log(OUT); });
