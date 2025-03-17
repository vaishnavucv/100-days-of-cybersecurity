import subprocess
import time
import re
import requests


def print_banner():
    banner = r"""
  ___|                     _| ___|  |    _)      |     | 
\___ \  __ \   _ \   _ \  | \___ \  __ \  |  _ \ |  _` | 
      | |   | (   | (   | __|     | | | | |  __/ | (   | 
_____/  .__/ \___/ \___/ _| _____/ _| |_|_|\___|_|\__,_| 
       _|                                                
    """
    print(banner)
    print("🚨 SpoofShield - ARP Spoofing Detection Tool 🔥")
    print("Made by c1ph3r1337 😎🔥\n")

# Configuration
WEBHOOK_URL = "webhook_url"  # Replace with your actual webhook URL
SUBNET_PREFIX = "192.168.1."
GATEWAY_IP = "192.168.1.1"  # IP to compare for spoofing checks
SCAN_INTERVAL = 60          # Seconds between scans

def get_arp_table():
    """
    Run the 'arp -a' command and return its output as a string.
    """
    try:
        result = subprocess.run(["arp", "-a"], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error executing arp -a:", e)
        return ""

def parse_arp_entries(arp_output):
    """
    Parse the ARP table output from 'arp -a' into a structured list of dicts.
    Each entry is of the form:
        {
          'interface': 'Interface: 192.168.1.10 --- 0x13',
          'ip': '192.168.1.1',
          'mac': '58-11-22-e0-67-4f' or '58:11:22:e0:67:4f',
          'line': 'Raw line from arp -a'
        }
    """
    lines = arp_output.splitlines()
    entries = []
    current_interface = None

    for line in lines:
        line = line.strip()
        if line.startswith("Interface:"):
            # Windows ARP often shows lines like: "Interface: 192.168.1.10 --- 0x13"
            current_interface = line
            continue

        # Skip headers or blank lines
        if line.startswith("Internet Address") or not line:
            continue

        # Two common ARP output formats:

        # 1) Windows format:
        #    192.168.1.10       00-50-56-c0-00-08     dynamic
        win_match = re.match(r"^(\d+\.\d+\.\d+\.\d+)\s+([\da-fA-F:-]+)\s+(\w+)", line)

        # 2) Linux/macOS format:
        #    ? (192.168.1.1) at 58:11:22:e0:67:4f [ether] on eth0
        #    or "192.168.1.1 dev eth0 lladdr 58:11:22:e0:67:4f STALE" on some systems
        #    We'll try a simple pattern for the typical "at" style.
        nix_match = re.match(r"^\S+\s+\((\d+\.\d+\.\d+\.\d+)\)\s+at\s+([0-9a-fA-F:]+)", line)

        if win_match:
            ip_addr = win_match.group(1)
            mac_addr = win_match.group(2)
            entries.append({
                'interface': current_interface,
                'ip': ip_addr,
                'mac': mac_addr,
                'line': line
            })
        elif nix_match:
            ip_addr = nix_match.group(1)
            mac_addr = nix_match.group(2)
            entries.append({
                'interface': current_interface,
                'ip': ip_addr,
                'mac': mac_addr,
                'line': line
            })

    return entries

def filter_by_subnet(entries, subnet_prefix):
    """
    Filter the parsed ARP entries so we only keep those where the IP starts with SUBNET_PREFIX.
    Returns a dictionary grouped by interface, e.g.:
      {
        'Interface: 192.168.1.10 --- 0x13': [
            { 'ip': '192.168.1.2', 'mac': '00-50-56-c0-00-08', ... },
            ...
        ],
        ...
      }
    """
    grouped = {}
    for entry in entries:
        ip_addr = entry['ip']
        if ip_addr.startswith(subnet_prefix):
            iface = entry['interface']
            if iface not in grouped:
                grouped[iface] = []
            grouped[iface].append(entry)
    return grouped

def check_arp_spoofing(entries, gateway_ip):
    """
    Check if any IP other than `gateway_ip` has the same MAC as `gateway_ip`.
    Return True if spoofing is detected, False otherwise.
    """
    # Build a map of IP -> MAC
    ip_mac = { e['ip']: e['mac'].lower() for e in entries }
    if gateway_ip in ip_mac:
        gateway_mac = ip_mac[gateway_ip]
        # Compare every other IP's MAC
        for ip, mac in ip_mac.items():
            if ip != gateway_ip and mac == gateway_mac:
                return True
    return False

def format_arp_output(grouped_entries):
    """
    Format the ARP entries grouped by interface into a multiline string
    that can be placed inside a Discord code block.
    """
    lines = []
    for iface, entries in grouped_entries.items():
        if not entries:
            continue
        # Only show the interface line if it actually has entries in the desired subnet
        lines.append(iface)
        for e in entries:
            lines.append(e['line'])
    return "\n".join(lines)

def send_discord_notification(message):
    """
    Send the message to Discord using the webhook.
    """
    payload = {'content': message}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code not in [200, 204]:
            print(f"Failed to send notification: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending Discord notification: {e}")

def main():
    while True:
        arp_output = get_arp_table()
        if not arp_output:
            print("Failed to retrieve ARP table.")
        else:
            # Parse all ARP entries
            entries = parse_arp_entries(arp_output)
            # Filter for 192.168.1.x only
            grouped = filter_by_subnet(entries, SUBNET_PREFIX)

            # Flatten filtered entries to check for spoofing
            all_filtered = []
            for e_list in grouped.values():
                all_filtered.extend(e_list)

            # Check for ARP spoofing
            spoofing_detected = check_arp_spoofing(all_filtered, GATEWAY_IP)

            # Build the output message
            formatted_output = format_arp_output(grouped)
            if not formatted_output.strip():
                message = f"No ARP entries found for subnet {SUBNET_PREFIX}0/24."
            else:
                message = f"📋 **ARP Table ({SUBNET_PREFIX}0/24):**\n```{formatted_output}```"

            if spoofing_detected:
                message += "\n\n**🔔ALERT: Possible ARP spoofing detected!** " \
                           "Another IP shares the same MAC as the gateway."

            # Send to Discord
            send_discord_notification(message)
            print("Sent ARP table to Discord.")

        print(f"Waiting {SCAN_INTERVAL} seconds before next scan...\n")
        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    main()
