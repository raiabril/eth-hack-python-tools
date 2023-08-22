#/usr/bin/env python3

"""
localhost_port.py - Sniff TCP traffic

This script captures TCP traffic on the localhost and port specified and prints the data message to a JSON file.
"""

import scapy.all as scapy
import json
import sys

def sniff_tcp(interface, port):
	scapy.sniff(iface=interface, filter="tcp port " + str(port), store=False, prn=process_packet)

def process_packet(packet):
	if packet.haslayer(scapy.TCP):
		# Obtain the raw in case we can extract usernames and passwords
		# from the packet.
		if packet.haslayer(scapy.Raw):
			load = packet[scapy.Raw].load

			# Print the load to the screen.
			print(load.decode())

			# Write the load to a JSON file.
			with open("tcp.json", "a") as f:
				json.dump(load.decode(), f)


def main():
	if len(sys.argv) != 3:
		print("Usage: ./localhost_port.py <interface> <port>")
		sys.exit(1)
	else:
		sniff_tcp(sys.argv[1], sys.argv[2])

main()