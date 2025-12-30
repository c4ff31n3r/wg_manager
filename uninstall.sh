#!/bin/bash
set -e

BIN_PATH="/usr/local/bin/wg_manager"

echo "Removing wg_manager..."

if [ -L "$BIN_PATH" ] || [ -f "$BIN_PATH" ]; then
    rm -f "$BIN_PATH"
    echo "Symbolic link has been removed"
else
    echo "File '$BIN_PATH' not found"
fi

echo "Removal finished"
