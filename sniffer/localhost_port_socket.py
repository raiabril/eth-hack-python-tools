#!/usr/bin/env python3

"""
localhost_port_socket.py - Sniff TCP traffic

This script captures TCP traffic on the localhost and port specified and prints the data message to a JSON file. It 
uses the socket library to capture the traffic.
"""

import socket
import json
import sys

def sniff_tcp(interface, port):
	# Create a socket object.
	sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

	# Bind the socket to the interface and port.
	sock.bind((interface, port))

	# Receive data from the socket.
	while True:
		data = sock.recvfrom(65535)

		# Print the data to the screen.
		print(data[0].decode())

		# Write the data to a JSON file.
		with open("tcp.json", "a") as f:
			json.dump(data[0].decode(), f)
	
def main():
	if len(sys.argv) != 3:
		print("Usage: ./localhost_port_socket.py <interface> <port>")
		sys.exit(1)
	else:
		sniff_tcp(sys.argv[1], int(sys.argv[2]))

main()