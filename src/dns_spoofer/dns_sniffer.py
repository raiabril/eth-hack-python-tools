#!/usr/bin/env python3
"""
dns_sniffer.py - Sniff packet to find DNS requests and responses.

Author: @raiabril
"""

from scapy import all as scapy

def dns_sniffer(packet):
    """ Retrieve the DNS query if the packet has it. """

    if packet.haslayer(scapy.DNS):
        print("[+] DNS Query: " + packet[scapy.IP].src + " --> " + packet[scapy.IP].dst + " " + packet[scapy.DNS].summary())

if "__main__" == __name__:
    scapy.sniff(filter="udp and port 53", prn=dns_sniffer)



