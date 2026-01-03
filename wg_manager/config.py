import platform

# ================= CONFIG =================

SYSTEM = platform.system()
if SYSTEM == "Linux":
    WG_CONF = "/etc/wireguard/wg0.conf"
    DATA_DIR = "/etc/wg_manager"
elif SYSTEM == "FreeBSD":
    WG_CONF = "/usr/local/etc/wireguard"
    DATA_DIR = "/var/db/wg_manager"	

WG_IF = "wg0"
DB_FILE = f"{DATA_DIR}/clients.yaml"
LOG_FILE = f"{DATA_DIR}/logs.yaml"
SUBNET = "10.200.200."
DNS = "1.1.1.1"
ENDPOINT_PORT = 51820
KEEPALIVE = 25
MAX_LOG_ENTRIES = 500
