>[!WARNING]
Images used in this file are not owned or made by me and are copied from internet. The Sources of the image have been provided below. The document is completely for educational and illustrational purposes only.
 
# OBJECTIVES
- Learn core concepts of how computers communicate with each other
- Deeply understand each Concepts

# SYNOPSIS
1. **INTRODUCTION**
2. What is **INTERNET**
3. Types of **NETWORK**
4. Common Terms in Networking
5. IDENTIFYING DEVICES ON A NETWORK
	a. **IP ADDRESS**
	b. **MAC ADDRESS**
6. **PING (ICMP)**
7. **TOPOLOGIES** 
8. **SWITCH**
9. **ROUTER**
10. **SUBNETTING**
11. **ARP**
12. **DHCP**
13. **OSI MODEL**
14. **PACKETS AND FRAMES**
15. **TCP/IP THREE-WAY HANDSHAKE**
16. **UDP/IP**
17. **PORTS**
18. **PORT FORWARDING**
19. **FIREWALLS**
20. **VPN**
21. **DNS**
	

# 1. INTRODUCTION
---
A **NETWORK** consists of 2 or more computers linked to share resources. These devices include everything from your laptop and phone to security cameras, traffic lights, and even farming.   They are the basis of communication in IT. Networks are integrated into our everyday life. Because networks are so embedded in modern-day, networking is an essential concept in Cyber Security.

> [!NOTE]
> **COMPUTER NETWORK** 
> SET OF COMPUTERS THAT ARE CONNECTED TOGETHER SO AS TO SHARE INFORMATION


![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115221827.png)
\
**Source : Random pages on Internet**


# 2. WHAT IS INTERNET
---
Internet is one giant network that consists of many, many small networks within itself. The first iteration of **INTERNET** was within the **ARPANET** project in the late 1960s. Advanced Research Project Agency Network was the first public packet-switched computer network! Main use was for academic and research purposes. It was decommissioned in the late 1980s.

A side benefit of ARPANET's design was that because messages could be routed or rerouted in more than one direction, the network could continue to function even if parts of it were destroyed in the event of a military attack or other disaster. This project was funded by the United States Defence Department and was the first documented network in action. 

However, it wasn't until 1989 when the **INTERNET** as we know it was invented by Tim Berners Lee by the creation of the **W**orld **W**ide **W**eb (**WWW**). It wasn't until this point that the Internet started to be used as a repository for storing and sharing information, just like it is today.


>[!NOTE]
> **INTERNET** aka **NET** is worldwide system of interconnected Computer Networks and Electronic Devices that communicate with each other using an established set of **PROTOCOLS**.


![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115222650.png)
**Source : Britannica**

The **INTERNET** is made up of **MANY SMALL NETWORKS** joined together. 
- These small networks are called **PRIVATE NETWORKS**.
- The networks connecting these small networks are called **PUBLIC NETWORKS**
# 3. TYPES OF NETWORK
---
There are mainly five types of Computer Networks: 

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116121259.png)

## Personal Area Network (PAN)
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116121501.png)

- Designed to connect devices within a short range, typically around one person. 
- Allows your personal devices, like smartphones, tablets, laptops, and wearables, to communicate and share data with each other. 
- Offers a network range of 1 to 100 meters from person to device providing communication.
- Transmission speed is very high with very easy maintenance and very low cost. 
- This uses Bluetoot,  IrDA and Zigbee as technology. Examples of PAN are USB, computer, phone, tablet, printer, PDA, etc

## Local Area Network (LAN)
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116121713.png)

- Network that connects computers through a common communication path, contained within a limited area
- Has a logical and physical borders that a computer can broadcast
- LAN encompasses two or more computers connected over a server.
- The two important technologies involved in this network are Ethernet and Wi-fi.
- It ranges up to 2km & transmission speed is very high with easy maintenance and low cost. 
- Examples of LAN are networking in a home, school, library, laboratory, college, office, etc.

## Campus Area Network (CAN)
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116122030.png)

- Bigger than a LAN but smaller than a MAN. 
- Usually used in places like a school or colleges. 
- Covers a limited geographical area that is, it spreads across several buildings within the campus. 
- Mainly use Ethernet technology with a range from 1km to 5km. T
- Transmission speed is very high with a moderate maintenance cost and moderate cost. 
- Examples of CAN are networks that cover schools, colleges, buildings, etc

## Metropolitan Area Network (MAN)
---
 
 ![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116122247.png)

- Larger than a LAN but smaller than a WAN. 
- Connects computers over a geographical distance through a shared communication path over a city, town, or metropolitan area. 
- Mainly uses FDDI, CDDI, and ATM as the technology with a range from 5km to 50km. 
- Transmission speed is average.
- Difficult to maintain and it comes with a high cost. 
- Examples of MAN are networking in towns, cities, a single large city, a large area within multiple buildings, etc.

## Wide Area Network (WAN)
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116122439.png)

- Connects computers over a large geographical distance through a shared communication path. 
- Not restrained to a single location but extends over many locations.
- Group of local area networks that communicate with each other with a range above 50km. 
- Leased-Line & Dial-up technology is used here. 
- Transmission speed is very low and it comes with very high maintenance and very high cost. 
- The most common example of WAN is the Internet.

# 4. Common Terms in Networking
---
- **IP (internet protocol) address**: the network address of the system across the network, which is also known as the Logical Address). 

- **MAC address**: the MAC address or physical address uniquely identifies each host. It is associated with the Network Interface Card (NIC).

- **Open system**: an open system is connected to the network and prepared for communication.

- **Closed system**: a closed system is not connected to the network and so can't be communicated with.

- **Port**: a port is a channel through which data is sent and received.

- **Nodes**: nodes is a term used to refer to any computing devices such as computers that send and receive network packets across the network.

- **Network packets**: the data that is sent to and from the nodes in a network.

- **Routers**: routers are pieces of hardware that manage router packets. They determine which node the information came from and where to send it to. A router has a routing protocol which defines how it communicates with other routers.

- **‍Network address translation (NAT)**: a technique that routers use to provide internet service to more devices using fewer public IPs. A router has a public IP address but devices connected to it are assigned private IPs that others outside of the network can't see.

- **Dynamic host configuration protocol (DHCP)**: assigns dynamic IP addresses to hosts and is maintained by the internet service provider.

- **Internet service providers (ISP)**: companies that provide everyone with their internet connection, both to individuals and to businesses and other organizations.
# 5. IDENTIFYING DEVICES ON A NETWORK
***
To communicate and maintain order, devices must be **BOTH IDENTIFYING AND IDENTIFIABLE** on a network. Devices on a network are very similar to humans in the fact that we have two ways of being identified **Our Name** **Our Fingerprints**.

We can change our name through deed poll, but we can't, change our fingerprints. Every human has an individual set of fingerprints which means that even if they change their name, there is still an identity behind it. Devices have the same thing: two means of identification, with one being permeable. They are **IP Address** and **Media Access Control (MAC) Address**

## 3. a. IP ADDRESSES
---

IP address (or **I**nternet **P**rotocol) address can be used as a way of identifying a host on a network for a period of time, where that IP address can then be associated with another device without the IP address changing.

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115224629.png)
**Source : HOSTWINDS**


An **IP ADDRESS** is a set of numbers that are divided into four octets. The value of each octet will summarise to be the IP address of the device on the network. This number is calculated through a technique known as **IP ADDRESSING & SUBNETTING**. IP addresses can change from device to device but cannot be active simultaneously more than once within the same network. 

IP Addresses follow a set of standards known as protocols. These protocols are the backbone of networking and force many devices to communicate in the same language. 

A device can be on both a private and public network. Depending on where they are will determine what type of IP address they have: 

- **GLOBAL or PUBLIC or EXTERNAL IP ADDRESS** : Identify the device on the Internet. This group can also be called 'WAN addresses' .
- **PRIVATE or LOCAL or INTERNAL IP ADDRESS** : Identify a device amongst other devices. These are used in the local network (LAN). They are not routed on the Internet and no traffic can be sent to them from the Internet, they only supposed to work within the local network


![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115225243.png)
**SOURCE : GEOTARGETLY**

> [!Note]
> An **Internet Protocol Address (IP ADDRESS)** is a unique address that identifies a device on the internet or a local network. IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network


![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115230725.png)
**Source : Tryhackme**, not my real IP or MAC Address!

These two devices will be able to use their private IP addresses to communicate with each other. However, any data sent to the Internet from either of these devices will be identified by the same public IP address. Public IP addresses are given by your **I**nternet **S**ervice **P**rovider (or **ISP**) at a monthly fee (your bill!).

As more and more devices become connected, it is becoming increasingly harder to get a public address that isn't already in use. Cisco, an industry giant in the world of networking, estimated that there would be approximately 50 billion devices connected on the Internet by the end of 2021.

We have only discussed one version of the Internet Protocol addressing scheme known as IPv4, which uses a numbering system of 2^32 IP addresses (4.29 billion), still there will be a shortage!

IPv6 is a new iteration of the Internet Protocol addressing scheme to help tackle this issue. It supports up to 2^128 of IP addresses (340 trillion-plus), resolving the issues faced with IPv4 and is more efficient due to new methodologies.

## IPv4
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115231813.png)|

**Source : Tryhackme**, not my real IP or MAC Address!

## IPv6
----

![](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115232224.png)|

**Source : Tryhackme**, not my real IP Address!

## IPv4 vs IPv6
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115232533.png)
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

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115235710.png)
**Source : Internet**


![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250115235335.png)

### ``inet``  
---

```inet``` (Internet protocol family) show the local IP address

``` bash
	inet 192.168.1.54  netmask 255.255.255.0  broadcast 192.168.1.255  
```

-    This is IP version 4 (IPv4) Using 32-bit decimal number
-    inet IPv4 : ``192.168.1.54``


