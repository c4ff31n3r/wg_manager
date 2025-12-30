#!/bin/sh

# Directories
CODE_DIR="/usr/lib/wg_manager"
BIN_PATH="/usr/local/bin/wg_manager"
DATA_DIR="/etc/wg_manager"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"

# Check root
if [ "$(id -u)" != "0" ]; then
  echo "ERROR: Must be run as root"
  exit 1
fi

# Copy code to CODE_DIR
mkdir -p "$CODE_DIR"
cp -r "$SRC_DIR/"* "$CODE_DIR/"
chown -R root:root "$CODE_DIR"
chmod -R 755 "$CODE_DIR"

# Create launcher
ln -sf "$CODE_DIR/main.py" "$BIN_PATH"
chmod +x "$CODE_DIR/main.py"

# Create data directory
mkdir -p "$DATA_DIR"
chown root:root "$DATA_DIR"
chmod 700 "$DATA_DIR"

# Create empty YAML files if missing
[ -f "$DATA_DIR/clients.yaml" ] || echo '{"clients":{}}' > "$DATA_DIR/clients.yaml"
[ -f "$DATA_DIR/logs.yaml" ]    || echo '{"logs":[]}' > "$DATA_DIR/logs.yaml"
chmod 600 "$DATA_DIR"/*.yaml

echo "wg_manager installed successfully."
echo "Launcher: $BIN_PATH"
echo "Code directory: $CODE_DIR"
echo "Data directory: $DATA_DIR"
