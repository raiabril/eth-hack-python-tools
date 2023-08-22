#!/usr/bin/env python3
"""
mac_sniffer.py: This script allows to sniff MAC addresses communicating in the network.

"""

import socket
from struct import unpack

def parse_mac(mac_address):
    """
    Parse a MAC address from the representation in bytes to the representation in hexadecimal.
    """
    return ':'.join(map('{:02x}'.format, mac_address))

try:
    # Create a raw socket and bind it to the interface to listen for IP packets
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

except socket.error as msg:
    print('Socket could not be created. Error Code : ' +
        str(msg[0]) + ' Message ' + msg[1])
    exit()

try:
    
    while True:
        # Receive a packet and obtain the mac addresses from ethernet header
        packet = s.recvfrom(65565)

        # Obtain the ethernet header
        # Ethernet header is 14 bytes
        eth_header = packet[0][0:14]
        
        # Obtain the mac addresses
        # MAC addresses are 6 bytes
        eth = unpack('!6s6sH', eth_header)

        # Protocol is in the last 2 bytes of the ethernet header
        eth_protocol = socket.ntohs(eth[2])

        print(f"[+] Source: {parse_mac(eth[1])} Destination: {parse_mac(eth[0])} Protocol: {eth_protocol}")


except KeyboardInterrupt:
    print('\nExiting...')
    exit()
