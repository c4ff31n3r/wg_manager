from wg_runtime import update_allowed_ips
from wg_config import remove_peer_from_config, add_peer_to_config
from utils import get_public_ip, log_action
from config import WG_IF, LOG_FILE
from storage import ClientStore
from wg_keys import server_pubkey

def run(store: ClientStore, username: str):
    client = store.get(username)
    if not client:
        print("User not found")
        return

    old_ip = client["ip"]
    old_pub = client["pubkey"]

    # Enter new metadata
    new_username = input(f"Username [{username}]: ").strip() or username
    new_ip = input(f"IP [{old_ip}]: ").strip() or old_ip
    new_allowed = input(f"Allowed IPs (all/resources/custom) [{client['allowed']}]: ").strip() or client["allowed"]
    new_os = input(f"Client OS [{client['client_os']}]: ").strip() or client["client_os"]
    new_purpose = input(f"Purpose [{client['purpose']}]: ").strip() or client["purpose"]

    # Update runtime and config
    update_allowed_ips(WG_IF, old_pub, new_ip)
    remove_peer_from_config(old_pub)

    if new_allowed == "all":
        allowed_ips_str = "0.0.0.0/0"
    elif new_allowed == "resources":
        allowed_ips_str = f"{new_ip}/32"
    else:
        allowed_ips_str = new_allowed

    add_peer_to_config(new_username, old_pub, allowed_ips_str)

    # Create client's config
    conf_path = f"{new_username}.conf"
    conf_text = "\n".join([
        "[Interface]",
        f"Address = {new_ip}/32",
        f"PrivateKey = {client['privkey']}",
        "DNS = 1.1.1.1",
        "",
        "[Peer]",
        f"PublicKey = {server_pubkey()}",
        f"Endpoint = {get_public_ip()}:{51820}",
        f"AllowedIPs = {allowed_ips_str}",
        "PersistentKeepalive = 25"
    ])
    with open(conf_path, "w") as f:
        f.write(conf_text)

    # Update DB
    client.update({
        "ip": new_ip,
        "allowed": new_allowed,
        "client_os": new_os,
        "purpose": new_purpose
    })
    if new_username != username:
        store.data["clients"][new_username] = client
        del store.data["clients"][username]
    store.save()

    log_action(LOG_FILE,
               action="edit",
               username=new_username,
               ip=new_ip,
               client_os=new_os,
               purpose=new_purpose,
               allowed_ips=allowed_ips_str)

    print(f"Updated client {new_username} -> {conf_path}")
