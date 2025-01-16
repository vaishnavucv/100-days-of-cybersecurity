>[!WARNING]
Images used in this file are not owned or made by me and are copied from internet. The Sources of the image have been provided below. The document is completely for educational and illustrational purposes only.
 
 <h1 style="color:cadetblue">OBJECTIVES</h1>
- Learn core concepts of how computers communicate with each other
- Deeply understand the 

<h1 style="color:cadetblue">SYNOPSIS</h1>
1. **INTRODUCTION**
2. What is **INTERNET**
3. IDENTIFYING DEVICES ON A NETWORK
	a. **IP ADDRESS**
	b. **MAC ADDRESS**
	

# 1. INTRODUCTION
---
A **NETWORK** consists of 2 or more computers linked to share resources. These devices include everything from your laptop and phone to security cameras, traffic lights, and even farming.   They are the basis of communication in IT. Networks are integrated into our everyday life. Because networks are so embedded in modern-day, networking is an essential concept in Cyber Security. 

> [!Network]
> **COMPUTER NETWORK** 
> SET OF COMPUTERS THAT ARE CONNECTED TOGETHER SO AS TO SHARE INFORMATION


![[Images/Pasted image 20250115221827.png]]

**Source : Random pages on Internet**


# 2. WHAT IS INTERNET
---
Internet is one giant network that consists of many, many small networks within itself. The first iteration of **INTERNET** was within the **ARPANET** project in the late 1960s. Advanced Research Project Agency Network was the first public packet-switched computer network! Main use was for academic and research purposes. It was decommissioned in the late 1980s.

A side benefit of ARPANET's design was that because messages could be routed or rerouted in more than one direction, the network could continue to function even if parts of it were destroyed in the event of a military attack or other disaster. This project was funded by the United States Defence Department and was the first documented network in action. 

However, it wasn't until 1989 when the **INTERNET** as we know it was invented by Tim Berners Lee by the creation of the **W**orld **W**ide **W**eb (**WWW**). It wasn't until this point that the Internet started to be used as a repository for storing and sharing information, just like it is today.


>[!INTERNET]
> **INTERNET** aka **NET** is worldwide system of interconnected Computer Networks and Electronic Devices that communicate with each other using an established set of **PROTOCOLS**.


![[Images/Pasted image 20250115222650.png]]**Source : Britannica**

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

![[Images/Pasted image 20250115224629.png]]
**Source : HOSTWINDS**


An **IP ADDRESS** is a set of numbers that are divided into four octets. The value of each octet will summarise to be the IP address of the device on the network. This number is calculated through a technique known as **IP ADDRESSING & SUBNETTING**. IP addresses can change from device to device but cannot be active simultaneously more than once within the same network. 

IP Addresses follow a set of standards known as protocols. These protocols are the backbone of networking and force many devices to communicate in the same language. 

A device can be on both a private and public network. Depending on where they are will determine what type of IP address they have: 

- **GLOBAL or PUBLIC or EXTERNAL IP ADDRESS** : Identify the device on the Internet. This group can also be called 'WAN addresses' .
- **PRIVATE or LOCAL or INTERNAL IP ADDRESS** : Identify a device amongst other devices. These are used in the local network (LAN). They are not routed on the Internet and no traffic can be sent to them from the Internet, they only supposed to work within the local network


![[Images/Pasted image 20250115225243.png]]
**SOURCE : GEOTARGETLY**

> [!Note]
> An **Internet Protocol Address (IP ADDRESS)** is a unique address that identifies a device on the internet or a local network. IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network


![[Images/Pasted image 20250115230725.png]]
**Source : Tryhackme**, not my real IP or MAC Address!

These two devices will be able to use their private IP addresses to communicate with each other. However, any data sent to the Internet from either of these devices will be identified by the same public IP address. Public IP addresses are given by your **I**nternet **S**ervice **P**rovider (or **ISP**) at a monthly fee (your bill!).

As more and more devices become connected, it is becoming increasingly harder to get a public address that isn't already in use. Cisco, an industry giant in the world of networking, estimated that there would be approximately 50 billion devices connected on the Internet by the end of 2021. 

We have only discussed one version of the Internet Protocol addressing scheme known as IPv4, which uses a numbering system of 2^32 IP addresses (4.29 billion), still there will be a shortage!

IPv6 is a new iteration of the Internet Protocol addressing scheme to help tackle this issue. It supports up to 2^128 of IP addresses (340 trillion-plus), resolving the issues faced with IPv4 and is more efficient due to new methodologies.

## IPv4
---
![[Images/Pasted image 20250115231813.png]]
**Source : Tryhackme**, not my real IP or MAC Address!

## IPv6
----
![[Images/Pasted image 20250115232224.png]]
**Source : Tryhackme**, not my real IP Address!

## IPv4 vs IPv6
---
![[Images/Pasted image 20250115232533.png]]
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
![[Images/Pasted image 20250115235710.png]]
>**Source : Internet**


![[Images/Pasted image 20250115235335.png]]
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

