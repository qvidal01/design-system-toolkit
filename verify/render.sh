#!/usr/bin/env bash
# render.sh <card.html> [out.png] [WIDTHxHEIGHT]
# Screenshot a card with headless Chrome so you can eyeball it before pushing.
set -euo pipefail
CARD="${1:?usage: render.sh card.html [out.png] [WIDTHxHEIGHT]}"
OUT="${2:-${CARD%.html}.png}"
SIZE="${3:-900x900}"; W="${SIZE%x*}"; H="${SIZE#*x}"
CH="$(command -v google-chrome || command -v chromium || command -v chromium-browser || true)"
if [ -z "$CH" ]; then
  CH="$(find "$HOME/.cache/puppeteer" -type f \( -name 'chrome-headless-shell' -o -name 'chrome' \) 2>/dev/null | head -1)"
fi
[ -n "$CH" ] && [ -x "$CH" ] || { echo "no executable chrome/chromium found (install one or set PATH)" >&2; exit 1; }
"$CH" --headless --no-sandbox --hide-scrollbars --force-color-profile=srgb \
  --window-size="$W,$H" --screenshot="$OUT" "file://$(readlink -f "$CARD")" >/dev/null 2>&1
echo "wrote $OUT ($(du -h "$OUT" | cut -f1))"
