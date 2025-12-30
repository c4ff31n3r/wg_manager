#!/usr/bin/env python3

import os
import sys
from utils import die, ensure_dirs
from config import DB_FILE, LOG_FILE
from storage import ClientStore

from commands import issue, revoke, recreate, edit, list as list_cmd, import_peers

def help():
    print(f"""
--- WG Manager v 2.1 ---

wg_manager commands:

  issue               create new client
  revoke USER         revoke client
  recreate USER       regenerate keys
  edit USER           edit metadata
  list                list clients
  import              import peers from WireGuard config
""")

if __name__ == "__main__":
    if os.geteuid() != 0:
        die("Run as root")

    # Create DB/LOG dirs and files, if not present
    ensure_dirs({
        DB_FILE: {"clients": {}},
        LOG_FILE: {"logs": []}
    })

    store = ClientStore(DB_FILE)

    if len(sys.argv) < 2:
        help()
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd == "issue":
        issue.run(store)
    elif cmd == "revoke" and args:
        revoke.run(store, args[0])
    elif cmd == "recreate" and args:
        recreate.run(store, args[0])
    elif cmd == "edit" and args:
        edit.run(store, args[0])
    elif cmd == "list":
        list_cmd.run(store)
    elif cmd == "import":
        import_peers.run(store)
    else:
        help()
