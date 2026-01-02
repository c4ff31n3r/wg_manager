# wg_manager

Simple WireGuard client manager. Manages clients, keys, and configuration securely. Root-only utility.

## Features

- Issue new WireGuard clients
- Revoke or recreate client keys
- Edit client metadata
- Import existing peers from server config
- List all clients
- Logs all actions

## Dependencies

- Linux or FreeBSD
- wg, wg-quick
- Python >=3.8
- PyYAML 6.0.3
- pipx
- Root privileges

---

## Installation

1. Clone repository:

    ```bash
    git clone https://github.com/c4ff31n3r/wg_manager.git
    cd wg_manager
    ```

2. Install system-wide:

    using pipx >=1.5.0:
    ```bash
    sudo pipx ensurepath --global
    sudo pipx install --global .
    ```
 
    using pipx <1.5.0:
    ```bash
    echo 'export PATH="$PATH:/usr/local/bin"' | sudo tee /etc/profile.d/pipx-global.sh
    sudo PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin PIPX_MAN_DIR=/usr/local/share/man pipx install .
    ```

Test installation:

```bash
wg_manager
```

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

## Updating

When you have a new version in your local repository, update the global installation with:

```bash
cd /path/to/wg_manager
git pull origin master
sudo pipx upgrade --global .
```

## Uninstallation

```bash
sudo pipx uninstall wg_manager
```

## License

GNU GPL v3
