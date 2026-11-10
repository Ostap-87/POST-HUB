#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Отправка уведомления в Telegram.

Использование:
    python3 CONTROL/TOOLS/notify.py "текст сообщения"

Секреты (GitHub → Settings → Secrets → Actions):
    TELEGRAM_BOT_TOKEN — токен бота от @BotFather
    TELEGRAM_CHAT_ID   — id чата (ваш user id или id группы)

Если секретов нет — скрипт молча выходит с кодом 0, чтобы не ломать публикацию.
"""
import json
import os
import sys
import urllib.parse
import urllib.request

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
CHAT = os.environ.get("TELEGRAM_CHAT_ID", "").strip()


def send(text):
    if not TOKEN or not CHAT:
        print("уведомления выключены: нет TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID")
        return 0
    data = urllib.parse.urlencode({
        "chat_id": CHAT,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": "false",
    }).encode()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        with urllib.request.urlopen(url, data=data, timeout=20) as r:
            ok = json.load(r).get("ok")
        print("уведомление отправлено" if ok else "Telegram ответил отказом")
    except Exception as e:
        # уведомление не должно валить публикацию
        print(f"не удалось отправить уведомление: {e}")
    return 0


if __name__ == "__main__":
    msg = " ".join(sys.argv[1:]).strip() or sys.stdin.read().strip()
    sys.exit(send(msg))
