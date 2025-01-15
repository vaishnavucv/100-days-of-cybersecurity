>[!WARNING]
Images used in this file are not owned or made by me and are copied from internet. The Sources of the image have been provided below. The document is completely for educational and illustrational purposes only.

# OBJECTIVES
- Learn core concepts of how computers communicate with each other

# SYNOPSIS
1. **INTRODUCTION**
2. What is **INTERNET**
3. IDENTIFYING DEVICES ON A NETWORK
- a. **IP ADDRESS**
- b. **MAC ADDRESS**
\
\
# 1. INTRODUCTION
---
A **NETWORK** consists of 2 or more computers linked to share resources. These devices include everything from your laptop and phone to security cameras, traffic lights, and even farming.   They are the basis of communication in IT. Networks are integrated into our everyday life. Because networks are so embedded in modern-day, networking is an essential concept in Cyber Security. 

> [!NOTE]
> **COMPUTER NETWORK** 
> SET OF COMPUTERS THAT ARE CONNECTED TOGETHER SO AS TO SHARE INFORMATION


![Images](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115222650.png)**Source : Britannica**

The **INTERNET** is made up of **MANY SMALL NETWORKS** joined together. 
- These small networks are called **PRIVATE NETWORKS**.
- The networks connecting these small networks are called **PUBLIC NETWORKS**

# 3. IDENTIFYING DEVICES ON A NETWORK
***
To communicate and maintain order, devices must be **BOTH IDENTIFYING AND IDENTIFIABLE** on a network. Devices on a network are very similar to humans in the fact that we have two ways of being identified **Our Name** **Our Fingerprints**.

We can change our name through deed poll, but we can't, change our fingerprints. Every human has an individual set of fingerprints which means that even if they change their name, there is still an identity behind it. Devices have the same thing: two means of identification, with one being permeable. They are **IP Address** and **Media Access Control (MAC) Address**

## 3. a. IP ADDRESSES
---
IP address (or **I**nternet **P**rotocol) address can be used as a way of identifying a host on a network for a period of time, where that IP address can then be associated with another device without the IP address changing.

![Images](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115224629.png)
**Source : HOSTWINDS**


An **IP ADDRESS** is a set of numbers that are divided into four octets. The value of each octet will summarise to be the IP address of the device on the network. This number is calculated through a technique known as **IP ADDRESSING & SUBNETTING**. IP addresses can change from device to device but cannot be active simultaneously more than once within the same network. 

IP Addresses follow a set of standards known as protocols. These protocols are the backbone of networking and force many devices to communicate in the same language. 

A device can be on both a private and public network. Depending on where they are will determine what type of IP address they have: 

- **GLOBAL or PUBLIC or EXTERNAL IP ADDRESS** : Identify the device on the Internet. This group can also be called 'WAN addresses' .
- **PRIVATE or LOCAL or INTERNAL IP ADDRESS** : Identify a device amongst other devices. These are used in the local network (LAN). They are not routed on the Internet and no traffic can be sent to them from the Internet, they only supposed to work within the local network


![Images](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115225243.png)
**SOURCE : GEOTARGETLY**

> [!Note]
> An **Internet Protocol Address (IP ADDRESS)** is a unique address that identifies a device on the internet or a local network. IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network

![Images](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115230725.png)
**Source : Tryhackme**, not my real IP or MAC Address!

These two devices will be able to use their private IP addresses to communicate with each other. However, any data sent to the Internet from either of these devices will be identified by the same public IP address. Public IP addresses are given by your **I**nternet **S**ervice **P**rovider (or **ISP**) at a monthly fee (your bill!).

As more and more devices become connected, it is becoming increasingly harder to get a public address that isn't already in use. Cisco, an industry giant in the world of networking, estimated that there would be approximately 50 billion devices connected on the Internet by the end of 2021. 

We have only discussed one version of the Internet Protocol addressing scheme known as IPv4, which uses a numbering system of 2^32 IP addresses (4.29 billion), still there will be a shortage!

IPv6 is a new iteration of the Internet Protocol addressing scheme to help tackle this issue. It supports up to 2^128 of IP addresses (340 trillion-plus), resolving the issues faced with IPv4 and is more efficient due to new methodologies.

## IPv4
---
![Images](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115231813.png)
**Source : Tryhackme**, not my real IP or MAC Address!

## IPv6
----
![Images](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115232224.png)
**Source : Tryhackme**, not my real IP Address!

## IPv4 vs IPv6
---
![Images](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115232533.png)
**Source : AVAST**

## Check your local IP address
---
If you are using Linux or MacOS you can open your terminal and type 
```bash 
ifconfig
```

For Windows machine you can open up the cmd prompt or powershell, then type 
```Powershell
ipconfig /all
```

>[!ifconfig]
![Images](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115235710.png)
>**Source : Internet**

![Images](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115235335.png)
### ``inet``  
---
```inet``` (Internet protocol family) show the local IP address

``` bash
	inet 192.168.1.54  netmask 255.255.255.0  broadcast 192.168.1.255  
```

-    This is IP version 4 (IPv4) Using 32-bit decimal number
-    inet IPv4 : ``192.168.1.54``


```bash
	inet6 fe80::a163:b52c:c585:7a47  prefixlen 64  scopeid 0x20<link>  
```

- This is new version of IP (IPv6), using 128 bits hexadecimal value
- inet IPv6 : ``fe80::a163:b52c:c585:7a47``

###  `ether` 
---
For the net-tools version typically found on Linux, the word `ether` is the _hardware class_, and the value following that is the hardware address. For the "Ethernet" hardware class the address is the card's MAC address. `ifconfig` shows the current hardware address of the interface, with its hardware class. For Ethernet interfaces, the class is `ether` and the hardware address is the MAC address.

## IPv4 Calculation
---
```Calculation
IPv4 = 32 bits range(4 octets of 8 bits from 0-255 each(4))
11000000.10101000.00000001.00110110        [IPv4 BINARY]
   192  .   168  .   1    .   54           [IPv4 DECIMAL]
```


```Calculation
  1   1   1   1   1   1   1   1
  |   |   |   |   |   |   |   |
(128 +64 +32 +16 +8  +4  +2  +1) --> 255 
Example of octet conversion:
IP Address: 192.168.1.54
To calculate the first octet (192.), from binary format to decimal:
128  64  32  16  8   4   2   1         
 |   |   |   |   |   |   |   |
 1   1   0   0   0   0   0   0          
 |   |   |   |   |   |   |   |
128+ 64+ 0+  0+  0+  0+  0+  0 = 192   final value (firt octet IPv4 in decimal)
```

- Take the IP: `192.168.64.3`
- The first octet `192` in 8-bit binary is `11000000`.
- Only the `8th` and `7th` bit is on and the rest of them (`6th to 1st bit`) is off, meaning the decimal value is the final sum of these values: `128 + 64 = 192`

## 3. b. MAC ADDRESSES
---