```bash
	inet6 fe80::a163:b52c:c585:7a47  prefixlen 64  scopeid 0x20<link>  
```

- This is new version of IP (IPv6), using 128 bits hexadecimal value
- inet IPv6 : ``fe80::a163:b52c:c585:7a47``

###  `ether` 
---

- For the net-tools version typically found on Linux, the word `ether` is the _hardware class_, and the value following that is the hardware address. 
- For the "Ethernet" hardware class the address is the card's MAC address. `ifconfig` shows the current hardware address of the interface, with its hardware class. 
- For Ethernet interfaces, the class is `ether` and the hardware address is the MAC address.

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

## NAT : Network Address Translation
---

- NAT stands for network address translation. 
- Way to map multiple private addresses inside a local network to a public IP address before transferring the information onto the internet. 
- Organisations that want multiple devices to employ a single IP address use NAT, as do most home routers. 

>[!NOTE]
>It is a process in which one or more local IP addresses are translated into one or more Global IP addresses and vice versa to provide Internet access to the local hosts. It also does the translation of port numbers, i.e., masks the port number of the host with another port number in the packet that will be routed to the destination. 

- It then makes the corresponding entries of IP address and port number in the NAT table. 
- NAT generally operates on a router or firewall. 
- If NAT runs out of addresses, i.e., no address is left in the pool configured then the packets will be dropped and an Internet Control Message Protocol (ICMP) host unreachable packet to the destination is sent.

- The router has one interface in the local (inside) network and one interface in the global (outside) network. 
- When a packet traverse outside the local (inside) network, then NAT converts that local (private) IP address to a global (public) IP address. 
- When a packet enters the local network, the global (public) IP address is converted to a local (private) IP address.

Suppose, in a network, two hosts A and B are connected. Now, both of them request for the same destination, on the same port number, say 1000, on the host side, at the same time. If NAT does only translation of IP addresses, then when their packets will arrive at the NAT, both of their IP addresses would be masked by the public IP address of the network and sent to the destination. Destination will send replies to the public IP address of the router. Thus, on receiving a reply, it will be unclear to NAT as to which reply belongs to which host (because source port numbers for both A and B are the same). Hence, to avoid such a problem, NAT masks the source port number as well and makes an entry in the NAT table.

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116104057.png)

Inside refers to the addresses which must be translated. Outside refers to the addresses which are not in control of an organization. These are the network Addresses in which the translation of the addresses will be done.

- **Inside local address** An IP address that is assigned to a host on the Inside (local) network. The address is probably not an IP address assigned by the service provider i.e., these are private IP addresses. This is the inside host seen from the inside network. 
- **Inside global address** IP address that represents one or more inside local IP addresses to the outside world. This is the inside host as seen from the outside network. 
- **Outside local address** This is the actual IP address of the destination host in the local network after translation. 
- **Outside global address This is the outside host as seen from the outside network. It is the IP address of the outside destination host before translation.

### Network Address Translation (NAT) Types

There are 3 ways to configure NAT: 

### Static NAT
---
 
- Single unregistered (Private) IP address is mapped with a legally registered (Public) IP address 
- One-to-one mapping between local and global addresses. 
- Used for Web hosting. 
- Not used in organizations as there are many devices that will need Internet access and to provide Internet access, a public IP address is needed. 

Suppose, if there are 3000 devices that need access to the Internet, the organization has to buy 3000 public addresses that will be very costly. 

### Dynamic NAT
---

- Unregistered IP address is translated into a registered (Public) IP address from a pool of public IP addresses. 
- If the IP address of the pool is not free, then the packet will be dropped as only a fixed number of private IP addresses can be translated to public addresses. 

Suppose, if there is a pool of 2 public IP addresses then only 2 private IP addresses can be translated at a given time. If 3rd private IP address wants to access the Internet then the packet will be dropped therefore many private IP addresses are mapped to a pool of public IP addresses. NAT is used when the number of users who want to access the Internet is fixed. This is also very costly as the organization has to buy many global IP addresses to make a pool. 

#### Port Address Translation (PAT)
---

- This is also known as NAT overload.
- Many local (private) IP addresses can be translated to a single registered IP address. 
- Port numbers are used to distinguish the traffic i.e., which traffic belongs to which IP address. 
- Most frequently used as it is cost-effective as thousands of users can be connected to the Internet by using only one real global (public) IP address.

### SUBNETTING
---

- Process of creating a subnetwork (also known as a subnet) within a network. 
- Network interfaces and devices within a subnet can communicate with each other directly. 
- Routers facilitate communication between different subnets. 
- Provides each group of devices have their own space to communicate, that ultimately helps network to work easily.
- Boosts security and makes it easier to manage the network, as each subnet can be monitored and controlled separately.

>[!NOTE]
>A subnet is like a smaller group within a large network. It is a way to split a large network into smaller networks so that devices present in one network can transmits data more easily. Subnet makes the network faster and easier to manage and also improves the security of the network.

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116111029.png)

- **Network Portion** :  The first few sections (octets) of an IP address identify the network that the device belongs to. This part of the IP address is common among all devices on the same network, allowing them to communicate with each other and share resources.
- **Host Portion** : The remaining sections of the IP address specify the individual device, or “host,” within that network. This part makes each device unique within the network, allowing the router to distinguish between different devices.

The 32-bit IP address is divided into sub-classes. These are given below:

- **Class A :** The network ID is 8 bits long and the host ID is 24 bits long.
- **Class B :** The network ID is 16 bits long and the host ID is 16 bits long.
- **Class C :** The network ID is 24 bits long and the host ID is 8 bits long.

- **Class A**: the IP starts from 0 -126 (talking about the first octet from left) that’s how we identify classes.  
- **Class B** : It starts from 128–191  
- **Class C** : It starts from 192–223  
- **Class D** : 224–239  
- **Class E** : 240–255

The working of subnets starts in such a way that firstly it divides the subnets into smaller subnets. For communicating between subnets, routers are used. Each subnet allows its linked devices to communicate with each other. Subnetting for a network should be done in such a way that it does not affect the network bits.\

In class C the first 3 octets are network bits so it remains as it is. 

- **For Subnet-1 :** The first bit which is chosen from the host id part is zero and the range will be from (193.1.2.00000000 till you get all 1’s in the host ID part i.e, 193.1.2.01111111) except for the first bit which is chosen zero for subnet id part.
	- Thus, the range of subnet 1 is: **193.1.2.0 to 193.1.2.127**
- **For Subnet-2 :** The first bit chosen from the host id part is one and the range will be from (193.1.2.100000000 till you get all 1’s in the host ID part i.e, 193.1.2.11111111).
	- Thus, the range of subnet-2 is: **193.1.2.128 to 193.1.2.255**

Finally, after using the subnetting the total number of usable hosts is reduced from 254 to 252. 

>[!NOTE]
> To divide a network into four (2 2 ) parts you need to choose two bits from the host id part for each subnet i.e, (00, 01, 10, 11).
> To divide a network into eight (2 3 ) parts you need to choose three bits from the host id part for each subnet i.e, (000, 001, 010, 011, 100, 101, 110, 111) and so on.
>  We can say that if the total number of subnets in a network increases the total number of usable hosts decreases.

**Subnet mask**:
- A 32-bit number used in IP addressing to separate the network portion of an IP address from the host portion. 
- Helps computers and devices determine which part of an IP address refers to the network they are present, and which part refers to their specific location or address within that network.

**Point to point subnet**
- A point-to-point subnet is a particular type of subnet used in point-to-point links that facilitate direct communication between two routers. 
- Consists of a 31-bit subnet mask, leaving only two possible addresses in the network. 
- Since point-to-point subnets contain only one host, a different broadcast address isn’t necessary.

Because an IP address is limited to indicating the network and the device address, IP addresses cannot be used to indicate which subnet an IP packet should go to. Routers within a network use something called a subnet mask to sort data into subnetworks.

[Click here for Subnetting Cheatsheet PDF](https://nsrc.org/workshops/2009/summer/presentations/day3/subnetting.pdf)
### Other relevant information about IPs

- **IPv4 Main Address Types**
    - **Unicast** - acted on by a single recipient
    - **Multicast** - acted on by members of a specific group
    - **Broadcast** - acted on by everyone on the network
        - **Limited** - delivered to every system in the domain (255.255.255.255)
        - **Directed** - delivered to all devices on a subnet and use that broadcast address
- **Subnet mask** - determines how many address available on a specific subnet
    - Represented by three methods
        - **Decimal** - 255.240.0.0
        - **Binary** - 11111111.11110000.00000000.00000000
        - **CIDR** - x.x.x.x/12 (where x.x.x.x is an ip address on that range)
    - If all the bits in the host field are 1s, the address is the broadcast
    - If they are all 0s, it's the network address
    - Any other combination indicates an address in the range
## 3. b. MAC ADDRESSES
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116191347.png)

- Devices on a network will all have a physical network interface, which is a microchip board found on the device's motherboard. 
- This network interface is assigned a unique address at the factory it was built at, called a **MAC** (**M**edia **A**ccess **C**ontrol ) address. 
- The MAC address is a **twelve-character** hexadecimal number (_a base sixteen numbering system used in computing to represent numbers_) split into two's and separated by a colon. 
- These colons are considered separators. 
- For example, **a4:c3:f0:85:ac:2d**. The first six characters represent the company that made the network interface, and the last six is a unique number.

>[!NOTE]
>MAC (Media Access Control) address are 48-bit hardware numbers and is provided by NIC Card'd manufacturer and gives the physical address of a computer

