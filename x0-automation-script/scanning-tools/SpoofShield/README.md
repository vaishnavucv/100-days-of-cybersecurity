# 🚨 SpoofShield - ARP Spoofing Detection Tool 🔥

```
  ___|                     _| ___|  |    _)      |     | 
\___ \  __ \   _ \   _ \  | \___ \  __ \  |  _ \ |  _` | 
      | |   | (   | (   | __|     | | | | |  __/ | (   | 
_____/  .__/ \___/ \___/ _| _____/ _| |_|_|\___|_|\__,_| 
       _|  
```

## 🛡️ Overview
**SpoofShield** is a powerful ARP spoofing detection tool that keeps your network safe from MITM (Man-in-the-Middle) attacks. It scans your network, detects ARP anomalies, and alerts you on **Discord** when it finds something shady! 🕵️‍♂️


## ⚡ Features
✅ Real-time ARP table scanning 🔄  
✅ Detects ARP spoofing attacks 🕶️  
✅ Sends instant alerts to **Discord** 🚀  
✅ Works on **Windows** 🖥️  
✅ Customizable scan intervals ⏳  

## 🔧 Requirements
- **Python 3.x** 🐍
- `requests` module (for Discord alerts) 🌐

## 📥 Installation
1️⃣ Clone the repo:
   ```bash
   git clone git clone https://github.com/c1ph3r-1337/spoofshield.git
   cd spoofshield
   ```
2️⃣ Install dependencies:
   ```bash
   pip install requests
   ```

## ⚙️ Configuration
Edit the script to set up your **Discord webhook & network settings**:

🔹 **WEBHOOK_URL** → Replace with your **Discord Webhook URL** 🎯  
🔹 **SUBNET_PREFIX** → Set the subnet to **monitor** (default: `192.168.130.`) 🌍  
🔹 **SCAN_INTERVAL** → Adjust scanning frequency (default: `60` seconds) ⏰  

Example config inside `main.py`:
```python
WEBHOOK_URL = "your_discord_webhook_url"
SUBNET_PREFIX = "192.168.130." 
SCAN_INTERVAL = 60  # Seconds between scans
```

## 🚀 Usage
Run **SpoofShield** like a pro:
```bash
python main.py
```
It will **continuously monitor** your ARP table and send 🔔 **alerts** if it detects spoofing! 👀

## 🕵️‍♂️ How It Works
1️⃣ Fetches the **ARP table** using `arp -a` 🗂️  
2️⃣ Parses the ARP table for **IP-MAC** pairs 📊  
3️⃣ Filters results for your **subnet** 🌍  
4️⃣ Detects if multiple **IP addresses** share the same MAC 🚨  
5️⃣ Sends an **alert to Discord** if spoofing is detected! ⚠️  

## 📢 Example Discord Alert
```
📋 **ARP Table (192.168.130.0/24):**
```
```plaintext
192.168.130.1    58:11:22:e0:67:4f    dynamic
192.168.130.5    58:11:22:e0:67:4f    dynamic
```

🔔 **ALERT: Possible ARP spoofing detected!** 🚨  
**Multiple IPs share the same MAC!**
```

## 📜 License
🚀 **SpoofShield** is open-source and available under the **MIT License**. 

## 💻 Contribution
Pull requests are **welcome**! Feel free to submit **issues & PRs** to improve **SpoofShield**! 🔥

## ⚠️ Disclaimer
🛑 **For educational & security purposes only!** Ensure you have **permission** to scan the network you're monitoring! 🚫

