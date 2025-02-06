import datetime
import http.client
import re
import socket
import ssl
import urllib.parse
import base64

class DomainScanner:
    def log(self, message):
        with open(self.scanResult, "a") as log:
            log.write(message + "\n")
        print(message)

    def checkPort (self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.settimeout(2)
                return sock.connect_ex((self.domain, port)) == 0
            except Exception as e:
                self.log(f"  - Port {port} Scan Failed: {e}")

    def __init__ (self, domain):
        domain = domain.lower()
        domain = re.sub(r'https?://', '', domain)
        domain = domain.split('/')[0]
        domain = domain.split(':')[0]
        self.domain = domain
        domainSanitised = re.sub(r'[^a-zA-Z0-9-]', '_', domain)
        self.scanResult = f"Scan Results for {domainSanitised}.txt"
        self.log(f"Scan for '{domain}' Started at {datetime.datetime.now()}\n\n=====")

    def portScanning(self):
        self.log("\n[+] Performing Port Scan...\n")
        ports = [
            1000, 10000, 10001, 1001, 10011, 10101, 1080, 1099, 110, 11011, 1111, 11211, 119, 1194, 123, 123, 1234,
            12345, 12543, 12931, 1337, 143, 1433, 1434, 15000, 1521, 1555, 161, 162, 177, 18000, 194, 20, 2000, 20000,
            20002, 2005, 2020, 2048, 20480, 20481, 20490, 21, 2101, 2121, 21345, 22, 2222, 23, 2323, 2345, 25, 25000,
            2545, 2546, 27017, 27018, 28017, 3000, 30000, 303, 3030, 30303, 30304, 3060, 3128, 31337, 3306, 33333, 3389,
            3434, 34343, 3600, 3690, 4000, 40000, 4011, 4020, 4040, 4200, 4242, 4321, 443, 4433, 4443, 4444, 44444, 445,
            45000, 45010, 4554, 4848, 500, 5000, 5050, 50500, 50505, 5060, 5101, 5150, 520, 53, 5335, 5353, 5432, 54321,
            5522, 5555, 55555, 5632, 5858, 587, 5900, 5985, 5986, 6000, 60000, 631, 6379, 65430, 65431, 65432, 6660,
            6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669, 6670, 6680, 6697, 6699, 67, 6789, 68, 69, 7000, 7070,
            7171, 7777, 7778, 7800, 80, 8000, 8080, 8088, 8443, 8888, 9000, 9001, 9035, 9080, 9090, 9876, 993, 995, 999,
            9999,
            ]
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                try:
                    sock.settimeout(2)
                    result = sock.connect_ex((self.domain, port))
                    if result == 0:
                        self.log(f"  - Port {port} is OPEN")
                    else:
                        print(f"  - Port {port} is CLOSED")
                except Exception as e:
                    self.log(f"  - Port {port} Scan Failed: {e}")
                    

    def checkSSL(self):
        self.log("\n[+] Checking SSL Certificate...\n")
        if not self.checkPort(443):
            self.log("  - Port 443 is CLOSED. Skipping SSL Check.")
            return
        try:
            ctx = ssl.create_default_context()
            with ctx.wrap_socket(socket.socket(), server_hostname=self.domain) as sock:
                sock.connect((self.domain, 443))
                cert = sock.getpeercert()
                expiry = cert['notAfter']
                self.log(f"  - SSL Certificate Valid Until: {expiry}")
        except Exception as e:
            self.log(f"  - SSL Check Failed: {e}")
    
    def checkHTTPHeaders(self):
        self.log("\n[+] Checking HTTP Headers...\n")
        if not self.checkPort(443):
            self.log("  - Port 443 is CLOSED. Skipping HTTPS Headers Check.")
            return
        try:
            connection = http.client.HTTPSConnection(self.domain)
            connection.request("GET", "/")
            response = connection.getresponse()
            headers = response.getheaders()
            connection.close()
            for header, value in headers:
                self.log(f"  - {header}: {value}")
        except Exception as e:
            self.log(f"  - HTTP Headers Check Failed: {e}")
    
    def checkXSS(self):
        self.log("\n[+] Checking for Cross-site Scripting Vulnerabilities...\n")
        payloads = [
            "<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>", "<svg onload=alert('XSS')>",
            "javascript:alert('XSS')", base64.b64encode("<script>alert('XSS')</script>".encode()).decode(),
            "<ScRiPt>alert('XSS')</ScRiPt>", "<SCRIPT>alert('XSS');</SCRIPT>", 
            "<scr<script>ipt>alert('XSS')</scr</script>ipt>", "' onmouseover='alert('XSS')",
            "\" onmouseover=\"alert('XSS')", "' onfocus='alert('XSS')", "\"><iframe src=\"javascript:alert('XSS')\">",
            "\"><video><source onerror=\"alert('XSS')\">", "';alert('XSS')//", "\";alert('XSS')//",
            "><script>alert(String.fromCharCode(88,83,83))</script>",
        ]
        contexts = [
            ("/?q={}", "GET"),
            ("/search?query={}", "GET"),
            ("/login?username={}&password=test", "POST"),
            ("/comment?text={}", "POST")
        ]
        patterns = [
            "customAlert", "sanitize", "escapeHTML", "innerHTML", "document.write",
        ]
        headers = { 
            "User-Agent": "Mozilla/5.0", "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        for payload in payloads:
            for template, method in contexts:
                try:
                    payloadEncoded = urllib.parse.quote(payload)
                    path = template.format(payloadEncoded)
                    connection = http.client.HTTPConnection(self.domain)
                    if method == "GET":
                        connection.request(method, path, headers=headers)
                    else:
                        body = f"data={payloadEncoded}"
                        connection.request(method, path, body=body, headers=headers)
                    response = connection.getresponse()
                    content = response.read().decode(errors="ignore")
                    connection.close()
                    if payload in content or payloadEncoded in content:
                        self.log("  - Potential XSS (Reflected) Found!")
                        self.log(f"    Path: {path}")
                        self.log(f"    Method: {method}")
                        self.log(f"    Payload: {payload}")
                    if "alert" not in content and "XSS" in content:
                        self.log("  - Potential Filter Bypass Found!")
                        self.log(f"    Path: {path}")
                        self.log(f"    Method: {method}")
                        self.log(f"    Payload: {payload}")
                    for pattern in patterns:
                        if pattern in content:
                            self.log(f"  - Suspicious Pattern Found: {pattern}")
                            self.log(f"    Path: {path}")
                            self.log(f"    Method: {method}")
                except Exception as e:
                    self.log(f"  - XSS Test Failed: {e}")
                    self.log(f"    Path: {path}")
                    self.log(f"    Method: {method}")

    def checkCSRF(self):
        self.log("\n[+] Checking for Basic Cross-Site Request Forgery...\n")
        try:
            connection = http.client.HTTPConnection(self.domain)
            connection.request("GET", "/")
            response = connection.getresponse()
            headers = response.getheaders()
            connection.close()
            content = response.read().decode(errors="ignore")
            CSRFHeaders = ["X-CSRF-Token", "CSRF-Token", "X-XSRF-Token",]
            CSRFPatterns = [
                r'<input[^>]*type=["\']hidden["\'][^>]*name=["\']csrf[^"\']*["\']',
                r'<input[^>]*name=["\']csrf[^"\']*["\'][^>]*type=["\']hidden["\']', 
                r'<meta[^>]*name=["\']csrf-token["\']',
            ]
            for header in CSRFHeaders:
                if header in headers:
                    csrf = True
                    self.log(f"  - Found CSRF Protection Header: {header}")
                else:
                    csrf = False
            for pattern in CSRFPatterns:
                if re.search(pattern, content, re.IGNORECASE):
                    csrf = True
                    self.log("  - Found CSRF Token in Form")
                else:
                    csrf = False
            if csrf == False:
                self.log("  - No CSRF Protection Detected!")
        except Exception as e:
            self.log(f"  - CSRF Check Failed: {e}")

    def checkSQLInjection(self):
        self.log("\n[+] Checking for Basic SQL Injection Vulnerabilities...\n")
        payloads = [
            "' OR '1'='1", "1' OR '1'='1", "1 OR 1=1", "' --", "1' --", "' UNION SELECT NULL--", "admin' --",
        ]
        patterns = [
            "sql", "mysql", "oracle", "syntax error", "postgresql", "sqlite", "database error",
            ]
        for payload in payloads:
            try:
                sql = False
                payloadEncoded = urllib.parse.quote(payload)
                connection = http.client.HTTPConnection(self.domain)
                connection.request("GET", f"/?id={payloadEncoded}")
                response = connection.getresponse()
                content = response.read().decode(errors="ignore").lower()
                connection.close()
                for pattern in patterns:
                    if pattern in content:
                        self.log(f"  - Potential SQL Injection Found with Payload: {payload}")
                        self.log(f"    Database Error Pattern: {pattern}")
                        sql = True
                if response.status == 500:
                    self.log(f"  - Potential SQL Injection Found! Server Error with Payload: {payload}")
                    sql = True
            except Exception as e:
                self.log(f"  - SQL Injection Test Failed for Payload {payload}: {e}")
        if sql == False:
            self.log("  - No Obvious SQL Injection Vulnerabilities Detected.")

    def checkDNSEnumeration(self):
        self.log("\n[+] Performing DNS Enumeration...\n")
        subdomains = [
            "www", "mail", "smtp", "imap", "pop3", "pop", "mxb", "aspmx", "mx", "alt", "inbound", "admin", "blog", 
            "dev", "test", "staging", "backup", "api", "portal", "cms", "support", "cdn", "shop", "meet", "team", 
            "learn", "promo", "store", "engage", "quote", "landing", "services", "hello", "try", "trial", "demo", 
            "sales", "m", "ftp", "wiki", "webmail", "kb", "help", "stage", "app",
        ]
        for subdomain in subdomains:
            domainFull = f"{subdomain}.{self.domain}"
            try:
                socket.setdefaulttimeout(3) 
                IPAddress = socket.gethostbyname(domainFull)
                self.log(f"  - Subdomain Found: {domainFull} -> {IPAddress}")
            except (socket.gaierror, socket.timeout, socket.error) as e:
                print(f"  - DNS Enumeration Failed for {domainFull}: {e}")
                continue
            except Exception as e:
                self.log(f"  - DNS Enumeration Failed for {domainFull}: {e}")

    def checkDirectories(self):
        self.log("\n[+] Checking for Directory Traversal Vulnerabilities...\n")
        payloads = [
            "../", "../../", "../../../", "../../../../", ".../", "%2e%2e%2f", "../" "..%2f", "..%252f", 
            "..%c0%af", "..\\", "..\\..\\", "/etc/passwd", "C:\\Windows\\system32\\config\\SAM",
        ]
        patterns = [
            "root:", "passwd", "windows", "system32", "etc/shadow", "boot.ini",
        ]
        for payload in payloads:
            try:
                payloadEncoded = urllib.parse.quote(payload)
                connection = http.client.HTTPConnection(self.domain)
                connection.request("GET", f"/download?file={payloadEncoded}")
                response = connection.getresponse()
                content = response.read().decode(errors="ignore").lower()
                connection.close()
                for pattern in patterns:
                    if pattern in content:
                        self.log("  - Potential Directory Traversal Found!")
                        self.log(f"    Payload: {payload}")
                        self.log(f"    Pattern: {payload}")
                if response.status in [200, 403, 500]:
                    self.log(f"  - Suspicious Response for Payload: {payload} (Status Code {response.status})")
            except Exception as e:
                self.log(f"  - Directory Traversal Test Failed for Payload {payload}: {e}")

    def runScan(self):
        self.portScanning()
        self.checkDNSEnumeration()
        self.checkDirectories()
        self.checkSSL()
        self.checkHTTPHeaders()
        self.checkXSS()
        self.checkCSRF()
        self.checkSQLInjection()
        self.log(f"\n=====\n\nScanning Completed at {datetime.datetime.now()}")

if __name__ == "__main__":
    domain = input("\nEnter Domain to Scan: ")
    scanner = DomainScanner(domain)
    scanner.runScan()