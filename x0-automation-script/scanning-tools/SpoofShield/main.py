import subprocess
import time
import re
import requests
from datetime import datetime

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
WEBHOOK_URL = "your_webhook_url"  # Replace with actual webhook URL
SUBNET_PREFIX = "192.168.130."  # This filters for 192.168.130.0/24
SCAN_INTERVAL = 60  # Scan interval in seconds

def get_arp_table():
    """
    Run the 'arp -a' command and return its output as a string.
    """
    try:
        result = subprocess.run(["arp", "-a"], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error executing 'arp -a':", e.stderr)
        return ""

def parse_arp_table(output, subnet_prefix=SUBNET_PREFIX):
    """
    Parse the ARP table output and extract IP and MAC addresses.
    Returns a list of dictionaries containing the IP, MAC, and Type.
    """
    lines = output.splitlines()
    arp_entries = []
    
    for line in lines:
        line = line.strip()
        
        # Skip headers and empty lines
        if line.startswith("Interface:") or line.startswith("Internet Address") or not line:
            continue
        
        # Extract IP, MAC, and Type
        ip_match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)
        mac_match = re.search(r"([0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2})", line)
        type_match = re.search(r"(static|dynamic)", line, re.IGNORECASE)
        
        if ip_match and mac_match:
            ip_addr = ip_match.group(1)
            if ip_addr.startswith(subnet_prefix):
                arp_entries.append({
                    "ip": ip_addr,
                    "mac": mac_match.group(1).replace(":", "-").lower(),  # Normalize MAC format
                    "type": type_match.group(1) if type_match else "unknown"
                })
    
    return arp_entries

def detect_arp_spoofing(arp_entries):
    """
    Detect potential ARP spoofing by finding duplicate MAC addresses.
    Returns a dictionary of MAC addresses with their associated IPs.
    """
    mac_to_ips = {}
    for entry in arp_entries:
        mac = entry["mac"]
        ip = entry["ip"]
        
        if mac in mac_to_ips:
            mac_to_ips[mac].append(ip)
        else:
            mac_to_ips[mac] = [ip]
    
    # Filter for MAC addresses that are associated with more than one IP
    suspicious_macs = {mac: ips for mac, ips in mac_to_ips.items() if len(ips) > 1 and "255" not in ips[0]}
    
    return suspicious_macs

def format_arp_table(arp_entries):
    """
    Format the ARP table entries into a readable string table.
    """
    if not arp_entries:
        return "No ARP entries found for subnet 192.168.130.0/24."
    
    table = "IP Address      MAC Address           Type\n"
    table += "--------------------------------------------------\n"
    
    for entry in arp_entries:
        table += f"{entry['ip']:<15} {entry['mac']:<20} {entry['type']}\n"
    
    return table

def send_discord_notification(message):
    """
    Send the message to Discord using the webhook.
    """
    payload = {'content': message}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code not in [200, 204]:
            print(f"Failed to send notification: {response.status_code} - {response.text}")
        else:
            print("Successfully sent notification to Discord.")
    except Exception as e:
        print(f"Error sending Discord notification: {e}")

def main():
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arp_output = get_arp_table()
        
        if arp_output:
            arp_entries = parse_arp_table(arp_output)
            formatted_table = format_arp_table(arp_entries)
            suspicious_macs = detect_arp_spoofing(arp_entries)
            
            if suspicious_macs:
                # Format the alert for potential ARP spoofing
                for mac, ips in suspicious_macs.items():
                    # Find the gateway IP (assuming it's x.x.x.1)
                    gateway_ip = next((ip for ip in ips if ip.endswith(".1")), None)
                    if gateway_ip:
                        other_ips = [ip for ip in ips if ip != gateway_ip]
                        alert_message = (
                            f"**🚨 ALERT: ARP SPOOFING DETECTED!**\n"
                            f"Suspicious IPs sharing gateway MAC: {', '.join(other_ips)}\n"
                            f"Gateway IP: {gateway_ip}\n"
                            f"Timestamp: {timestamp}\n"
                            f"**ARP Table:**\n\n```\n{formatted_table}```"
                        )
                        send_discord_notification(alert_message)
                    else:
                        alert_message = (
                            f"**🚨 ALERT: Potential ARP SPOOFING DETECTED!**\n"
                            f"Multiple IPs sharing MAC address {mac}: {', '.join(ips)}\n"
                            f"Timestamp: {timestamp}\n"
                            f"**ARP Table:**\n\n```\n{formatted_table}```"
                        )
                        send_discord_notification(alert_message)
            else:
                # Normal update  
                update_message = (
                    f"**🔍 Network Monitor Update**\n"
                    f"Scan completed at: {timestamp}\n"
                    f"Devices detected: {len(arp_entries)}\n"
                    f"Status: Normal - No spoofing detected\n"
                    f"**ARP Table:**\n\n```\n{formatted_table}```"
                )
                send_discord_notification(update_message)
        else:
            print("Failed to retrieve ARP table.")
                
        print(f"Scan completed at {timestamp}. Waiting {SCAN_INTERVAL} seconds before next scan...\n")
        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    print_banner()  # Show banner on startup
    print("ARP Spoofing Detector started. Monitoring network...\n")
    main()
