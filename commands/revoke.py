from wg_runtime import remove_peer
from wg_config import remove_peer_from_config
from utils import log_action
from config import WG_IF, LOG_FILE
from storage import ClientStore

def run(store: ClientStore, username: str):
    client = store.get(username)
    if not client:
        print("User not found")
        return

    pub = client["pubkey"]
    ip = client["ip"]

    remove_peer(WG_IF, pub)
    remove_peer_from_config(pub)

    store.revoke(username)

    log_action(LOG_FILE,
               action="revoke",
               username=username,
               ip=ip,
               client_os=client.get("client_os", "unknown"),
               purpose=client.get("purpose", "unknown"),
               allowed_ips=client.get("allowed", "resources"),
               reason="revoked manually")

    print(f"Revoked {username}")
