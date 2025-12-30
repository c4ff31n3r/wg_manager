from utils import load_yaml, save_yaml

class ClientStore:
    def __init__(self, db_file):
        self.db_file = db_file
        self.data = load_yaml(db_file, {"clients": {}})

    def save(self):
        save_yaml(self.db_file, self.data)

    def get(self, username):
        return self.data["clients"].get(username)

    def add(self, username, client_data):
        """
        Adds a new client
        client_data: dict with keys: ip, pubkey, privkey, status, client_os, purpose, allowed
        """
        self.data["clients"][username] = client_data
        self.save()

    def revoke(self, username):
        """
        Marks client as revoked
        """
        client = self.get(username)
        if client:
            client["status"] = "revoked"
            self.save()
        return client

    def update(self, username, update_data):
        """
        Updates fields of an existing client
        """
        client = self.get(username)
        if not client:
            return None
        client.update(update_data)
        self.save()
        return client

    def all_clients(self):
        return self.data["clients"]
