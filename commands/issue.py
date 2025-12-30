from wg_keys import wg_genkey, server_pubkey
from wg_runtime import add_peer
from wg_config import add_peer_to_config
from utils import get_public_ip, log_action
from config import WG_IF, LOG_FILE
from storage import ClientStore

def run(store: ClientStore):
    username = input("Username: ").strip()
    if not username:
        print("Empty username")
        return
    if store.get(username):
        print("User already exists")
        return

    client_os = input("Client OS [unknown]: ").strip() or "unknown"
    purpose = input("Purpose [general]: ").strip() or "general"
    allowed_input = input("Allowed IPs (all/resources/{custom CIDR}) [resources]: ").strip() or "resources"

    # IP generation
    used_ips = {c["ip"].split(".")[-1] for c in store.all_clients().values() if c.get("ip")}
    ip = None
    for i in range(2, 255):
        if str(i) not in used_ips:
            ip = f"10.200.200.{i}"
            break
    if not ip:
        print("No free IPs left")
        return

    priv, pub = wg_genkey()

    if allowed_input == "all":
        allowed_ips = "0.0.0.0/0"
    elif allowed_input == "resources":
        allowed_ips = f"{ip}/32"
    else:
        allowed_ips = allowed_input

    add_peer(WG_IF, pub, ip)
    add_peer_to_config(username, pub, allowed_ips)

    conf = "\n".join([
        "[Interface]",
        f"PrivateKey = {priv}",
        f"Address = {ip}/32",
        "DNS = 1.1.1.1",
        "",
        "[Peer]",
        f"PublicKey = {server_pubkey()}",
        f"Endpoint = {get_public_ip()}:{51820}",
        f"AllowedIPs = {allowed_ips}",
        "PersistentKeepalive = 25"
    ])

    with open(f"{username}.conf", "w") as f:
        f.write(conf)

    store.add(username, {
        "ip": ip,
        "pubkey": pub,
        "privkey": priv,
        "status": "active",
        "client_os": client_os,
        "purpose": purpose,
        "allowed": allowed_ips
    })

    log_action(LOG_FILE, action="issue", username=username, ip=ip,
               client_os=client_os, purpose=purpose, allowed_ips=allowed_ips)

    print(f"Issued {username} ({ip}) -> {username}.conf")
