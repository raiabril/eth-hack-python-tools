#!/usr/bin/env python3

from scapy.all import *

def floodz(source, target):
	""" Function to create multiple TCP requests. """
	for source_p in range(100,150):
		IP_layer = IP(src=source, dst=target)
		TCP_layer = TCP(sport=source_p, dport=600)
		pkt = IP_layer/TCP_layer # Create the packet
		send(pkt)

source = "127.0.0.1"
target = "127.0.0.1"

floodz(source, target)