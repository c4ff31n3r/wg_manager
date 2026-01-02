import subprocess

# ================= WG RUNTIME =================

def add_peer(iface, pubkey, ip, dry_run=False):
    """
    Добавляет peer в рантайм WireGuard
    """
    cmd = ["wg", "set", iface, "peer", pubkey, "allowed-ips", f"{ip}/32"]
    if dry_run:
        print("[DRY-RUN]", " ".join(cmd))
    else:
        subprocess.run(cmd, check=True)

def remove_peer(iface, pubkey, dry_run=False):
    """
    Удаляет peer из рантайма WireGuard
    """
    cmd = ["wg", "set", iface, "peer", pubkey, "remove"]
    if dry_run:
        print("[DRY-RUN]", " ".join(cmd))
    else:
        subprocess.run(cmd, check=True)

def update_allowed_ips(iface, pubkey, ip, dry_run=False):
    """
    Меняет AllowedIPs для существующего peer
    """
    cmd = ["wg", "set", iface, "peer", pubkey, "allowed-ips", f"{ip}/32"]
    if dry_run:
        print("[DRY-RUN]", " ".join(cmd))
    else:
        subprocess.run(cmd, check=True)
