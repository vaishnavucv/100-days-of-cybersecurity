# Lab Setup for Cybersecurity

This repository provides step-by-step instructions to set up a cybersecurity lab for learning, experimentation, and research. The lab setup includes guidance for installing VirtualBox, downloading virtual machine (VM) files for Kali Linux, and creating your own Xubuntu or Ubuntu MATE VMs. 

## Prerequisites

1. A computer with at least:
   - **Processor**: 64-bit capable CPU
   - **RAM**: 8 GB (minimum)
   - **Storage**: 50 GB free space
   - **Virtualization**: Enabled in BIOS/UEFI

2. A stable internet connection.

---

## Steps to Set Up Your Lab

### 1. Install VirtualBox

VirtualBox is an open-source virtualization tool that allows you to run multiple operating systems on your computer.

- **Download VirtualBox:**  
  [Download VirtualBox (Windows Version)](https://download.virtualbox.org/virtualbox/7.0.18/VirtualBox-7.0.18-162988-Win.exe)

- **Installation Instructions:**
  1. Run the installer.
  2. Follow the installation wizard prompts.
  3. Ensure you select the option to install the VirtualBox Network Adapter.

---

### 2. Download Kali Linux VM
>[!NOTE]
> Kali Linux is a popular Linux distribution used by cybersecurity professionals. However, it is not recommended for beginners. For working professionals, you can download the prebuilt VM:

- **Download:**  
  [Kali Linux for VirtualBox](https://cdimage.kali.org/kali-2024.4/kali-linux-2024.4-virtualbox-amd64.7z)

- **Steps to Set Up Kali Linux VM:**
  1. Download and extract the VM file using software like [7-Zip](https://www.7-zip.org/).
  2. Open VirtualBox and import the VM file:
     - Go to **File > Import Appliance**.
     - Select the `.ova` file and follow the prompts.
  3. Start the VM to launch Kali Linux.

>[!WARNING]
> Kali Linux is designed for advanced users and professionals. Beginners are encouraged to use Xubuntu or Ubuntu MATE instead.

---

### 3. Create Your Own VM

You can create your own virtual machine using Xubuntu or Ubuntu MATE. These are lightweight Linux distributions suitable for beginners in cybersecurity.

#### Option 1: Xubuntu

- **Download Xubuntu ISO:**  
  [Xubuntu Official Website](https://xubuntu.org/)

- **Steps to Create a Xubuntu VM:**
  1. Open VirtualBox and click **New** to create a new VM.
  2. Name your VM and select **Linux** as the type and **Ubuntu (64-bit)** as the version.
  3. Allocate at least **2 GB RAM** and **20 GB storage**.
  4. Attach the downloaded ISO:
     - Go to **Settings > Storage**.
     - Add the ISO under **Controller: IDE**.
  5. Start the VM and follow the on-screen installation prompts.

#### Option 2: Ubuntu MATE

- **Download Ubuntu MATE ISO:**  
  [Ubuntu MATE Official Website](https://ubuntu-mate.org/)

- **Steps to Create an Ubuntu MATE VM:**
  1. Follow the same steps as for Xubuntu, replacing the ISO file with the Ubuntu MATE ISO.

---

### 4. General Tips for Beginners

- Begin with **Xubuntu** or **Ubuntu MATE** to familiarize yourself with Linux commands and the environment.
- **Avoid starting directly with Kali Linux, as it is tailored for advanced tasks and may be overwhelming for beginners**.

---

## Feedback and Contribution

If you encounter issues or have suggestions for improving this guide, please feel free to open an issue or submit a pull request.

---

## 📬 Community Support & Updates

Need help or support during the challenge? Connect with the community and stay updated via the following platforms:

### Join the Discussion
- **Discord (Main Source of Support)**: [discord.gg/bFkdWjgCdF](https://discord.gg/bFkdWjgCdF) 🎮

### Stay Updated
- **Instagram**:
  - [@hack_with_vyshu](https://Instagram.com/hack_with_vyshu) 📸
  - [@thecyberrange](https://www.instagram.com/thecyberrange/) 📸
  - [@realsector21](https://www.instagram.com/realsector21/) 📸
- **LinkedIn**:
  - [Vaishnavu C V](https://www.linkedin.com/in/vaishnavucv/) 💼

## 🌍 Spread the Word!

Let’s inspire more learners to join the **100 Days of Cybersecurity** challenge! Share your journey on social media:
- Take screenshots of your daily progress.
- Use the hashtag **#100DaysOfCybersecurity**.
- Tag our accounts so we can cheer you on!

### Example Post:
```
🚀 I’m taking the **100 Days of Cybersecurity** challenge! 💻  
Day [X]: [Brief Description of What You Learned]  
#100DaysOfCybersecurity #Cybersecurity #ethicalhacking
```
---

Start your cybersecurity journey today and join a growing community of learners and professionals passionate about making a difference in the world of cybersecurity.

Happy Learning! 🚀
