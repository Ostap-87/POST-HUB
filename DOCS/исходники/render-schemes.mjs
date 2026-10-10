// Рендер схем из схемы.html в PNG: node DOCS/исходники/render-schemes.mjs
// Результат — DOCS/схемы/01-…png. Нужен playwright (глобально или в node_modules).
import { createRequire } from 'module';
import path from 'path';
import { fileURLToPath } from 'url';
const require = createRequire(import.meta.url);
let pw;
for (const p of ['playwright', '/opt/node22/lib/node_modules/playwright']) {
  try { pw = require(p); break; } catch (e) {}
}
if (!pw) { console.error('Не найден playwright'); process.exit(1); }
const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.join(here, '..', 'схемы');
const names = { d1: '01-общая-схема', d2: '02-проект-изнутри', d3: '03-путь-поста', d4: '04-кнопка-и-смена-агента', d5: '05-порядок-правил' };
const browser = await pw.chromium.launch();
const page = await browser.newPage({ viewport: { width: 1500, height: 1000 }, deviceScaleFactor: 2 });
await page.goto('file://' + path.join(here, 'схемы.html'), { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
for (const [id, name] of Object.entries(names)) {
  await page.locator('#' + id).screenshot({ path: path.join(out, name + '.png') });
  console.log(name);
}
await browser.close();
