import sys

def update_etc_hosts(ip, hostname):
    lines = []
    ip_found = False

    try:
        with open('/etc/hosts', 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading /etc/hosts: {e}")
        return

    for index, line in enumerate(lines):
        # Stripping leading/trailing whitespaces and splitting fields by whitespace
        tokens = line.strip().split()

        if len(tokens) > 1 and tokens[0] == ip:
            if hostname not in tokens[1:]:
                # Append new hostname to existing IP address line
                lines[index] = line.strip() + ' ' + hostname + '\n'
            ip_found = True
            break

    if not ip_found:
        # Append a new line for the new IP address and hostname
        lines.append(f"{ip} {hostname}\n")

    try:
        with open('/etc/hosts', 'w') as f:
            f.writelines(lines)
    except Exception as e:
        print(f"Error writing to /etc/hosts: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 update_hosts.py [IP_ADDRESS] [HOSTNAME]")
    else:
        ip_address = sys.argv[1]
        hostname = sys.argv[2]
        update_etc_hosts(ip_address, hostname)
