#!/usr/bin/env python3
"""
find_hidden_directories.py - Find hidden directories in a web service.

Usage: python3 find_hidden_directories.py <domain>

"""

import sys

import requests

from models import Target


def get_request(url, directory):
    """
    Send a GET request to the target URL.
    """
    try:
        response = requests.get(url + directory)
        # Check that the response does not contain error
        print("[+] GET request sent to: " + url)
        if 'error' not in response.text and response.status_code != 404:
            print('[+] Directory found: ' + directory)
            return directory
    except ConnectionError:
        print('[-] Connection error')
        exit()
    except KeyboardInterrupt:
        print('[-] User Interrupt')
        exit()
    except Exception as e:
        print('[-] Error: ' + str(e))
        exit()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 find_hidden_directories.py <domain>")
		sys.exit(1)

	target = Target(sys.argv[1])
	# Send a request to the target URL with each line in the wordlist
	with open('wordlists/directory-list-2.3-medium.txt') as f:
		for line in f:
			directory = line.strip('\n')
			get_request(target.url, directory)


if '__main__' == __name__:
	main()
	sys.exit(0)