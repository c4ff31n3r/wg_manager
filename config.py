# ================= CONFIG =================

WG_IF = "wg0"
WG_CONF = "/etc/wireguard/wg0.conf"
BASE_DIR = "/etc/wireguard/wg_manager"
DB_FILE = f"{BASE_DIR}/clients.yaml"
LOG_FILE = f"{BASE_DIR}/logs.yaml"
SUBNET = "10.200.200."
DNS = "1.1.1.1"
ENDPOINT_PORT = 51820
KEEPALIVE = 25
MAX_LOG_ENTRIES = 500
