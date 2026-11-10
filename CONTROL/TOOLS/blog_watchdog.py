#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сторож блогов: если статья просрочена и лежит в READY — запустить публикатор.

Запускается из workflow «Сторож блогов» раз в час. Ничего не публикует сам:
только дергает нужный workflow, чтобы логика публикации осталась в одном месте.
"""
import datetime
import os
import pathlib
import re
import subprocess
import sys

MAX_LATE_H = 2.0  # сколько часов просрочки считаем нормой (cron + задержка GitHub)
MSK = datetime.timezone(datetime.timedelta(hours=3))  # в именах папок — московское время

PLANS = [
    # проект, репозиторий с публикатором, workflow
    ("OSTAPDOTCENKO", os.environ.get("HUB", "Ostap-87/POST-HUB"), "blog-od.yml"),
    ("GTT", "Ostap-87/SINOTECH", "blog-from-post-hub.yml"),
    ("AURA", "Ostap-87/AURA", "blog-from-post-hub.yml"),
]


def head_ready(project):
    root = pathlib.Path(project) / "BLOG" / "READY"
    if not root.is_dir():
        return None
    items = []
    for p in root.iterdir():
        m = re.match(r"^(\d{4}-\d{2}-\d{2})_(\d{4})", p.name)
        if m and p.is_dir():
            dt = datetime.datetime.strptime(m.group(1) + m.group(2), "%Y-%m-%d%H%M")
            items.append((dt.replace(tzinfo=MSK).astimezone(datetime.timezone.utc), p.name))
    return min(items)[0] if items else None


def dispatch(repo, workflow, token):
    url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow}/dispatches"
    r = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-m", "30", "-X", "POST",
         "-H", f"Authorization: Bearer {token}", "-H", "Accept: application/vnd.github+json",
         "-d", '{"ref":"main"}', url],
        capture_output=True, text=True)
    return r.stdout.strip()


def main():
    token = os.environ.get("GH_TOKEN", "")
    if not token:
        print("::error::Нет GH_TOKEN — не могу запускать публикаторы")
        return 1
    now = datetime.datetime.now(datetime.timezone.utc)
    lagging = []
    for project, repo, wf in PLANS:
        due = head_ready(project)
        if due is None:
            print(f"{project}: очередь пуста")
            continue
        late = (now - due).total_seconds() / 3600
        print(f"{project}: в очереди {due:%Y-%m-%d %H:%M} UTC, просрочка {late:.1f} ч")
        if late > MAX_LATE_H:
            code = dispatch(repo, wf, token)
            print(f"  → запускаю {repo}/{wf}: HTTP {code}")
            lagging.append(f"{project} ({late:.1f} ч)")
    if lagging:
        print("::warning::Догнал публикацию: " + ", ".join(lagging))
    return 0


if __name__ == "__main__":
    sys.exit(main())
