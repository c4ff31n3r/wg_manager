from wg_keys import wg_genkey, server_pubkey
from wg_runtime import remove_peer, add_peer
from wg_config import remove_peer_from_config, add_peer_to_config
from utils import get_public_ip, log_action
from config import WG_IF, LOG_FILE
from storage import ClientStore

def run(store: ClientStore, username: str):
    client = store.get(username)
    if not client:
        print("User not found")
        return

    old_ip = client["ip"]
    old_pub = client["pubkey"]

    # Delete an old peer
    remove_peer(WG_IF, old_pub)
    remove_peer_from_config(old_pub)

    # Generate new keys
    priv, pub = wg_genkey()

    # Add a new peer with the same IP
    add_peer(WG_IF, pub, old_ip)
    add_peer_to_config(username, pub, f"{old_ip}/32")

    allowed_ips = client.get("allowed", f"{old_ip}/32")

    # Create client's config
    conf = "\n".join([
        "[Interface]",
        f"PrivateKey = {priv}",
        f"Address = {old_ip}/32",
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

    # Update DB
    store.update(username, {"privkey": priv, "pubkey": pub, "status": "active"})

    log_action(LOG_FILE,
               action="recreate",
               username=username,
               ip=old_ip,
               client_os=client.get("client_os", "unknown"),
               purpose=client.get("purpose", "unknown"),
               allowed_ips=allowed_ips)

    print(f"Recreated {username} -> {username}.conf")