- The first three bytes of a MAC address were originally known as **OUI**’s, or **Organizational Unique Identifiers**. 
- Each manufacturer of networking equipment was assigned an OUI, and was free to assign their own numbers in that block. 
- They can be faked or "spoofed" in a process known as spoofing. 
- This spoofing occurs when a networked device pretends to identify as another using its MAC address. 
- When this occurs, it can often break poorly implemented security designs that assume that devices talking on a network are trustworthy.

```MAC
   OUI     NIC
    |       |
________ ________
a4:c3:f0:85:ac:2d
```

## Checking vendor behind MAC address
---

1. Check your MAC address use the command ``ifconfig`` (Linux) or ``ipconfig`` (Windows)

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116113423.png)

2. Copy and save the first three bytes of your address. (The first three bytes from image above is *f8:fe:5e*)

4. Validate the information by performing a **MAC Address Lookup** on the internet. Here I am using [DNS CHECKER](https://dnschecker.org/mac-lookup.php)

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116113536.png)
- As you can see the OUI lookup identify a virtual network interface provided by VMware


# 6. PING (ICMP)
---

- One of the most fundamental network tools available to us. 
- Uses **ICMP** (**I**nternet **C**ontrol **M**essage **P**rotocol) packets to determine the performance of a connection between devices, for example, if the connection exists or is reliable.

>[!NOTE]
>**Internet Control Message Protocol (ICMP)** is a protocol that devices within a network use to communicate problems with data transmission

- The time taken for ICMP packets travelling between devices is measured by ping. 
- This measuring is done using ICMP's echo packet and then ICMP's echo reply from the target device.

- Pings can be performed against devices on a network, such as your home network or resources like websites. 
- This tool can be easily used and comes installed on Operating Systems (OSs) such as Linux and Windows. The syntax to do a simple ping is ``ping <IP_address_or_website_URL>``.

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116114038.png)
Here we are pinging a device that has the public address of **8.8.8.8**. 

- Ping informs us that we have sent four ICMP packets, all of which were received with an average time of 29.125 milliseconds. 
- It relays messages from the receiver to the sender about the data that was supposed to arrive. 
- If the data either does not reach the receiver or is received in the wrong order, ICMP lets the sender know so the data can be resent.
- In this way, ICMP is simply a protocol for communicating information about data, but it does not manage the data itself. 
- It can be used to execute distributed denial-of-service (DDoS) attacks. 
- ICMP packets are transmitted in the form of datagrams that contain an IP header with ICMP data. 
- ICMP datagram is similar to a packet, which is an independent data entity.
- ICMP header comes after IPv4 and IPv6 packet header.

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116120655.png)


In the ICMP packet format, the first 32 bits of the packet contain three fields:

**Type (8-bit)** : 
- The initial 8-bit of the packet is for message type 
- Provides a brief description of the message so that receiving network would know what kind of message it is receiving and how to respond to it. 

Some common message types are as follows:
- Type 0 – Echo reply
- Type 3 – Destination unreachable
- Type 5 – Redirect Message
- Type 8 – Echo Request
- Type 11 – Time Exceeded
- Type 12 – Parameter problem

**Code (8-bit) :** 
- Code is the next 8 bits of the ICMP packet format
- Carries some additional information about the error message and type.

**Checksum (16-bit) :** 
- Last 16 bits are for the checksum field in the ICMP packet header. 
- Used to check the number of bits of the complete message and enable the ICMP tool to ensure that complete data is delivered.

**Extended Header :**
- Next 32 bits of the ICMP Header 
- Pointing out the problem in IP Message. 
- Byte locations are identified by the pointer which causes the problem message and receiving device looks here for pointing to the problem.

**Data or Payload :**
- The last part of the ICMP packet is  of variable length. 
- The bytes included in IPv4 are 576 bytes and in IPv6, 1280 bytes.

## Uses of ICMP 

- Error reporting : If two devices connect over the internet and some error occurs, the router sends an ICMP error message to the source informing about the error. Whenever a device sends any message which is large enough for the receiver, in that case, the receiver will drop the message and reply to the ICMP message to the source.
- Traceroute : Used to know the route between two devices connected over the internet. It routes the journey from one router to another, and a traceroute is performed to check network issues before data transfer.  
- Ping : Simple kind of traceroute known as the echo-request message, it is used to measure the time taken by data to reach the destination and return to the source, these replies are known as echo-replies messages.
For more information, [Check this out!](https://www.fortinet.com/resources/cyberglossary/internet-control-message-protocol-icmp)

# 7. TOPOLOGIES
---

>[!NOTE]
>Topology refer to the design or look of the network at hand

### Star Topology
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116131546.png)

- Devices are individually connected via a central networking device such as a switch or hub. 
- This topology is the most commonly found today because of its reliability and scalability - despite the cost.
- Any information sent to a device in this topology is sent via the central device to which it connects.
- Because more cabling and the purchase of dedicated networking equipment is required for this topology, it is more expensive than any of the other topologies.
- This topology is much more scalable in nature, which means that it is very easy to add more devices as the demand for the network increases.
- The more the network scales, the more maintenance is required to keep the network functional. 
- This increased dependence on maintenance can also make troubleshooting faults much harder. 
- Furthermore, the star topology is still prone to failure - albeit reduced. If the centralised hardware that connects devices fails, these devices will no longer be able to send or receive data.

### Bus Topology
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116131732.png)

- This type of connection relies upon a single connection which is known as a backbone cable. 
- This type of topology is similar to the leaf off of a tree in the sense that devices (leaves) stem from where the branches are on this cable.
- Because all data destined for each device travels along the same cable, it is very quickly prone to becoming slow and bottlenecked if devices within the topology are simultaneously requesting data. 
- This bottleneck also results in very difficult troubleshooting because it quickly becomes difficult to identify which device is experiencing issues with data all travelling along the same route.
- However, with this said, bus topologies are one of the easier and more cost-efficient topologies to set up because of their expenses, such as cabling or dedicated networking equipment used to connect these devices.
- Lastly, another disadvantage of the bus topology is that there is little redundancy in place in case of failures. 
- This disadvantage is because there is a single point of failure along the backbone cable. 
- If this cable were to break, devices can no longer receive or transmit data along the bus.

### Ring Topology (Token Topology)
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116132002.png)

- Devices such as computers are connected directly to each other to form a loop
- There is little cabling required and less dependence on dedicated hardware such as within a star topology.
- A ring topology works by sending data across the loop until it reaches the destined device, using other devices along the loop to forward the data. 
- A device will only send received data from another device in this topology if it does not have any to send itself. 
- If the device happens to have data to send, it will send its own data first before sending data from another device.
- Because there is only one direction for data to travel across this topology, it is fairly easy to troubleshoot any faults that arise. 
- It isn't an efficient way of data travelling across a network, as it may have to visit many multiple devices first before reaching the intended device.
- Ring topologies are less prone to bottlenecks, such as within a bus topology, as large amounts of traffic are not travelling across the network at any one time. 
- The design of this topology does, however, mean that a fault such as cut cable, or broken device will result in the entire networking breaking.

### Point to Point Topology
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116132130.png)

- Works on the functionality of the sender and receiver. 
- Simplest communication between two nodes, in which one is the sender and the other one is the receiver.
- Point-to-Point provides high bandwidth.

### Mesh Topology
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116132224.png)

- Every device is connected to another device via a particular channel. 
- Every device is connected to another via dedicated channels. 
- These channels are known as links. 
- In Mesh Topology, the protocols used are AHCP (Ad Hoc Configuration Protocols), DHCP (Dynamic Host Configuration Protocol), etc.

### Tree Topology
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116132415.png)

- Tree topology is the variation of the Star topology. 
- Has a hierarchical flow of data. 
- Protocols like DHCP and SAC (Standard Automatic Configuration) are used.
- Various secondary hubs are connected to the central hub which contains the repeater. 
- This data flow from top to bottom i.e. from the central hub to the secondary and then to the devices or from bottom to top i.e. devices to the secondary hub and then to the central hub.
- It is a multi-point connection and a non-robust topology because if the backbone fails the topology crashes. 

### Hybrid Topology
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116132437.png)

- Combination of all the various types of topologies 
- Hybrid Topology is used when the nodes are free to take any form. 
- It means these can be individuals such as Ring or Star topology or can be a combination of various types of topologies seen above. 
- Each individual topology uses the protocol that has been discussed earlier.

# 8. SWITCH
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116133546.png)

- Dedicated devices within a network that are designed to aggregate multiple other devices such as computers, printers, or any other networking-capable device using ethernet. 
- These various devices plug into a switch's port. 
- Switches are usually found in larger networks such as businesses, schools, or similar-sized networks, where there are many devices to connect to the network. 
- Switches can connect a large number of devices by having ports of 4, 8, 16, 24, 32, and 64 for devices to plug into.
- Switches are much more efficient than their lesser counterpart (hubs/repeaters). 
- Switches keep track of what device is connected to which port. 
- When they receive a packet, instead of repeating that packet to every port like a hub would do, it just sends it to the intended target, thus reducing network traffic.
- Different types of communication are supported here like unicast, multicast, and broadcast communication.
- It operates in the Data Link Layer in the OSI Model.
- It performs error checking before forwarding data.
- It operates in full duplex mode.
- It allocates each LAN segment to a limited bandwidth.
- It uses Unicast (one-to-one), multicast (one-to-many), and broadcast (one-to-all) transmission modes.
- Packet-switching techniques are used to transfer data packets from source to destination.
- Both Switches and Routers can be connected to one another. 
- The ability to do this increases the redundancy (the reliability) of a network by adding multiple paths for data to take.
- If one path goes down, another can be used. 
- Whilst this may reduce the overall performance of a network because packets have to take longer to travel, there is no downtime

>[!IMPORTANT]
>The Switch is a network device that is used to segment the networks into different subnetworks called subnets or LAN segments. It is responsible for filtering and forwarding the packets between LAN segments based on MAC address. 


