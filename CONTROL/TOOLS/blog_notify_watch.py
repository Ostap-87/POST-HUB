#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Уведомление в Telegram о выходе статей на globaltechtour.ru и aura-robotics.ru.

Вызывается из дежурного workflow блога ostapdotcenko — там уже есть секреты Telegram,
поэтому дублировать их в SINOTECH и AURA не нужно.

Сравнивает самый свежий пост в sitemap с сохранённым состоянием. Первый запуск
только запоминает состояние, чтобы не присылать ложные сообщения о старых статьях.
"""
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "CONTROL" / "STATE" / "blog-notify-seen.json"
NOTIFY = ROOT / "CONTROL" / "TOOLS" / "notify.py"
SITES = {
    "globaltechtour.ru": "https://globaltechtour.ru/sitemap.xml",
    "aura-robotics.ru": "https://aura-robotics.ru/sitemap.xml",
}


def newest(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 blog-watch/1.0"})
    xml = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "ignore")
    posts = [u for u in re.findall(r"<loc>([^<]+)</loc>", xml)
             if "/blog/" in u and "/category/" not in u]
    return posts[-1] if posts else ""


def main():
    state = {}
    if STATE.exists():
        try:
            state = json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            state = {}
    changed = False
    for site, sitemap in SITES.items():
        try:
            post = newest(sitemap)
        except Exception as exc:
            print("пропуск " + site + ": " + str(exc)[:60])
            continue
        if not post:
            continue
        prev = state.get(site)
        if prev == post:
            continue
        state[site] = post
        changed = True
        if prev is None:
            print("первый запуск, запоминаю " + site)
            continue
        slug = post.rstrip("/").split("/")[-1]
        title = "Новая статья на " + site
        subprocess.run([sys.executable, str(NOTIFY), title + "\n\n" + post], check=False)
        print("уведомил: " + site + " / " + slug)
    if changed:
        STATE.parent.mkdir(parents=True, exist_ok=True)
        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("state=changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
