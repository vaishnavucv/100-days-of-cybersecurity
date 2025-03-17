# ARP Spoofing Detection Tool

## Overview
This tool monitors the local network for ARP spoofing attacks by analyzing the ARP table and checking if multiple IP addresses share the same MAC address as the gateway. If suspicious activity is detected, it sends an alert to a Discord webhook.

## Features
- Periodically scans the ARP table for anomalies.
- Detects ARP spoofing attacks by checking for duplicate MAC addresses.
- Sends alerts to a Discord webhook when spoofing is detected.
- Supports both Windows and Linux/macOS ARP table formats.

## Requirements
- Python 3.x
- `requests` module (for sending alerts to Discord)

## Installation
1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/yourrepo/arp-spoof-detector.git
   cd arp-spoof-detector
   ```
2. Install the required dependencies:
   ```bash
   pip install requests
   ```

## Configuration
Modify the script to set up your Discord webhook and network settings:
- **`WEBHOOK_URL`**: Replace with your Discord webhook URL.
- **`SUBNET_PREFIX`**: Set the subnet to monitor (default: `192.168.1.`).
- **`GATEWAY_IP`**: Set your router's IP address (default: `192.168.1.1`).
- **`SCAN_INTERVAL`**: Adjust the scanning frequency (default: `60` seconds).

Example configuration in the script:
```python
WEBHOOK_URL = "your_discord_webhook_url"
SUBNET_PREFIX = "192.168.1."
GATEWAY_IP = "192.168.1.1"
SCAN_INTERVAL = 60  # Seconds between scans
```

## Usage
Run the script using:
```bash
python arp_spoof_detector.py
```
The tool will continuously monitor the ARP table and send notifications to Discord when suspicious activity is detected.

## How It Works
1. Retrieves the ARP table using `arp -a`.
2. Parses the ARP table to extract IP-MAC pairs.
3. Filters the results based on the subnet.
4. Detects if multiple IPs are associated with the same MAC as the gateway.
5. Sends alerts to Discord if spoofing is detected.

## Example Discord Alert
```
📋 **ARP Table (192.168.1.0/24):**
```plaintext
192.168.1.1    58:11:22:e0:67:4f    dynamic
192.168.1.5    58:11:22:e0:67:4f    dynamic
```

🔔 **ALERT: Possible ARP spoofing detected!** Another IP shares the same MAC as the gateway.
```

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contribution
Feel free to contribute by submitting pull requests or reporting issues!

## Disclaimer
This tool is for educational and security monitoring purposes only. Use it responsibly and ensure you have permission to monitor the network you are scanning.
