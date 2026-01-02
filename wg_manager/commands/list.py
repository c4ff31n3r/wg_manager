def run(store):
    clients = store.all_clients()
    if not clients:
        print("No clients found")
        return

    print(f"{'Username':15} {'IP':15} {'Status':10}")
    print("-" * 45)
    for u, c in clients.items():
        print(f"{u:15} {c.get('ip',''):15} {c.get('status',''):10}")
