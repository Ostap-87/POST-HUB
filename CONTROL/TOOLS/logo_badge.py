#!/usr/bin/env python3
"""Логотип бренда бейджем внизу слева (правила — CONTROL/IMAGE-RULES.md, раздел 2).

python3 CONTROL/TOOLS/logo_badge.py картинка.png логотип.svg [логотип2.png] -o результат.jpg
Без логотипов просто приводит картинку к формату хранения: JPG, длинная сторона до 1600 px, качество 88.
Нужны Pillow и (для SVG) cairosvg.
"""
import argparse
import io
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter

MAX_SIDE = 1600
LOGO_H = 0.062      # высота логотипа — доля высоты картинки
MAX_LOGO_W = 0.26   # максимальная ширина логотипа — доля ширины картинки
MARGIN = 0.032      # отступ плашки от краёв — доля короткой стороны


def load_logo(path: Path) -> Image.Image:
    if path.suffix.lower() == '.svg':
        import cairosvg
        png = cairosvg.svg2png(url=str(path), output_width=1200)
        img = Image.open(io.BytesIO(png)).convert('RGBA')
    else:
        img = Image.open(path).convert('RGBA')
    # убрать поля: прозрачные или почти белые
    alpha = img.getchannel('A')
    if alpha.getextrema()[0] < 250:
        box = alpha.point(lambda a: 255 if a > 12 else 0).getbbox()
    else:
        rgb = img.convert('RGB')
        diff = ImageChops.difference(rgb, Image.new('RGB', rgb.size, (255, 255, 255))).convert('L')
        box = diff.point(lambda v: 255 if v > 18 else 0).getbbox()
    return img.crop(box) if box else img


def plate(logo: Image.Image, h: int, max_w: int) -> Image.Image:
    lw = round(logo.width * h / logo.height)
    if lw > max_w:
        h = round(h * max_w / lw); lw = max_w
    logo = logo.resize((lw, h), Image.LANCZOS)
    px, py = round(h * 0.45), round(h * 0.34)
    w, ph = lw + 2 * px, h + 2 * py
    r = round(ph * 0.24)
    card = Image.new('RGBA', (w, ph), (0, 0, 0, 0))
    ImageDraw.Draw(card).rounded_rectangle((0, 0, w - 1, ph - 1), radius=r, fill=(255, 255, 255, 240))
    card.alpha_composite(logo, (px, py + (h - logo.height) // 2))
    return card


def badge(src: Path, logos: list[Path], out: Path) -> None:
    img = Image.open(src).convert('RGB')
    k = MAX_SIDE / max(img.size)
    if k < 1:
        img = img.resize((round(img.width * k), round(img.height * k)), Image.LANCZOS)
    if logos:
        base = img.convert('RGBA')
        m = round(min(base.size) * MARGIN)
        h = max(34, round(base.height * LOGO_H))
        x, y_bottom = m, base.height - m
        for p in logos:
            card = plate(load_logo(p), h, round(base.width * MAX_LOGO_W))
            shadow = Image.new('RGBA', base.size, (0, 0, 0, 0))
            sh = Image.new('RGBA', card.size, (0, 0, 0, 70))
            shadow.paste(sh, (x + 2, y_bottom - card.height + 3), card)
            base = Image.alpha_composite(base, shadow.filter(ImageFilter.GaussianBlur(6)))
            base.alpha_composite(card, (x, y_bottom - card.height))
            x += card.width + round(m * 0.5)
        img = base.convert('RGB')
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, 'JPEG', quality=88, optimize=True, progressive=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('image')
    ap.add_argument('logos', nargs='*')
    ap.add_argument('-o', '--out', required=True)
    a = ap.parse_args()
    badge(Path(a.image), [Path(x) for x in a.logos], Path(a.out))
    print(a.out)
