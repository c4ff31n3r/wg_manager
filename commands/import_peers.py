from wg_config import import_peers_from_config
from storage import ClientStore

def run(store: ClientStore):
    import_peers_from_config(store)
    print("Imported peers from wg0.conf")