Switches are mainly classified into the following types that are mentioned below.

**Virtual Switches :** 
- Virtual Switches are the switches that are inside Virtual Machine hosting environments.

**Routing Switches :** 
- These are the switches that are used to connect LANs.
- They also have the work of performing functions in the Network Layer of the OSI Model.

**Unmanaged Switches :** 
- Unmanaged Switches are the devices that are used to enable Ethernet devices that help in automatic data passing. 
- These are generally used for home networks and small businesses. 
- In case of the requirement of more switches, we just add more switches by plug and play method.

**Managed Switches :** 
- Managed Switches are switches having more complex networks. 
- SNMP (Simple Network Management Protocol) can be used for configuring managed switches. 
- These types of switches are mostly used in large networks having complex architecture. 
- They provide better security levels and precision control but they are more costly than Unmanaged switches. 

**LAN Switches :** 
- LAN (Local Area Network) Switches are also called ethernet switches or data switches.
- LAN switches always try to avoid overlapping of data packets in the network just by allocating bandwidth in such a manner.

**PoE Switches :** 
- Power over Ethernet(PoE) are the switches used in Gigabit Ethernets. 
- PoE help in combining data and power transmission over the same cable so that it helps in receiving data and electricity over the same line.

**Smart Switches :**
- Smart Switches are switches having some extra controls on data transmissions but also have extra limitations over managed Switches. 
- They are also called partially managed switches.

**Stackable Switches :**
- Stackable switches are connected through a backplane to combine two logical switches into a single switch.

**Modular Switches :**
- These types of switches help in accommodating two or more cards. 
- Modular switches help in providing better flexibility.
# 9. ROUTER
---

>[!IMPORTANT]
>Routing is the process of selecting and defining paths for IP-packet traffic within or between networks as well as the process of managing network traffic overall.
>
>A routing table is a repository of all the routes to all the destinations in use by a network.

- Routers connect networks to other networks and act as dispatchers. 
- They analyze data to be sent across networks, identify where it needs to go, choose the best routes for it, and send it on its way.
- Routers connect organizations to the outside world and can help to protect information from outside security threats.
- While switches and routers differ in several other ways, a key difference is how they identify end devices.
- A Layer 2 switch uniquely identifies a device by its MAC address. 
- A Layer 3 router uniquely identifies a device by a network-assigned IP address.
- Ethernet technology provides the routing rules that enable network-connected devices to talk to, and not over, one another.
- If two or more connected devices on a network try to transmit data packets at the same time, a packet collision occurs. Ethernet was designed to solve the problem of packet collision.
- It provides network devices with a set of rules that essentially says, "Make sure no one else is talking before you talk. If you hear someone talking while you're talking, stop, listen, and wait for the talking to end before you talk again."
- The routing process starts when software on a host device uses a packet's contents, destination, or purpose to select a possible route from a routing table. A routing table is a repository of all the routes to all the destinations in use by a network.
- Routing tables can be created manually and "learned" by software as it observes network traffic, or they can be built according to routing protocols.
- A simple print job may be transmitted using static routing, where the host plugs in a previously used route. 
- Dynamic routing allows a packet to be routed contextually, according to network conditions or factors such as reliability, performance, and security requirements.
- Every pathway segment in the network has a metric assigned to it that's based on such factors. 
- These metrics are shared with hosts and other nodes to be stored in routing tables and used for path selection.
- A node is any device, such as a switch or router, that is connected to a network. 
- A host is a type of node, such as a computer, that has a network address, the ability to permit access to a network, and the ability to participate in application-level functions.

[For more information on routing, Check this out!](https://aws.amazon.com/what-is/routing/)

# 10. SUBNETTING
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116140541.png)
**SOURCE : Tryhackme**

- Subnetting is the term given to splitting up a network into smaller, miniature networks within itself
- Process of creating a subnetwork (also known as a subnet) within a network. 
- Network interfaces and devices within a subnet can communicate with each other directly. 
- Routers facilitate communication between different subnets. 
- Provides each group of devices have their own space to communicate, that ultimately helps network to work easily.
- Boosts security and makes it easier to manage the network, as each subnet can be monitored and controlled separately.
- Subnetting is achieved by splitting up the number of hosts that can fit within the network, represented by a number called a **SUBNET MASK**.
- The working of subnets starts in such a way that firstly it divides the subnets into smaller subnets. 
- For communicating between subnets, routers are used. 
- Each subnet allows its linked devices to communicate with each other. 
- Subnetting for a network should be done in such a way that it does not affect the network bits.

>[!IMPORTANT]
>A subnet is like a smaller group within a large network. 
>
>It is a way to split a large network into smaller networks so that devices present in one network can transmits data more easily. 
>
>Subnet makes the network faster and easier to manage and also improves the security of the network.

## Subnet mask :
---

- A 32-bit number used in IP addressing to separate the network portion of an IP address from the host portion. 
- Helps computers and devices determine which part of an IP address refers to the network they are present, and which part refers to their specific location or address within that network.
- Because an IP address is limited to indicating the network and the device address, IP addresses cannot be used to indicate which subnet an IP packet should go to. 
- Routers within a network use something called a subnet mask to sort data into subnetworks.



![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116111029.png)

- Subnets use IP addresses in three different ways:
	- Identify the network address
	- Identify the host address
	- Identify the default gateway

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116140839.png)

Let's split these three up to understand their purposes into the table below:
- **Network Portion** :  The first few sections (octets) of an IP address identify the network that the device belongs to. This part of the IP address is common among all devices on the same network, allowing them to communicate with each other and share resources.
- **Host Portion** : The remaining sections of the IP address specify the individual device, or “host,” within that network. This part makes each device unique within the network, allowing the router to distinguish between different devices.

The 32-bit IP address is divided into sub-classes. These are given below:

- **Class A :** The network ID is 8 bits long and the host ID is 24 bits long.
- **Class B :** The network ID is 16 bits long and the host ID is 16 bits long.
- **Class C :** The network ID is 24 bits long and the host ID is 8 bits long.

- **Class A**: the IP starts from 0 -126 (talking about the first octet from left) that’s how we identify classes.  
- **Class B** : It starts from 128–191  
- **Class C** : It starts from 192–223  
- **Class D** : 224–239  
- **Class E** : 240–255

In class C the first 3 octets are network bits so it remains as it is. 

- **For Subnet-1 :** The first bit which is chosen from the host id part is zero and the range will be from (193.1.2.00000000 till you get all 1’s in the host ID part i.e, 193.1.2.01111111) except for the first bit which is chosen zero for subnet id part. Thus, the range of subnet 1 is: **193.1.2.0 to 193.1.2.127**
- **For Subnet-2 :** The first bit chosen from the host id part is one and the range will be from (193.1.2.100000000 till you get all 1’s in the host ID part i.e, 193.1.2.11111111). Thus, the range of subnet-2 is: **193.1.2.128 to 193.1.2.255**
- Finally, after using the subnetting the total number of usable hosts is reduced from 254 to 252. 

>[!NOTE]
> To divide a network into four (2 2 ) parts you need to choose two bits from the host id part for each subnet i.e, (00, 01, 10, 11).
> To divide a network into eight (2 3 ) parts you need to choose three bits from the host id part for each subnet i.e, (000, 001, 010, 011, 100, 101, 110, 111) and so on.
>  We can say that if the total number of subnets in a network increases the total number of usable hosts decreases.


Now, in small networks such as at home, you will be on one subnet as there is an unlikely chance that you need more than 254 devices connected at one time.

However, places such as businesses and offices will have much more of these devices (PCs, printers, cameras and sensors), where subnetting takes place.


**Point to point subnet**
- A point-to-point subnet is a particular type of subnet used in point-to-point links that facilitate direct communication between two routers. 
- Consists of a 31-bit subnet mask, leaving only two possible addresses in the network. 
- Since point-to-point subnets contain only one host, a different broadcast address isn’t necessary.



[Click here for Subnetting Cheatsheet PDF](https://nsrc.org/workshops/2009/summer/presentations/day3/subnetting.pdf)


# 11. ARP (ADDRESS RESOLUTION PROTOCOL)
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116141933.png)

- The technology that is responsible for allowing devices to identify themselves on a network.
- ARP allows a device to associate its MAC address with an IP address on the network. 
- **ARP** dynamically translates Internet addresses into the unique hardware addresses on local area networks.
- Each device on a network will keep a log of the MAC addresses associated with other devices.
- Devices can use ARP to find the MAC address (and therefore the physical identifier) of a device for communication
- Each device within a network has a ledger to store information on, which is called a cache. In the context of ARP, this cache stores the identifiers of other devices on the network.
- In order to map these two identifiers together (IP address and MAC address), ARP sends two types of messages: ARP Request and ARP Reply
- When an **ARP request** is sent, a message is broadcasted on the network to other devices asking, "What is the mac address that owns this IP address?"
- When any host that supports **ARP** receives an **ARP** request packet, the host notes the **IP** and hardware addresses of the requesting system and updates its mapping table.
- They will only respond if they own that IP address and will send an **ARP reply** with its MAC address.
- If the receiving host **IP** address does not match the requested address, the host discards the request packet. 
- If the **IP** address does match, the receiving host sends a response packet to the requesting system. 
- The requesting system stores the new mapping in its **ARP cache** for future use and uses it to transmit any similar pending Internet packets. 

> [!NOTE]
> Address Resolution Protocol (ARP) is responsible for finding the MAC (hardware) address related to a specific IP address. It works by broadcasting an ARP query, "Who has this IP address? Tell me." And the response is of the form, "The IP address is at this MAC address."


![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116142231.png)
FOR MORE INFORMATION ABOUT ARP :
- [RESOURCE 1 : MICROSOFT](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/arp)
- [RESOURCE 2 : FORTINET](https://www.fortinet.com/resources/cyberglossary/what-is-arp)

# 12. DHCP
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116142724.png)

