#!/usr/bin/env python3

"""
discover-subdomains.py - This script allows to discover subdomains of a given domain.

Usage: python3 discover-subdomains.py <domain>

"""

import sys
from sqlite3 import connect

import requests

target_url = sys.argv[1]

with open('wordlists/subdomains-1000.txt', 'r') as f:
    subdomain_list = f.read().splitlines()

for subdomain in subdomain_list:
    # Generate the URL to test
    url = 'http://' + subdomain + '.' + target_url

    # Check if the URL is valid with the subdomain
    try:
        response = requests.get(url)

    except requests.ConnectionError:
        continue

    # If the URL is valid, print it
    if response.status_code == 200:
        print(url)
