from wg_manager.config import WG_CONF

# ================= WG CONFIG =================

def add_peer_to_config(username, pubkey, allowed_ips):
    """
    Adds [Peer] block into WG_CONF config
    """
    block = [
        "\n",
        f"# {username}\n",
        "[Peer]\n",
        f"PublicKey = {pubkey}\n",
        f"AllowedIPs = {allowed_ips}\n",
        "PersistentKeepalive = 25\n"
    ]
    with open(WG_CONF, "a") as f:
        f.writelines(block)

def remove_peer_from_config(pubkey):
    """
    Removes [Peer] block using public key
    """
    with open(WG_CONF) as f:
        lines = f.readlines()

    out = []
    skip_block = False
    previous_line_was_empty = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        if skip_block:
            if stripped.startswith("["):
                skip_block = False
                out.append(line)
                previous_line_was_empty = False
            elif stripped == "":
                if i + 1 < len(lines) and lines[i + 1].strip().startswith("["):
                    skip_block = False
                    previous_line_was_empty = True
                continue
            else:
                continue

        if stripped == "[Peer]":
            found_key = False
            j = i + 1
            while j < len(lines):
                next_stripped = lines[j].strip()
                if next_stripped.startswith("["):
                    break
                if "PublicKey" in lines[j] and pubkey in lines[j]:
                    found_key = True
                    break
                if next_stripped == "":
                    break
                j += 1

            if found_key:
                skip_block = True
                if out and out[-1].strip().startswith("#"):
                    out.pop()
                if out and out[-1].strip() == "":
                    out.pop()
                continue

        if stripped == "":
            previous_line_was_empty = True
        else:
            previous_line_was_empty = False

        out.append(line)

    while out and out[-1].strip() == "":
        out.pop()

    with open(WG_CONF, "w") as f:
        f.writelines(out)

def import_peers_from_config(store):
    """
    Imports peers from WG_CONF into DB
    store: ClientStore object
    """
    clients = store.all_clients()
    with open(WG_CONF) as f:
        lines = f.readlines()

    current_peer = {}
    username_comment = None

    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            username_comment = line[1:].strip()
        elif line.startswith("[Peer]"):
            current_peer = {}
        elif line.startswith("PublicKey"):
            current_peer["pubkey"] = line.split("=",1)[1].strip()
        elif line.startswith("AllowedIPs"):
            allowed_ips = line.split("=",1)[1].strip()
            current_peer["allowed"] = allowed_ips
            if allowed_ips.endswith("/32"):
                current_peer["ip"] = allowed_ips.split("/")[0]

        if current_peer.get("pubkey") and current_peer.get("allowed"):
            found = None
            for u, c in clients.items():
                if c.get("pubkey") == current_peer["pubkey"]:
                    found = u
                    break
            if found:
                clients[found]["ip"] = current_peer.get("ip", clients[found].get("ip"))
                clients[found]["allowed"] = current_peer.get("allowed")
            else:
                new_username = username_comment or current_peer["pubkey"][:8]
                if new_username in clients:
                    i = 1
                    while f"{new_username}_{i}" in clients:
                        i += 1
                    new_username = f"{new_username}_{i}"
                clients[new_username] = {
                    "ip": current_peer.get("ip", ""),
                    "pubkey": current_peer["pubkey"],
                    "privkey": "",
                    "status": "active",
                    "client_os": "unknown", # no way to determine these
                    "purpose": "unknown",
                    "allowed": current_peer["allowed"]
                }
            current_peer = {}
            username_comment = None

    store.save()
