import subprocess
from utils import die
from config import WG_CONF

# ================= WG KEYS =================

def wg_genkey():
    """
    Generates client's public and private keys
    """
    priv = subprocess.check_output(["wg", "genkey"]).decode().strip()
    pub = subprocess.check_output(["wg", "pubkey"], input=priv.encode()).decode().strip()
    return priv, pub

def server_pubkey():
    """
    Gets public key using WG_CONF file
    """
    try:
        with open(WG_CONF) as f:
            for line in f:
                if line.startswith("PrivateKey"):
                    priv = line.split("=", 1)[1].strip()
                    return subprocess.check_output(["wg", "pubkey"], input=priv.encode()).decode().strip()
    except FileNotFoundError:
        die(f"WG config file {WG_CONF} not found")
    die("Server private key not found in WG config")
