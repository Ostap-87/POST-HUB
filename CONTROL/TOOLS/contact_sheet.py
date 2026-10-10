#!/usr/bin/env python3
"""Лист картинок на согласование (CONTROL/IMAGE-RULES.md, раздел 7).

python3 CONTROL/TOOLS/contact_sheet.py AURA/TELEGRAM 1 12 -o лист.jpg [--title "…"] [--cols 4 --width 480]
Берёт тексты из <сеть>/TEXT (или <сеть>/<формат>/TEXT) и из READY/*/post.md по номеру в плане (поле number),
картинки — из PHOTO или из папки поста (поле image), рисует сетку 3 в ряд: картинка, номер, дата и время, заголовок, статус.
"""
import argparse
import glob
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HUB = Path(__file__).resolve().parents[2]
FONT = HUB / 'AURA/BRAND/FONTS/Inter-variable.ttf'


def meta_of(path):
    fm = open(path, encoding='utf-8').read().split('---\n', 2)[1]
    m = {}
    for line in fm.strip().split('\n'):
        k, v = line.split(': ', 1)
        m[k] = json.loads(v) if v.startswith('"') else v
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('channel', help='например AURA/TELEGRAM или GTT/FACEBOOK/POST')
    ap.add_argument('first', type=int)
    ap.add_argument('last', type=int)
    ap.add_argument('-o', '--out', required=True)
    ap.add_argument('--title', default='')
    ap.add_argument('--cols', type=int, default=3, help='картинок в ряд (для вертикальных 4:5 удобно 4)')
    ap.add_argument('--width', type=int, default=640, help='ширина картинки на листе, px')
    ap.add_argument('--order', choices=['number', 'date'], default='number',
                    help='date — first/last по порядку дат (для блогов, где number свой у каждой рубрики)')
    a = ap.parse_args()
    ch = HUB / a.channel
    items = []
    for f in sorted(glob.glob(str(ch / 'TEXT/*.md'))):
        m = meta_of(f)
        if (a.order == 'date' or a.first <= int(m['number']) <= a.last) and m.get('image'):
            items.append((int(m['number']), m, ch / 'PHOTO' / m['image']))
    for f in sorted(glob.glob(str(ch / 'READY/*/post.md'))):   # посты, уже перенесённые в очередь
        m = meta_of(f)
        if a.first <= int(m['number']) <= a.last and m.get('image'):
            items.append((int(m['number']), m, Path(f).parent / m['image']))
    seen, uniq = set(), []                      # статья блога в трёх языках — одна картинка
    for it in sorted(items, key=lambda x: (x[1]['date'], x[1].get('lang', 'ru') != 'ru', str(x[2]))):   # русская версия первой
        if it[2] not in seen:
            seen.add(it[2]); uniq.append(it)
    if a.order == 'date':
        allp = []
        for f in sorted(glob.glob(str(ch / 'TEXT/*.md'))):
            m = meta_of(f)
            if m.get('image') and m['image'] not in allp:
                allp.append(m['image'])
        pos = {img: k + 1 for k, img in enumerate(allp)}
        uniq = [(pos[i[2].name], i[1], i[2]) for i in uniq if i[2].name in pos and a.first <= pos[i[2].name] <= a.last]
    items = sorted(uniq, key=lambda x: x[0])
    cols, W, pad, cap = a.cols, a.width, 24, 70
    imgs = [Image.open(p).convert('RGB') for _, _, p in items]
    H = round(W * imgs[0].height / imgs[0].width) if imgs else 360
    rows = (len(items) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * W + (cols + 1) * pad, 80 + rows * (H + cap + pad) + pad), (244, 244, 246))
    d = ImageDraw.Draw(sheet)
    ft, fb, fs = (ImageFont.truetype(str(FONT), s) for s in (30, 20, 17))
    d.text((pad, 24), a.title or f'{a.channel} · №{a.first}–{a.last}', font=ft, fill=(23, 23, 29))
    for k, ((num, m, _), img) in enumerate(zip(items, imgs)):
        x = pad + (k % cols) * (W + pad)
        y = 80 + pad + (k // cols) * (H + cap + pad)
        sheet.paste(img.resize((W, H), Image.LANCZOS), (x, y))
        date = m['date']
        tm = m.get('time', '')
        when = f"{date[8:]}.{date[5:7]}" + (f" {tm}" if len(tm) == 5 and tm[2] == ':' else '')   # в блогах time — время чтения
        status = '' if m.get('image_status') == 'утверждено' else ' · на согласовании'
        d.text((x, y + H + 8), f'№{num} · {when}{status}', font=fb, fill=(37, 99, 235))
        lim = round(62 * W / 640)                    # сколько знаков заголовка влезает под картинку
        t = m['title'] if len(m['title']) < lim else m['title'][:lim - 2] + '…'
        d.text((x, y + H + 36), t, font=fs, fill=(23, 23, 29))
    sheet.save(a.out, quality=88)
    print(a.out, len(items))


if __name__ == '__main__':
    main()