## NAT : Network Address Translation
---
NAT stands for network address translation. It’s a way to map multiple private addresses inside a local network to a public IP address before transferring the information onto the internet. Organisations that want multiple devices to employ a single IP address use NAT, as do most home routers. 

>[!NOTE]
>It is a process in which one or more local IP addresses are translated into one or more Global IP addresses and vice versa to provide Internet access to the local hosts. It also does the translation of port numbers, i.e., masks the port number of the host with another port number in the packet that will be routed to the destination. 

It then makes the corresponding entries of IP address and port number in the NAT table. NAT generally operates on a router or firewall. If NAT runs out of addresses, i.e., no address is left in the pool configured then the packets will be dropped and an Internet Control Message Protocol (ICMP) host unreachable packet to the destination is sent.

The router which has one interface in the local (inside) network and one interface in the global (outside) network. When a packet traverse outside the local (inside) network, then NAT converts that local (private) IP address to a global (public) IP address. When a packet enters the local network, the global (public) IP address is converted to a local (private) IP address.

Suppose, in a network, two hosts A and B are connected. Now, both of them request for the same destination, on the same port number, say 1000, on the host side, at the same time. If NAT does only translation of IP addresses, then when their packets will arrive at the NAT, both of their IP addresses would be masked by the public IP address of the network and sent to the destination. Destination will send replies to the public IP address of the router. Thus, on receiving a reply, it will be unclear to NAT as to which reply belongs to which host (because source port numbers for both A and B are the same). Hence, to avoid such a problem, NAT masks the source port number as well and makes an entry in the NAT table.(**Source : GFG**)

![[https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116104057.png]]

Inside refers to the addresses which must be translated. Outside refers to the addresses which are not in control of an organization. These are the network Addresses in which the translation of the addresses will be done.

- **Inside local address** An IP address that is assigned to a host on the Inside (local) network. The address is probably not an IP address assigned by the service provider i.e., these are private IP addresses. This is the inside host seen from the inside network. 
- **Inside global address** IP address that represents one or more inside local IP addresses to the outside world. This is the inside host as seen from the outside network. 
- **Outside local address** This is the actual IP address of the destination host in the local network after translation. 
- **Outside global address This is the outside host as seen from the outside network. It is the IP address of the outside destination host before translation.

### Network Address Translation (NAT) Types

There are 3 ways to configure NAT: 

#### Static NAT
---
 In this, a single unregistered (Private) IP address is mapped with a legally registered (Public) IP address i.e one-to-one mapping between local and global addresses. This is generally used for Web hosting. These are not used in organizations as there are many devices that will need Internet access and to provide Internet access, a public IP address is needed. 

Suppose, if there are 3000 devices that need access to the Internet, the organization has to buy 3000 public addresses that will be very costly. 

#### Dynamic NAT
---
In this type of NAT, an unregistered IP address is translated into a registered (Public) IP address from a pool of public IP addresses. If the IP address of the pool is not free, then the packet will be dropped as only a fixed number of private IP addresses can be translated to public addresses. 

Suppose, if there is a pool of 2 public IP addresses then only 2 private IP addresses can be translated at a given time. If 3rd private IP address wants to access the Internet then the packet will be dropped therefore many private IP addresses are mapped to a pool of public IP addresses. NAT is used when the number of users who want to access the Internet is fixed. This is also very costly as the organization has to buy many global IP addresses to make a pool. 

#### Port Address Translation (PAT)
---
This is also known as NAT overload. In this, many local (private) IP addresses can be translated to a single registered IP address. Port numbers are used to distinguish the traffic i.e., which traffic belongs to which IP address. This is most frequently used as it is cost-effective as thousands of users can be connected to the Internet by using only one real global (public) IP address.

### SUBNETTING
---
Subnetting is the process of creating a subnetwork (also known as a subnet) within a network. Network interfaces and devices within a subnet can communicate with each other directly. Routers facilitate communication between different subnets. Subnets provides each group of devices have thier own space to communicate, that ultimately helps network to work easily.This also boosts security and makes it easier to manage the network, as each subnet can be monitored and controlled separately.

>[!NOTE]
>A subnet is like a smaller group within a large network. It is a way to split a large network into smaller networks so that devices present in one network can transmits data more easily. Subnet makes the network faster and easier to manage and also improves the security of the network.

![[https://github.com/rockin-buddha/100-days-of-cybersecurity/blob/main/Notes/Day-02/Images/Pasted%20image%2020250116111029.png]]

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

The working of subnets starts in such a way that firstly it divides the subnets into smaller subnets. For communicating between subnets, routers are used. Each subnet allows its linked devices to communicate with each other. Subnetting for a network should be done in such a way that it does not affect the network bits.

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

A **subnet mask** is a 32-bit number used in IP addressing to separate the network portion of an IP address from the host portion. It helps computers and devices determine which part of an IP address refers to the network they are present, and which part refers to their specific location or address within that network.

A point-to-point subnet is a particular type of subnet used in point-to-point links that facilitate direct communication between two routers. This subnet consists of a 31-bit subnet mask, leaving only two possible addresses in the network. Since point-to-point subnets contain only one host, a different broadcast address isn’t necessary.

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
