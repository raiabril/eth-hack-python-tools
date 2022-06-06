#!/usr/bin/env python3

"""
new_mac.py: Generate a new random MAC address.

Usage: sudo python3 new_mac.py <interface>

"""

from operator import ge
import random
import os
import subprocess
import sys

# Generate a random MAC address.


def generate_mac():
    """ 
        Generate a random MAC address from Xensource, Inc.
        More info: https://macvendors.com/
    """
    mac = [0x00, 0x16, 0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

# Assign the MAC address to the interface.


def set_mac(interface, mac):
    """ Set the MAC address of the interface. """
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])


new_mac = generate_mac()
set_mac(sys.argv[1], new_mac)
print(new_mac)
