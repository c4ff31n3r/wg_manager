# wg_manager

Utility for managing WireGuard clients.

## Features

- **issue** — create new client
- **revoke USER** — revoke a client
- **recreate USER** — regenerate client keys
- **edit USER** — edit client metadata (IP, OS, Purpose, AllowedIPs)
- **list** — list all clients
- **import** — import peers from an existing WireGuard server configuration file

---

## Installation

1. Clone repository:
```bash
git clone <URL_REPO>
cd wg_manager
```

2. Make executable:
```bash
chmod +x main.py
```

3. Install system-wide:
```bash
sudo ./install.sh
```

Test:
```bash
wg_manager
```

---

## Uninstallation
```bash
sudo ./uninstall.sh
```

---

## Usage

Run `wg_manager` followed by the command. Examples:
```bash
sudo wg_manager issue
sudo wg_manager revoke john_doe
sudo wg_manager recreate john_doe
sudo wg_manager edit john_doe
sudo wg_manager list
sudo wg_manager import
```
