# wg_manager

Simple WireGuard client manager. Manages clients, keys, and configuration securely. Root-only utility.

## Features

- Issue new WireGuard clients
- Revoke or recreate client keys
- Edit client metadata
- Import existing peers from server config
- List all clients
- Logs all actions

---

## Installation

1. Clone repository:

    ```bash
    git clone <URL_REPO>
    cd wg_manager
    ```

2. Install system-wide:

    ```bash
    sudo ./install.sh
    ```

Test installation:

    ```bash
    wg_manager
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

---

## Uninstallation

    ```bash
    sudo ./uninstall.sh
    ```

**Notes:**

- Uninstaller **does not automatically delete data or code directories**.
- Code: `/usr/lib/wg_manager`
- Data: `/etc/wg_manager`
- Remove manually if needed:

    ```bash
    sudo rm -rf /usr/lib/wg_manager
    sudo rm -rf /etc/wg_manager
    ```

---

## License

GNU GPL v3
