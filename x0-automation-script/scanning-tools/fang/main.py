import dns.resolver
import subprocess
import json
import whois
import threading
from queue import Queue
from tabulate import tabulate
from tqdm import tqdm
import os
from colorama import Fore, Style, init

init(autoreset=True)

banner = r"""
___________                       ___.               .___                         .__       .__                                                              
\_   _____/____    ____    ____   \_ |__ ___.__.   __| _/____ ___  _____.__. ____ |__|_____ |  |__   ___________                                             
 |    __) \__  \  /    \  / ___\   | __ <   |  |  / __|\__  \  \/ <   |  |/ ___\|  \____ \|  |  \_/ __ \_  __ \                                            
 |     \   / __ \|   |  \/ /_/  >  | \_\ \___  | / /_/ | / __ \\   / \___  \  \___|  |  |_> >   Y  \  ___/|  | \/                                            
 \___  /  (____  /___|  /\___  /   |___  / ____| \____ |(____  /\_/  / ____|\___  >__|   __/|___|  /\___  >__|                                               
     \/        \/     \/_____/        \/\/           \/     \/      \/         \/   |__|        \/     \/                                                    
                                                                                                                                                              
Fang: Unleash the Power of Precision Recon!
"""


print(Fore.RED + banner)


def find_subdomains(domain):
    try:
        subfinder_output_file = f"{domain}_subdomains.txt"
        subprocess.run(
            ["subfinder", "-d", domain, "-silent", "-o", subfinder_output_file],
            check=True,
            text=True,
        )
        with open(subfinder_output_file, "r") as file:
            subdomains = file.read().splitlines()
        return subdomains
    except subprocess.CalledProcessError as e:
        return f"Error running Subfinder: {e}"

def query_dns(domain, record_types):
    records = {}
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            records[record] = [answer.to_text() for answer in answers]
        except dns.resolver.NoAnswer:
            records[record] = []
        except Exception as e:
            records[record] = str(e)
    return records
def run_nmap(domain, output_file):
    try:
        subprocess.run(
            ["nmap", "-sC", "-sV", "-T4", "-oN", output_file, domain],
            check=True,
            text=True,
        )
        with open(output_file, "r") as file:
            return file.read()
    except subprocess.CalledProcessError as e:
        return f"Error running Nmap: {e}"


def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return f"Error retrieving WHOIS data: {e}"


def generate_report(domain, subdomains, dns_data, whois_data, nmap_data):
    report = {
        "Domain": domain,
        "Subdomains": subdomains,
        "DNS Records": dns_data,
        "WHOIS Data": str(whois_data),
        "Nmap Output": nmap_data,
    }

    
    json_file = f"{domain}_report.json"
    with open(json_file, "w") as file:
        json.dump(report, file, indent=4)


    html_file = f"{domain}_report.html"
    html_content = f"""
    <html>
    <head>
        <title>ReconWhiz Report - {domain}</title>
    </head>
    <body>
        <h1>ReconWhiz Report for {domain}</h1>
        <h2>Subdomains</h2>
        <pre>{json.dumps(subdomains, indent=4)}</pre>
        <h2>DNS Records</h2>
        <pre>{json.dumps(dns_data, indent=4)}</pre>
        <h2>WHOIS Data</h2>
        <pre>{whois_data}</pre>
        <h2>Nmap Output</h2>
        <pre>{nmap_data}</pre>
    </body>
    </html>
    """
    with open(html_file, "w") as file:
        file.write(html_content)

    print(f"[INFO] Reports saved: {json_file}, {html_file}")
def worker(domain, record_types, output_file, results):
    results["dns"] = query_dns(domain, record_types)
    results["nmap"] = run_nmap(domain, output_file)

def main():
    domain = input("Enter the domain to enumerate: ").strip()
    record_types = ["A", "AAAA", "MX", "NS", "SOA", "TXT", "CNAME", "SRV"]
    nmap_output_file = f"{domain}_nmap.txt"
    results = {}

    print("[INFO] Starting ReconWhiz...")
    threads = []
 print("[INFO] Finding subdomains...")
    subdomains = find_subdomains(domain)
  t1 = threading.Thread(target=worker, args=(domain, record_types, nmap_output_file, results))
    threads.append(t1)
    t1.start()
 t2 = threading.Thread(target=lambda: results.update({"whois": get_whois_info(domain)}))
    threads.append(t2)
    t2.start()
  for t in threads:
        t.join()
  print("[INFO] Generating reports...")
    generate_report(domain, subdomains, results.get("dns", {}), results.get("whois", "N/A"), results.get("nmap", "N/A"))

if __name__ == "__main__":
    main()
             
