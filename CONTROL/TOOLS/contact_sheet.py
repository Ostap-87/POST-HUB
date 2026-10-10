#!/usr/bin/env python3
"""Лист картинок на согласование (CONTROL/IMAGE-RULES.md, раздел 7).

python3 CONTROL/TOOLS/contact_sheet.py AURA/TELEGRAM 1 12 -o лист.jpg [--title "…"]
Берёт тексты из <сеть>/TEXT (или <сеть>/<формат>/TEXT) по номеру в плане (поле number), картинки — из PHOTO
(поле image), рисует сетку 3 в ряд: картинка, номер, дата и время, заголовок, статус.
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
    a = ap.parse_args()
    ch = HUB / a.channel
    items = []
    for f in sorted(glob.glob(str(ch / 'TEXT/*.md'))):
        m = meta_of(f)
        if a.first <= int(m['number']) <= a.last and m.get('image'):
            items.append((int(m['number']), m, ch / 'PHOTO' / m['image']))
    items.sort(key=lambda x: x[0])
    cols, W, pad, cap = 3, 640, 24, 70
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
        when = f"{date[8:]}.{date[5:7]}" + (f" {m['time']}" if m.get('time') else '')
        status = '' if m.get('image_status') == 'утверждено' else ' · на согласовании'
        d.text((x, y + H + 8), f'№{num} · {when}{status}', font=fb, fill=(37, 99, 235))
        t = m['title'] if len(m['title']) < 62 else m['title'][:60] + '…'
        d.text((x, y + H + 36), t, font=fs, fill=(23, 23, 29))
    sheet.save(a.out, quality=88)
    print(a.out, len(items))


if __name__ == '__main__':
    main()
