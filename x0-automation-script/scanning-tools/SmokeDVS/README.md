# Domain Vulnerability Scanner v2.25

## Overview

The Domain Vulnerability Scanner is a portable Python-based tool designed to identify potential common security vulnerabilities in a given domain.

## Features

- **Port Scanning**: Checks for open ports and identifies associated services.
- **DNS Enumeration**: Detects common subdomains for the provided domain.
- **Directory Traversal**: Checks for directory traversal vulnerabilities.
- **SSL Certificate Validation**: Verifies the presence and validity of SSL certificates.
- **HTTP Header Analysis**: Checks for security-related HTTP headers.
- **Cross-Site Scripting (XSS)**: Tests for potential XSS vulnerabilities.
- **Cross-Site Request Forgery (CSRF)**: Checks for CSRF protection mechanisms.
- **SQL Injection**: Tests for basic SQL injection vulnerabilities.

## Requirements

- Python 3.x
- Standard Python libraries (`os`, `platform`, `datetime`, `http.client`, `re`, `socket`, `ssl`, `urllib.parse`, `base64`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/smokeshard/100-days-of-cybersecurity/
    cd 100-days-of-cybersecurity/x0-automation-script/scanning-tools/SmokeDVS
    ```

2. Run the scanner:
    ```bash
    python SmokeDVS.py
    ```

## Usage

1. Run the script and enter the domain you wish to scan when prompted.
2. The scanner will perform various security checks and log the results to a file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the __LICENSE__ file for details.

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Unauthorized use of this tool may violate laws and regulations. The author is not responsible for any misuse or damage caused by this tool.

## Contact

For any questions or feedback, please contact the author on Discord: @smokeshard
