#!/bin/bash
set -e

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
BIN_PATH="/usr/local/bin/wg_manager"

echo "Installing wg_manager..."

chmod +x "$BASE_DIR/main.py"

ln -sf "$BASE_DIR/main.py" "$BIN_PATH"

echo "wg_manager has been installed, you can try it out using 'wg_manager' command"
