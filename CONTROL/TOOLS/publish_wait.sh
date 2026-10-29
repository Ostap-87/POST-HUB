#!/usr/bin/env bash
# Дежурный прогон публикатора — режим `wait` в .github/workflows/publish.yml.
#
# Зачем (решение пользователя 29.10.2026: посты выходят точно в 08:30, 08:45, 09:00, 17:30, 17:45, 18:00, в выходные —
# 10:00, 10:15, 11:00 по Москве): расписание GitHub (cron) запускает прогоны с опозданием на часы, поэтому прогон не
# «публикует и выходит», а дежурит ~5 ч 40 мин:
#   1. забирает свежий main (новые посты в READY и правки CONTROL/PUBLISHING.yaml подхватываются на ходу);
#   2. publish.py --due — публикует всё, чему наступило время (пауза и pause_allow действуют как обычно);
#   3. сразу записывает результат в репозиторий (вышедшее уезжает в PUBLISHED — второй прогон его не повторит);
#   4. спит до ближайшего поста (publish.py --next), но не дольше 10 минут.
# В конце publish.yml запускает следующего дежурного — дежурство непрерывное; cron остаётся запасным стартом.
# Остановить цепочку — отменить текущий прогон «Публикация» в Actions; ничего не публиковать — pause: true без pause_allow.
#
#   WINDOW=20400 bash CONTROL/TOOLS/publish_wait.sh     # сколько секунд дежурить (по умолчанию 5 ч 40 мин)
set -u
cd "$(dirname "$0")/../.."
WINDOW=${WINDOW:-20400}
HARD=$(( $(date +%s) + WINDOW + 600 ))   # пост сразу после конца окна (до 10 мин) дожидаемся — не отдаём его пересменке
end=$(( $(date +%s) + WINDOW ))
rc=0

save() {
  git add -A
  git diff --cached --quiet && return 0
  git -c user.name="github-actions[bot]" -c user.email="41898282+github-actions[bot]@users.noreply.github.com" \
    commit -q -m "Публикация: результат прогона $(date -u '+%Y-%m-%d %H:%M') UTC"
  for i in 1 2 3 4 5; do git pull --rebase -q && git push -q && return 0; sleep $(( i * 5 )); done
  return 1
}

while :; do
  git pull --rebase -q || echo "! не удалось забрать main — работаю с тем, что есть"
  python3 CONTROL/TOOLS/publish.py --due || rc=1
  save || { echo "! не удалось записать результат"; rc=1; }
  now=$(date +%s)
  nxt=$(python3 CONTROL/TOOLS/publish.py --next || true)
  if [ "$now" -ge "$end" ]; then
    # окно кончилось: остаёмся, только если ближайший пост вот-вот (и ещё есть запас до жёсткого предела)
    if [ -z "$nxt" ] || [ $(( nxt - now )) -gt 600 ] || [ "$nxt" -gt "$HARD" ]; then break; fi
  fi
  pause=600
  if [ -n "$nxt" ]; then
    d=$(( nxt - now + 2 ))
    [ "$d" -lt "$pause" ] && pause=$d
    echo "  … ближайший пост в $(TZ=Europe/Moscow date -d "@$nxt" '+%d.%m %H:%M') МСК"
  fi
  [ "$now" -lt "$end" ] && [ $(( end - now )) -lt "$pause" ] && pause=$(( end - now ))
  [ "$pause" -lt 1 ] && pause=1
  sleep "$pause"
done
exit $rc
