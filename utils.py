import os
import sys
import yaml
import datetime
import urllib.request
from config import MAX_LOG_ENTRIES

# ================= UTILS =================

def die(msg):
    print(f"ERROR: {msg}")
    sys.exit(1)

def ensure_dirs(paths_defaults):
    """
    paths_defaults: dict, where key = path, value = default for file
    """
    for path, default in paths_defaults.items():
        dir_path = os.path.dirname(path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if not os.path.exists(path):
            with open(path, "w") as f:
                yaml.dump(default, f)

def load_yaml(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path) as f:
        return yaml.safe_load(f) or default

def save_yaml(path, data):
    with open(path, "w") as f:
        yaml.dump(data, f)

def log_action(log_file, action, username, ip, client_os, purpose, allowed_ips, reason=None):
    logs = load_yaml(log_file, {"logs": []})
    entry = {
        "timestamp": str(datetime.datetime.now()),
        "action": action,
        "username": username,
        "ip": ip,
        "client_os": client_os,
        "purpose": purpose,
        "allowed_ips": allowed_ips
    }
    if reason:
        entry["reason"] = reason
    logs["logs"].append(entry)

    # Limit log size
    if len(logs["logs"]) > MAX_LOG_ENTRIES":
        logs["logs"] = logs["logs"][-MAX_LOG_ENTRIES:]

    save_yaml(log_file, logs)

def get_public_ip():
    try:
        with urllib.request.urlopen("https://4.ident.me") as r:
            return r.read().decode().strip()
    except:
        die("Cannot determine public IP")
