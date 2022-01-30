#!/usr/bin/python3

"""
FTP Anonymous

This script allows to perform an anonymous login attack in an vulnerable FTP server.

Author: Rai

"""

import ftplib

from termcolor import colored


def anon_login(hostname):
	""" Function to perform an anonymous login ftp to the hostname provided."""
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'anonymous')
		print(colored(f"[+] Successful anonymous login @ {hostname}", 'green'))
	except Exception:
		print(colored(f"[-] Anonymous not permitted @ {hostname}", 'red'))

# Request the user for the IP to launch the anonymous login
hostname = input("Enter the IP Address: ")

# Launch anonymous login
anon_login(hostname)
