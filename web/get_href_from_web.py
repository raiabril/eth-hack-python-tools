#!/usr/bin/env python3
"""
get_href_from_web.py - Retrieve the href from a website using BeautifulSoup.
"""

import sys

import requests
from bs4 import BeautifulSoup
from termcolor import colored


def main():
    target = input("Enter the target URL: ")

    try:
        response = requests.get(target)

    except requests.exceptions.ConnectionError:
        print(colored("Error: Unable to connect to the target URL", "red"))
        sys.exit(1)

    if 'error' not in response.text:

        soup = BeautifulSoup(response.text, 'html.parser')

        links = get_links_from_soup(soup)

        for link in links:
            print(colored(f"[+] {link}"), "green")

def get_links_from_soup(soup):
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

if __name__ == '__main__':
    main()
    sys.exit(0)