- IP addresses can be assigned either manually, by entering them physically into a device, or automatically and most commonly by using a **DHCP** (**D**ynamic **H**ost **C**onfiguration **P**rotocol) server. 

>[!IMPORTANT]
>Dynamic Host Configuration Protocol (DHCP) is a client/server protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway


- When a device connects to a network, if it has not already been manually assigned an IP address, it sends out a request (**DHCP Discover**) to see if any DHCP servers are on the network. 
- The DHCP server then replies back with an IP address the device could use (**DHCP Offer**). 
- The device then sends a reply confirming it wants the offered IP Address (**DHCP Request**), and then lastly, the DHCP server sends a reply acknowledging this has been completed, and the device can start using the IP Address (**DHCP ACK**).


>[!NOTE]
>The Dynamic Host Configuration Protocol (DHCP) is a network management protocol used on Internet Protocol (IP) networks for automatically assigning IP addresses and other communication parameters to devices connected to the network using a client–server architecture.


Every device on a TCP/IP-based network must have a unique unicast IP address to access the network and its resources. Without DHCP, IP addresses for new computers or computers that are moved from one subnet to another must be configured manually; IP addresses for computers that are removed from the network must be manually reclaimed.

With DHCP, this entire process is automated and managed centrally. The DHCP server maintains a pool of IP addresses and leases an address to any DHCP-enabled client when it starts up on the network. Because the IP addresses are dynamic (leased) rather than static (permanently assigned), addresses no longer in use are automatically returned to the pool for reallocation.

The network administrator establishes DHCP servers that maintain TCP/IP configuration information and provide address configuration to DHCP-enabled clients in the form of a lease offer. The DHCP server stores the configuration information in a database that includes:

[FOR MORE INFORMATION ON DHCP, CLICK HERE](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top)


# 13. OSI MODEL
----

- **OSI** model (or **O**pen **S**ystems **I**nterconnection Model) provides a framework dictating how all networked devices will send, receive and interpret data. 
- OSI Model is a hypothetical networking framework that uses specific protocols and mechanisms in every layer of it. 
- This model is used to divide the network architecture into seven different layers conceptually. 
- One of the main benefits of the OSI model is that devices can have different functions and designs on a network while communicating with other devices. 
- Data sent across a network that follows the uniformity of the OSI model can be understood by other devices.
- At every individual layer that data travels through, specific processes take place, and pieces of information are added to this data. This process is called encapsulation.

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116145350.png)

## LAYER 07 : APPLICATION LAYER
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116153228.png)

- This is the only layer that directly interacts with data from the user. 
- It is the layer in which protocols and rules are in place to determine how the user should interact with data sent or received.
- Software applications like web browsers and email clients rely on the application layer to initiate communications. 
- Client software applications are not part of the application layer; rather the application layer is responsible for the protocols and data manipulation that the software relies on to present meaningful data to the user.
- Application layer protocols include HTTP as well as SMTP (Simple Mail Transfer Protocol is one of the protocols that enables email communications).
- Other protocols include **DNS** (**D**omain **N**ame **S**ystem), which is how website addresses are translated into IP addresses.

## LAYER 06 : PRESENTATION LAYER
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116153008.png)

- Layer 6 of the OSI model is the layer in which standardisation starts to take place. Because software developers can develop any software such as an email client differently, the data still needs to be handled in the same way — no matter how the software works.
- This layer acts as a translator for data to and from the application layer (layer 7). 
- The receiving computer will also understand data sent to a computer in one format destined for in another format. For example, when you send an email, the other user may have another email client to you, but the contents of the email will still need to display the same.
- The presentation layer is responsible for translation, encryption, and compression of data. Security features such as data encryption (like HTTPS when visiting a secure site) occur at this layer.
- It also makes the data presentable for applications to consume.

## LAYER 05 : SESSION LAYER
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116152714.png)

- Once data has been correctly translated or formatted from the presentation layer (layer 6), the session layer (layer 5) will begin to create and maintain the connection to other computer for which the data is destined. 
- This is the layer responsible for opening and closing communication between the two devices. 
- The time between when the communication is opened and closed is known as the session.  
- When a connection is established, a session is created. Whilst this connection is active, so is the session.
- The session layer is also responsible for closing the connection if it hasn't been used in a while or if it is lost. 
- Additionally, a session _can_ contain "checkpoints," where if the data is lost, only the newest pieces of data are required to be sent, saving bandwidth. 
- Sessions are unique. Data cannot travel over different sessions, but only across each session instead.

## LAYER 04 : TRANSPORT LAYER
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116151325.png)

- Layer 4 of the OSI model plays a vital part in transmitting data across a network
- When data is sent between devices, it follows one of two different protocols that are decided based upon several factors **TCP** or **UDP**
- It is responsible for end-to-end communication between the two devices. 
- This includes taking data from the session layer and breaking it up into chunks called segments before sending it to layer 3. 
- The transport layer on the receiving device is responsible for reassembling the segments into data the session layer can consume.
- The transport layer is also responsible for flow control and error control. 
- Flow control determines an optimal speed of transmission to ensure that a sender with a fast connection doesn’t overwhelm a receiver with a slow connection. 
- The transport layer performs error control on the receiving end by ensuring that the data received is complete, and requesting a retransmission if it isn’t.

### TCP (Transmission Control Protocol)
---

>[!IMPORTANT]
>TCP is a communication standard for delivering data and messages through networks. TCP is a basic standard that defines the rules of the internet and is a common protocol used to deliver data in digital network communications.

- TCP enables data to be transferred between applications and devices on a network. 
- It is designed to break down a message, such as an email, into packets of data to ensure the message reaches its destination successfully and as quickly as possible
- This protocol is designed with reliability and guarantee in mind.
- This protocol reserves a constant connection between the two devices for the amount of time it takes for the data to be sent and received.
- TCP incorporates error checking into its design. Error checking is how TCP can guarantee that data sent from the small chunks in the session layer (layer 5) has then been received and reassembled in the same order.

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116151630.png)

- TCP is the most commonly used of these protocols and accounts for the most traffic used on a TCP/IP network.
- TCP is used for situations such as file sharing, internet browsing or sending an email. This usage is because these services require the data to be accurate and complete (no good having half a file!).

### UDP (User Datagram Protocol)
---

- It lightweight data transport protocol that works on top of IP. 
- UDP provides a mechanism to detect corrupt data in packets, but it does not attempt to solve other problems that arise with packets, such as lost or out of order packets. Hence UDP is sometimes known as the Unreliable Data Protocol.
- Data that gets sent via UDP is sent to the computer whether it gets there or not. 
- There is no synchronisation between the two devices or guarantee; just hope for the best, and fingers crossed.
- UDP is simple but fast, at least in comparison to other protocols that work over IP. 

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116151945.png)

UDP is useful in situations where there are small pieces of data being sent. For example, protocols used for discovering devices (ARP and DHCP) or larger files such as video streaming (where it is okay if some part of the video is pixelated. Pixels are just lost pieces of data!). It's often used for time-sensitive applications (such as real-time video streaming) where speed is more important than accuracy.
## LAYER 03 : NETWORK LAYER
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116150707.png)

- The third layer of the OSI model (network layer) is where routing & re-assembly of data takes place (from these small chunks to the larger chunk). 
- Firstly, routing simply determines the most optimal path in which these chunks of data should be sent. The network layer finds the best physical path for the data to reach its destination.
- The network layer is responsible for facilitating data transfer between two different networks. 
- If the two devices communicating are on the same network, then the network layer is unnecessary. 
- The network layer breaks up segments from the transport layer into smaller units, called packets, on the sender’s device, and reassembling these packets on the receiving device. 
- The protocols that determine "optimal" path that data should take to reach a device include **OSPF** (**O**pen **S**hortest **P**ath **F**irst) and **RIP** (**R**outing **I**nformation **P**rotocol).
- The factors that decide what route is taken is decided by the following:
	- Shortest Path : Has the least amount of devices that the packet needs to travel across
	- Reliability : Have packets been lost on that path before
	- Faster physical connection : Is the path using a copper connection (slower) or a fibre (considerably faster)
- At this layer, everything is dealt with via IP addresses such as 192.168.1.100. 
- Devices such as routers capable of delivering packets using IP addresses are known as Layer 3 devices — because they are capable of working at the third layer of the OSI model.

## LAYER 02 : DATA LINK LAYER
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116150538.png)

- The data link layer focuses on the physical addressing of the transmission. 
- It receives a packet from the network layer (including the IP address for the remote computer) and adds in the physical **MAC** (Media Access Control) address of the receiving endpoint. 
- Inside every network-enabled computer is a **N**etwork **I**nterface Card (**NIC**) which comes with a unique MAC address to identify it.
- MAC addresses are set by the manufacturer and literally burnt into the card; they can’t be changed – although they can be spoofed. 
- When information is sent across a network, it’s actually the physical address that is used to identify where exactly to send the information.
- It is the job of the data link layer to present the data in a format suitable for transmission.
- It facilitates data transfer between two devices on the SAME network. 
- The data link layer takes packets from the network layer and breaks them into smaller pieces called frames. 
- The data link layer is responsible for flow control and error control in intra-network communication 

## LAYER 01 : PHYSICAL LAYER
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116150116.png)

- This layer references the physical components of the hardware used in networking and is the lowest layer that you will find. 
- Devices use electrical signals to transfer data between each other in a binary numbering system (1's and 0's). 
- The physical layer of both devices must also agree on a signal convention so that the 1s can be distinguished from the 0s on both devices. 
- For example, ethernet cables, Switches etc

# 14. PACKETS AND FRAMES
---

