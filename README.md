# Update /etc/hosts Python Script

## Overview

This Python script allows you to add or update IP and hostname entries in the `/etc/hosts` file on a Linux-based system. If the given IP address already exists in the file, the new hostname will be appended next to the existing ones for that IP. If the IP address is not found, a new entry is added.

## Requirements

- Python 3.x
- Superuser (root) access is required to modify `/etc/hosts`

## Usage

1. Save the Python script as `update_hosts.py`.

2. Run the script as superuser:

    ```bash
    sudo python3 update_hosts.py [IP_ADDRESS] [HOSTNAME]
    ```

    Replace `[IP_ADDRESS]` and `[HOSTNAME]` with the IP address and hostname you wish to add or update. For example:

    ```bash
    sudo python3 update_hosts.py 192.168.1.2 test.htb
    ```

## Examples

### Before Running the Script
Suppose the `/etc/hosts` file initially contains the following:

```
127.0.0.1 localhost
192.168.1.2 api.htb
```

### After Running the Script
After running `sudo python3 update_hosts.py 192.168.1.2 test.htb`, the `/etc/hosts` file will be updated to:

```
127.0.0.1 localhost
192.168.1.2 api.htb test.htb
```

## Note

Modifying `/etc/hosts` is a sensitive operation that could potentially disrupt network services if not done correctly. Use this script at your own risk and ensure you understand the implications of modifying `/etc/hosts`.