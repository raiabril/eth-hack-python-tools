#!/usr/bin/env python3
"""
NMAP automation tool

This script is usin the python-nmap package to automate scan.


"""

import nmap
from nmap.nmap import PortScannerError

# Start the scanner
scanner = nmap.PortScanner()

print("\nWelcome, this is a simple nmap scanner tool\n")

# Prompt the user to enter the IP address to scan.
ip_address = input("Enter IP address: ")
print(f"The IP address to scan is {ip_address}")

# Request the scan type
scan_type = input(
    """\nPlease enter the type of scan that you want to perform.\n
1) SYN ACK Scan
2) UDP Scan
3) Comprehensive scan
\nScan type: 
""")

if scan_type == "1":
    print(f"Nmap version: {scanner.nmap_version()}")

    try:
        scanner.scan(ip_address, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print(f"IP status: {scanner[ip_address].state()}")
        print(scanner[ip_address].all_protocols())
        print(f"Open ports: {scanner[ip_address]['tcp'].keys()}")

    except PortScannerError as e:
        print(f"Error: {e}")

    except KeyError:
        print(f"No ports open")

elif scan_type == "2":
    print(f"Nmap version: {scanner.nmap_version()}")

    try:
        scanner.scan(ip_address, '1-1024', '-v -sU')
        print(f"IP status: {scanner[ip_address].state()}")
        print(scanner[ip_address].all_protocols())
        print(f"Open ports: {scanner[ip_address]['udp'].keys()}")

    except PortScannerError as e:
        print(f"Error: {e}")

    except KeyError:
        print(f"No ports open")

elif scan_type == "3":
    
    try:
        print(f"Nmap version: {scanner.nmap_version()}")
        scanner.scan(ip_address, '1-1024', '-v -sS -A -sVC')
        print(f"IP status: {scanner[ip_address].state()}")
        print(scanner[ip_address].all_protocols())
        print(f"Open ports: {scanner[ip_address]['udp'].keys()}")

    except PortScannerError as e:
        print(f"Error: {e}")

    except KeyError:
        print(f"No ports open")

else:
    exit("[-] Scan type not valid! ")