- Packets and frames are small pieces of data that, when forming together, make a larger piece of information or message. 
- They are two different things in the OSI model. 
- A frame is at layer 2 - the data link layer, meaning there is no such information as IP addresses. Think of this as putting an envelope within an envelope and sending it away. The first envelope will be the packet that you mail, but once it is opened, the envelope within still exists and contains data (this is a frame). This process is called encapsulation.
- When we are talking about anything IP addresses, we are talking about packets. 
- When the encapsulating information is stripped away, we're talking about the frame itself.
- Packets are an efficient way of communicating data across networked devices because this data is exchanged in small pieces, there is less chance of bottlenecking occurring across a network than large messages being sent at once.
- When loading an image from a website, this image is not sent to your computer as a whole, but rather small pieces where it is reconstructed on your computer.

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116154748.png)
**Source : Tryhackme**

- Packets have different structures that are dependant upon the type of packet that is being sent.
- A packet using Internet Protocol will have a set of headers that contain additional pieces of information to the data that is being sent across a network, some notable ones are listed below

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116154930.png)

# 15. TCP/IP  THREE-WAY HANDSHAKE
---

- **TCP** (or **T**ransmission **C**ontrol **P**rotocol for short) is another one of these rules used in networking.

- This protocol is very similar to the OSI model that we have previously discussed in room three of this module so far. The TCP/IP protocol consists of four layers and is arguably just a summarised version of the OSI model. 

- These layers are:

	- Application
	- Transport
	- Internet
	- Network interface

- Information is added to each layer of the TCP model as the piece of data (or packet) traverses it. This process is known as encapsulation - where the reverse of this process is decapsulation.

- It is **connection-based**, which means that TCP must establish a connection between both a client and a device acting as a server **before** data is sent.

- TCP guarantees that any data sent will be received on the other end by a process named the Three-way handshake.
![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116170330.png)

- TCP packets contain various sections of information known as headers that are added from encapsulation. 

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116170445.png)

The TCP/IP model consists of several types of protocols, including:
    - TCP and IP
    - Address Resolution Protocol (ARP)
    - Internet Control Message Protocol (ICMP)
    - Reverse Address Resolution Protocol (RARP)
    - User Datagram Protocol (UDP)

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116171316.png)



## THREE WAY HANDSHAKE 
---

Three-way handshake is the term given for the process used to establish a connection between two devices. The Three-way handshake communicates using a few special messages :

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116170549.png)

## TCP Flags
---

|Flag|Name|Function|
|---|---|---|
|SYN|Synchronize|Set during initial communication. Negotiating of parameters and sequence numbers|
|ACK|Acknowledgment|Set as an acknowledgement to the SYN flag. Always set after initial SYN|
|RST|Reset|Forces the termination of a connection (in both directions)|
|FIN|Finish|Ordered close to communications|
|PSH|Push|Forces the delivery of data without concern for buffering|
|URG|Urgent|Data inside is being sent out of band. Example is cancelling a message|

## TCP PACKET FORMAT
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116171357.png)


### INITIATING A CONNECTION
---

Any sent data is given a random number sequence and is reconstructed using this number sequence and incrementing by 1. Both computers must agree on the same number sequence for data to be sent in the correct order. This order is agreed upon during three steps:
1. **SYN** - Client: Here's my Initial Sequence Number(**ISN**) to **SYNc**hronise with (0)
2. **SYN/ACK** - Server: Here's my Initial Sequence Number (**ISN**) to **SYN**chronise with (5,000), and I **ACK**nowledge your initial number sequence (0)
3. **ACK** - Client: I **ACK**nowledge your Initial Sequence Number (**ISN**) of (5,000), here is some data that is my **ISN**+1 (0 + 1)

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116170654.png)

### ESTABLISH CONNECTION
![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116171417.png)

### TCP HEADER WITH SYN AND ACK BITS HIGHLIGHTED
---

>[!NOTE]
>The first computer sends a packet with the SYN bit set to ‍  (SYN = "synchronize?"). The second computer sends back a packet with the ACK bit set to ‍  (ACK = "acknowledge!") plus the SYN bit set to ‍ . The first computer replies back with an ACK.


The SYN and ACK bits are both part of the TCP header :
![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116171443.png)

>[!NOTE]
>The three packets(**SYN**,**SYN/ACK** and **ACK**) involved in the three-way handshake do not typically include any data. Once the computers are done with the handshake, they're ready to receive packets containing actual data.

### SENDING PACKETS OF DATA
---

IMAGE DEMONSTRATE THE PROCESS OF SHARING OF DATA

>[!NOTE]
>The first computer sends a packet with data and a sequence number. 
>The second computer acknowledges it by setting the ACK bit and increasing the acknowledgement number by the length of the received data.


![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116171448.png)

### SEQUENCE AND ACKNOWLEDGEMENT DATA
---

>[!NOTE]
>When a packet of data is sent over TCP, the recipient must always acknowledge what they received. The first computer sends a packet with data and a sequence number. The second computer acknowledges it by setting the ACK bit and increasing the acknowledgement number by the length of the received data.


The sequence and acknowledgement numbers are part of the TCP header :

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116171453.png)

Those two numbers help the computers to keep track of which data was successfully received, which data was lost, and which data was accidentally sent twice.

### TCP Closing a Connection :
---

- TCP will close a connection once a device has determined that the other device has successfully received all of the data
- Either computer can close the connection when they no longer want to send or receive data
- Because TCP reserves system resources on a device, it is best practice to close TCP connections as soon as possible
- To initiate the closure of a TCP connection, the device will send a **FIN** packet to the other device
- The other device will have to acknowledge this packet

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116171502.png)

>[!NOTE]
>A computer initiates closing the connection by sending a packet with the FIN bit set to 1 (FIN = finish). The other computer replies with an ACK and another FIN. After one more ACK from the initiating computer, the connection is closed.

[CHECK THIS OUT FOR MORE INFO ON 3 WAY HANDSHAKE !](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet/xcae6f4a7ff015e7d:transporting-packets/a/transmission-control-protocol--tcp)

# 16. UDP/IP
---

- **U**ser **D**atagram **P**rotocol (**UDP**) is another protocol that is used to communicate data between devices.
- UDP is a **stateless** protocol that doesn't require a constant connection between the two devices for data to be sent. No acknowledgement is sent during a connection.
- Three-way handshake does not occur, nor is there any synchronisation between the two devices
- UDP is used in situations where applications can tolerate data being lost (such as video streaming or voice chat) or in scenarios where an unstable connection is not the end-all
- UDP provides a mechanism to detect corrupt data in packets
- it does not attempt to solve other problems that arise with packets, such as lost or out of order packets
- UDP is sometimes known as the Unreliable Data Protocol
- UDP is simple but fast, at least in comparison to other protocols that work over IP
- It's often used for time-sensitive applications where speed is more important than accuracy

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116185613.png)

- No process takes place in setting up a connection between two devices
- No regard for whether or not data is received, and there are no safeguards such as those offered by TCP, such as data integrity
- UDP packets are much simpler than TCP packets and have fewer headers

Both protocols share some standard headers :

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116185719.png)

**On Linux and Unix systems you can issue the `lsof` command to see which processes is using UDP ports**

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116185938.png)

## UDP PACKET FORMAT
---

> [!NOTE]
> When sending packets using UDP over IP, the data portion of each IP PACKET is formatted as a **UDP segment**. Each UDP segment contains an 8-byte header and variable length data.


![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116190131.png)

>[!IMPORTANT]
>The first four bytes of the UDP header store the port numbers for the source and destination. 
>
>A networked device can receive messages on different virtual ports, similar to how an ocean harbor can receive boats on different ports. 
>
>The different ports help distinguish different types of network traffic.


[CHECK THIS OUT TO LEARN MORE ABOUT UDP](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet/xcae6f4a7ff015e7d:transporting-packets/a/user-datagram-protocol-udp)

## CAPTURING THREE WAY HANDSHAKE USING WIRESHARK
---

