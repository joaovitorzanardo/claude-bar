#!/usr/bin/env bash
# Instala o claude-bar como status line do Claude Code.
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
SETTINGS="$HOME/.claude/settings.json"

mkdir -p "$HOME/.claude"
ln -sf "$DIR/statusline.py" "$HOME/.claude/statusline.py"

python3 - "$SETTINGS" <<'PY'
import json, os, sys
path = sys.argv[1]
data = {}
if os.path.exists(path):
    with open(path) as f:
        data = json.load(f)
data["statusLine"] = {"type": "command", "command": "python3 ~/.claude/statusline.py"}
with open(path, "w") as f:
    json.dump(data, f, indent=2)
    f.write("\n")
PY

echo "claude-bar instalado. Reinicie o Claude Code."
