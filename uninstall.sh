#!/bin/sh

BIN_PATH="/usr/local/bin/wg_manager"
CODE_DIR="/usr/lib/wg_manager"
DATA_DIR="/etc/wg_manager"

# Check root
if [ "$(id -u)" != "0" ]; then
  echo "ERROR: Must be run as root"
  exit 1
fi

# Remove launcher
if [ -L "$BIN_PATH" ] || [ -f "$BIN_PATH" ]; then
  rm -f "$BIN_PATH"
  echo "Launcher removed: $BIN_PATH"
fi

# Warn about code directory
if [ -d "$CODE_DIR" ]; then
  echo "WARNING: $CODE_DIR contains installed code."
  echo "Remove manually if needed: sudo rm -rf $CODE_DIR"
fi

# Warn about data directory
if [ -d "$DATA_DIR" ]; then
  echo "WARNING: $DATA_DIR contains client keys and data."
  echo "Remove manually if needed: sudo rm -rf $DATA_DIR"
fi

echo "wg_manager uninstalled."
