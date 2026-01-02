from wg_manager.utils import die, ensure_dirs
from wg_manager.config import DB_FILE, LOG_FILE
from wg_manager.storage import ClientStore

from . import issue, revoke, recreate, edit, list as list_cmd, import_peers


def help():
    print("""
--- WG Manager ---

Commands:
  issue
  revoke USER
  recreate USER
  edit USER
  list
  import
""")


def run(args):
    import os

    if os.geteuid() != 0:
        die("wg_manager must be run as root")

    ensure_dirs({
        DB_FILE: {"clients": {}},
        LOG_FILE: {"logs": []}
    })

    store = ClientStore(DB_FILE)

    if not args:
        help()
        return

    cmd = args[0]
    rest = args[1:]

    if cmd == "issue":
        issue.run(store)
    elif cmd == "revoke" and rest:
        revoke.run(store, rest[0])
    elif cmd == "recreate" and rest:
        recreate.run(store, rest[0])
    elif cmd == "edit" and rest:
        edit.run(store, rest[0])
    elif cmd == "list":
        list_cmd.run(store)
    elif cmd == "import":
        import_peers.run(store)
    else:
        help()