The figure below shows the 3-way-handshake packets captured by [Wireshark](https://www.wireshark.org/)
![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116191445.png)

[TO KNOW MORE ABOUT WIRESHARK, CLICK HERE](https://wiki.wireshark.org/)

# 17. PORTS
---

- Ports are an essential point in which data can be exchanged
- Networking devices use ports to enforce strict rules when communicating with one another
- When a connection has been established, any data sent or received by a device will be sent through these ports
- ports are a numerical value between **0** and **65535** (65,535).
- Because ports can range from anywhere between 0-65535, there quickly runs the risk of losing track of what application is using what port
- We associate applications, software and behaviours with a standard set of rules to avoid chaos
- **Internet Assigned Numbers Authority** (IANA) maintains Service Name and Transport Protocol Port Number Registry which lists all port number reservations
-  A service is said to be **listening** for a port when it has that specific port open
- Once a service has made a connection, the port is in an **established** state
- **Well-known ports** - 0 - 1023
- **Registered ports** - 1024 - 49,151
- **Dynamic ports** - 49,152 - 65,535
- These protocols only follow the standards.
- You can administer applications that interact with these protocols on a different port other than what is the standard (running a web server on 8080 instead of the 80 standard port).
- Applications will presume that the standard is being followed, so you will have to provide a **colon (:)** along with the port number.


>[!IMPORTANT]
>**PORT** is a communication endpoint. At the software level, within an operating system, a port is a logical construct that identifies a specific process or a type of network service.



| Port Number | Protocol | Transport Protocol |
| ----------- | -------- | ------------------ |
| 20/21       | FTP      | TCP                |
| 22          | SSH      | TCP                |
| 23          | Telnet   | TCP                |
| 25          | SMTP     | TCP                |
| 53          | DNS      | TCP/UDP            |
| 67          | DHCP     | UDP                |
| 69          | TFTP     | UDP                |
| 80          | HTTP     | TCP                |
| 110         | POP3     | TCP                |
| 135         | RPC      | TCP                |
| 137-139     | NetBIOS  | TCP/UDP            |
| 143         | IMAP     | TCP                |
| 161/162     | SNMP     | UDP                |
| 389         | LDAP     | TCP/UDP            |
| 443         | HTTPS    | TCP                |
| 445         | SMB      | TCP                |
| 514         | SYSLOG   | UDP                |

- **`netstat`** command shows open ports on computer
    - **netstat -an** displays connections in numerical form
    - **netstat -b** displays executables tied to the open port (admin only)

[NEED DETAILS ON REMAINING PORTS, CLICK HERE !](https://www.vmaxx.net/techinfo/ports.htm)
[TO KNOW MORE ABOUT NETSTAT, CLICK HERE](https://docs.oracle.com/cd/E19504-01/802-5753/6i9g71m3i/index.html)



# 18. PORT FORWARDING
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116214157.png)

- Port forwarding is an essential component in connecting applications and services to the Internet. 
- Without port forwarding, applications and services such as web servers are only available to devices within the same direct network.
- When you set up port forwarding, you essentially tell your router to send some data straight to a specific device on your network, bypassing certain security processes.
- This can potentially increase your speeds and offer a number of other benefits.
- Port forwarding opens specific ports
- Port forwarding is configured at the router of a network

>[!IMPORTANT]
>Port forwarding is a network configuration technique that enables external devices to access services on a private network, which otherwise wouldn’t be directly accessible from the outside. 
>
>With port forwarding, you can connect from a local computer to another server

[CHECK OUT THIS NORDVPN RESOURCE TO LEARN MORE](https://nordvpn.com/blog/port-forwarding/)

# 19. FIREWALLS
---

![Image](https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116221037.png)

- A firewall is a device within a network responsible for determining what traffic is allowed to enter and exit. 
- An administrator can configure a firewall to **permit** or **deny** traffic from entering or exiting a network based on numerous factors such as:
	- Has the firewall been told to accept/deny traffic from a specific network
	- Has the firewall been told to accept/deny traffic destined for a specific network
	- Has the firewall been told to accept/deny traffic destined for port 80 only
	- Has the firewall been told to accept/deny traffic that is UDP, TCP or both
- Firewalls perform packet inspection to determine the answers to these questions.
- A firewall is a network security device designed to monitor, filter, and control incoming and outgoing network traffic based on predetermined security rules.
- The primary purpose of a firewall is to establish a barrier between a trusted internal network and untrusted external networks.
- Firewalls come in both hardware that can handle a magnitude of data to residential routers and software software such as Snort
- Organizations can configure these rules to permit or deny traffic based on various criteria, such as source and destination IP addresses, port numbers, and protocol type.
## TYPES OF FIREWALL
---

### Static Packet-Filtering Firewall
---

- Static packet-filtering firewalls, also known as stateless inspection firewalls, operate at the OSI network layer (layer 3). 
- These offer basic filtering by checking all individual data packets sent across a network, based on where they're from and where they're attempting to go. 
- Previously accepted connections are not tracked. This means each connection must be re-approved with every data packet sent.
- Filtering is based on IP addresses, ports, and packet protocols.
- These firewalls prevent two networks from directly connecting without permission.
- Rules for filtering are set based on a manually created access control list. 
- These are very rigid and it is difficult to cover unwanted traffic appropriately without compromising network usability. 
- Static filtering requires ongoing manual revision to be used effectively. This can be manageable on small networks but can quickly become difficult on larger ones.
- Inability to read application protocols means the contents of a message delivered within a packet cannot be read. Without reading the content, packet-filtering firewalls have a limited quality of protection.

### Circuit-Level Gateway Firewall
---

- Circuit-level gateways operate on the session level (layer 5). 
- These firewalls check for functional packets in an attempted connection, and if operating well will permit a persistent open connection between the two networks.
- The firewall stops supervising the connection after this occurs.
- Aside from its approach to connections, the circuit-level gateway can be similar to proxy firewalls.
- The ongoing unmonitored connection is dangerous, as legitimate means could open the connection and later permit a malicious actor to enter uninterrupted.

### Stateful Inspection Firewall
---

- Stateful inspection firewalls, also called dynamic packet-filtering firewalls, are unique from static filtering in their ability to monitor ongoing connections and remember past ones. 
- These began by operating on the transport layer (layer 4) but nowadays, these firewalls can monitor many layers, including the application layer (layer 7).
- Like the static filtering firewall, stateful inspection firewalls allow or block traffic based on technical properties, such as specific packet protocols, IP addresses, or ports. 
- These firewalls also uniquely track, and filter based on the state of connections using a state table.
- This firewall updates filtering rules based on past connection events logged in the state table by the screening router.
- Filtering decisions are often based on the administrator's rules when setting up the computer and firewall. 
- The state table allows these dynamic firewalls to make their own decisions based on previous interactions it has ‘learned’ from. For example, traffic types that caused disruptions in the past would be filtered out in the future. 
- Stateful inspection's flexibility has cemented it as one of the most ubiquitous types of shields available.

### Proxy Firewall
---

- Proxy Firewalls, also known as application-level firewalls (layer 7), are unique in reading and filtering application protocols. 
- These combine application-level inspection, or ‘deep packet inspection (DPI),’ and stateful inspection.
- A proxy firewall is as close to an actual physical barrier as it's possible to get. 
- It acts as an additional two hosts between external networks and internal host computers, with one as a representative (or ‘proxy’) for each network.
- Filtering is based on application-level data rather than just IP addresses, ports, and basic packet protocols (UDP, ICMP) like in packet-based firewalls. 
- It essentially looks at and evaluates incoming data. If no problem is detected, the data is allowed to pass through to the user.
- The downside to this kind of heavy security is that it sometimes interferes with incoming data that isn't a threat, leading to functionality delays.

### Next-Generation Firewall (NGFW)
---

- It combines the features of a traditional firewall with network intrusion prevention systems.
- Threat-specific next-generation firewalls are designed to examine and identify specific threats, such as advanced malware, at a more granular level. 
- More frequently used by businesses and sophisticated networks, they provide a holistic solution to filtering out threats.

### Hybrid Firewall
---

As implied by the name, hybrid firewalls use two or more firewall types in a single private network.

CHECK THESE OUT TO READ MORE ON FIREWALL
1. **KASPERSKY** : [CLICK HERE](https://www.kaspersky.com/resource-center/definitions/firewall)
2. **CLOUDFLARE** : [CLICK HERE](https://www.cloudflare.com/learning/security/what-is-a-firewall/)
3. **NIST** : [CLICK HERE](https://csrc.nist.gov/glossary/term/firewall)
4. **CISCO** : [CLICK HERE](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-firewall.html)
5. **FORTINET** : [CLICK HERE](https://www.fortinet.com/resources/cyberglossary/firewall#:~:text=A firewall is a network,network and untrusted external networks.)
# 20. VPN
---

- A **V**irtual **P**rivate **N**etwork ( **VPN** ) is a technology that allows devices on separate networks to communicate securely by creating a dedicated path between each other over the Internet (known as a tunnel). 
- Devices connected within this tunnel form their own private network.
- The encrypted connection helps ensure that sensitive data is safely transmitted. 
- It prevents unauthorized people from eavesdropping on the traffic and allows the user to conduct work remotely.
- VPNs are using tunneling protocols that act as rules for sending the data. 
- It provides detailed instructions on packaging the data and what checks to perform when it reaches its destination. 
- These different methods directly affect the process speed and security.

> [!IMPORTANT]
>
> A Virtual Private Network is a way to create a secure "tunnel" between two networks
> VPNs are also commonly used for an employee to log into their workplace when they are not on site (such as working from home or travelling for business matters)
> VPNs are also used where networks (such as coffee shops) do not provide encryption, and are a great way of preventing others from reading your network traffic.
## Most common VPN protocols
---
### Internet Protocol Security (IPSec)
---

- IPSec is a VPN tunneling protocol that secures data exchange by enforcing session authentication and data packet encryption. 
- It is twofold encryption — the encrypted message sits in the data packet, which is further encrypted again. 
- IPSec protocol combines with other protocols for added security and frequently utilizes Site-to-site VPN setups due to its high compatibility.

### Layer 2 Tunneling Protocol (L2TP)
---

- L2TP works by generating a secure tunnel between two L2TP connection points. 
- Once established, it uses an additional tunneling protocol to encrypt the sent data, i.e., IPSec. L2TP's complex architecture helps to ensure high security of the exchanged data. 
- It's another popular choice for Site-to-site setups, especially when higher security is needed.

### Point to Point Protocol (PPP)
---

- This technology is used by PPTP to allow for authentication and provide encryption of data. 
- VPNs work by using a private key and public certificate (similar to **SSH**). 
- A private key & certificate must match for you to connect.
- This technology is not capable of leaving a network by itself (non-routable).

### Point–to–Point Tunneling Protocol (PPTP)
---

- PPTP is another tunneling protocol that creates a tunnel with a PPTP cipher. 
- Since the creation of the cipher in the '90s, the computing power has increased exponentially. 
- Brute-forcing the cipher wouldn't take too long to crack it to reveal the exchanged data. 
- For this reason, technology rarely uses this cipher — a replacement containing more secure tunneling protocols with more advanced encryption is preferable.

### SSL and TLS
---

- Secure Socket Layer and Transport Layer Security protocols are the same standard that encrypts HTTPS web pages. 
- Web browser acts as the client, and user access is limited to specific applications rather than the entire network. 
- No additional software is usually required. Usually, remote access VPNs use SSL/TLS.

### OpenVPN
---

- OpenVPN is an open-source enhancement of the SSL/TLS framework with additional cryptographic algorithms to make your encrypted tunnel even safer. 
- It's the go-to tunneling protocol for its high security and efficiency. 
- Though, compatibility and setup can be a bit hit or miss as you won't be able to install it natively on many devices to form router to router VPN networks. So, the performance may vary.
- It comes in User Datagram Protocol (UDP) or Transmission Control Protocol (TCP) versions.
- UDP is faster because it uses fewer data checks, while TCP is slower but better protects data integrity.
- OpenVPN is a well-rounded and secure tunneling protocol and is popular for both remote access and site-to-site virtual private network uses.

### Secure Shell (SSH)
---

- SSH generates an encrypted connection and allows port forwarding to remote machines via a secured channel. 
- It is useful for accessing your office desktop via your laptop at home. 
- While it does add additional flexibility, SSH channels should always be under close supervision to provide a direct entry point for breach. That's why it's a better fit only in remote access setups.

### Wireguard
---

- The most recent widely available tunneling protocol is less complex but much more efficient and safer than IPSec and OpenVPN. 
- It relies on highly streamlined code to squeeze the best possible performance with a minimal margin of error. 
- While it still is in the early adoption stage, you could find offices using Site-to-site connections based on Wireguard. 


BELOW ARE SOME RESOURCES THAT YOU MIGHT FIND INTERESTING
1. [KASPERSKY](https://www.kaspersky.com/resource-center/definitions/what-is-a-vpn)
2. [MICROSOFT](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-vpn)
3. [CISCO](https://www.cisco.com/c/en_in/products/security/vpn-endpoint-security-clients/what-is-vpn.html#~how-a-vpn-works)
4. [NORD VPN](https://nordvpn.com/what-is-a-vpn/)
5. [FORTINET](https://www.fortinet.com/resources/cyberglossary/what-is-a-vpn)

# 21. DNS
---

- DNS (Domain Name System) provides a simple way for us to communicate with devices on the internet without remembering complex numbers.
- It is the protocol responsible for resolving hostnames, such as tryhackme.com, to their respective IP addresses.
- Each device connected to the Internet has a unique IP address which other machines use to find the device. 
- DNS servers eliminate the need for humans to memorize IP addresses such as 192.168.1.1 (in IPv4), or more complex newer alphanumeric IP addresses such as 2400:cb00:2048:1::c629:d7a2 (in IPv6).
- The process of DNS resolution involves converting a hostname into a computer-friendly IP address.
- An IP address is given to each device on the Internet, and that address is necessary to find the appropriate Internet device.

## DOMAIN HIERARCHY
---

### TLD (Top-Level Domain)
---

- A TLD is the most righthand part of a domain name. So, for example, the example.com TLD is **.com**. 
- There are two types of TLD, gTLD (Generic Top Level) and ccTLD (Country Code Top Level Domain). 
- A gTLD was meant to tell the user the domain name's purpose; for example, a .com would be for commercial purposes, .org for an organisation, .edu for education and .gov for government. 
- A ccTLD was used for geographical purposes, for example, .ca for sites based in Canada, .co.uk for sites based in the United Kingdom and so on. 
- Due to such demand, there is an influx of new gTLDs ranging from .online , .club , .website , .biz and so many more. 

### Second-Level Domain
---

- Taking example.com as an example, the **.com** part is the TLD, and **example** is the Second Level Domain. 
- When registering a domain name, the second-level domain is limited to 63 characters + the TLD and can only use a-z 0-9 and hyphens (cannot start or end with hyphens or have consecutive hyphens).

### Subdomain
---

- A subdomain sits on the left-hand side of the Second-Level Domain using a period to separate it; for example, in the name **abc.example.com** the **abc** part is the **subdomain**. 
- A subdomain name has the same creation restrictions as a Second-Level Domain, being limited to 63 characters and can only use a-z 0-9 and hyphens (cannot start or end with hyphens or have consecutive hyphens).
- You can use multiple subdomains split with periods to create longer names, such as **alphabet.abcd.example.com**. But the length must be kept to 253 characters or less.
- There is no limit to the number of subdomains you can create for your domain name.



For a full list of over 2000 TLDs [click here](https://data.iana.org/TLD/tlds-alpha-by-domain.txt).

## DNS RECORDS
---

>[!IMPORTANT]
>A Domain Name System (DNS) record is a set of instructions used to connect domain names with internet protocol (IP) addresses within DNS servers

The most common types of DNS records are:
### A records
---

- Address records, or A records, are the most common DNS records used. 
- They create a direct connection between an IPv4 address and a domain name. 

### AAAA records
---

- This type of record connects domain names to IPv6 addresses. 
- IPv6 addresses have more numerals than IPv4 address and are becoming more common as options for IPv4 addresses are running out.

### CNAME records
---

- Canonical name records, or CNAME records, direct an alias domain to a canonical domain. 
- This means that this type of record is used to link subdomains to domain A or AAAA records.  
- For example, instead of creating two A records for www.example.com and product.example.com, you could link product.example.com to a CNAME record that is then linked to an A record for example.com. 
- The value is that if the IP address changes for the root domain, only the A record will have to be updated and the CNAME will update accordingly.

### DNAME records
---

- Delegation name records, or DNAME records, are used to redirect multiple subdomains with one record and point them to another domain. 
- For example, a DNAME record linking domain.com to example.com will link product.domain.com, trial.domain.com, and blog.domain.com to example.com. 
- These records are helpful in managing largescale domains and in managing domain name changes by ensuring subdomains are properly linked.

### CAA records
---

- Certification authority authorization records, or CAA records, allow domain owners to specify which certificate authorities (CAs) can issue certificates for their domain. 
- A CA is an organization that validates the identity of websites and connects them to cryptographic keys by issuing digital certificates.

### CERT records
---

- Certificate, or CERT records, store certificates that verify the authenticity of all parties involved. 
- This type of record is particularly valuable when securing and encrypting sensitive information.

### MX records
---
 
 - Mail exchange, or MX records, direct emails to your domain mail server. 
 - These records, along with an email server, allow for the creation of individual email accounts, such as user@example.com, that are linked to the domain (example.com).

### NS records
---

- Nameserver, or NS records, show which DNS server is acting as the authoritative nameserver for your domain. 
- Authoritative nameservers contain the final information about a specific domain and its corresponding IP address. 
- An NS record points to all of the different records your domain holds. 
- Without NS records, users will not be able to access your website.

### SOA records
---

- Start of authority, or SOA records, store important administrative information about a domain. 
- This information can include the domain administrator’s email address, information on domain updates and when a server should refresh its information.

### PTR records
---

- Pointer records, or PTR records, work in the opposite direction of A records. 
- They are used to connect an IP address with a domain name, instead of a domain name with an IP address. 
- When a DNS lookup begins with an IP address, it then finds the corresponding hostname. 
- These records are used to detect spam by checking if the IP addresses and associated email addresses are used by legitimate email servers. 
- PTR records must be set up by the server host.

### SPF records
---

- Sender policy framework, or SPF records, are used to identify the mail servers that can send emails through your domain. 
- This helps prevent your domain from being used by spammers or for malicious purposes by letting email receivers know that what they are receiving has been authorized.

### SRV records
---

- Service, or SRV records, identify a host and port for specific services, such as messaging, for a domain. 
- Ports are virtual connection points that allow digital devices to separate different types of traffic.

### ALIAS record
---

- ALIAS records are used to direct your domain name to a host name and not an IP address. 
- For instance, if your domain name is example.com, you can point it to product.differentexample.com using an ALIAS record.  

### NSEC records
---

- Next secure records, or NSEC records, allow for proof of non-existence.
- This means that these records exist to confirm that other records do not exist. 
- Being able to confirm the non-existance of a record saves time when searching for specific records.

### URLFWD records
---

- URL forwarding (or URL redirecting) is a technique used to make a single web page available via multiple URLs. 
- NS1 Connect users can easily set up URL forwarding (HTTP redirects or masking) between zones. 
- There are three types of URL redirects: Permanent (301), temporary (302), or masking.

### TXT records
---

- Text, or TXT records, store textual information related to domains and subdomains. 
- Text records allow for the storage of SPF records and email verification records. 
- DKIM and DMARC records, which are stored in TXT records, help email servers confirm that a message is coming from a reliable source.

## WHAT HAPPENS WHEN YOU MAKE A DNS REQUEST
---

- When you request a domain name, your computer first checks its local cache to see if you've previously looked up the address recently; if not, a request to your Recursive DNS Server will be made.
- A Recursive DNS Server is usually provided by your ISP, but you can also choose your own. This server also has a local cache of recently looked up domain names. If a result is found locally, this is sent back to your computer, and your request ends here (this is common for popular and heavily requested services such as Google, Facebook, Twitter).
- If the request cannot be found locally, a journey begins to find the correct answer, starting with the internet's root DNS servers.
- The root servers act as the DNS backbone of the internet; their job is to redirect you to the correct Top Level Domain Server, depending on your request. If, for example, you request www.example.com, the root server will recognise the Top Level Domain of .com and refer you to the correct TLD server that deals with .com addresses.
-The TLD server holds records for where to find the authoritative server to answer the DNS request. The authoritative server is often also known as the nameserver for the domain. You'll often find multiple nameservers for a domain name to act as a backup in case one goes down.
- An authoritative DNS server is the server that is responsible for storing the DNS records for a particular domain name and where any updates to your domain name DNS records would be made.
- Depending on the record type, the DNS record is then sent back to the Recursive DNS Server, where a local copy will be cached for future requests and then relayed back to the original client that made the request.
- DNS records all come with a TTL (Time To Live) value. This value is a number represented in seconds that the response should be saved for locally until you have to look it up again. Caching saves on having to make a DNS request every time you communicate with a server.
