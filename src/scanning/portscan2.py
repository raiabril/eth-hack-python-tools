#! /usr/bin/env python3
"""
Test port scan with args

Test the host specified by the user when prompted in the command line.

"""

import socket

from termcolor import colored

# Create the socket object
# Connect with TCP so STREAM and AF_INET is for IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)


def port_scanner(port):

    if not sock.connect_ex((host, port)):
        print(colored("Port {} is open".format(port), 'green'))


# Prompt the user to request the host
host = input("[*] Enter the host to scan: ")

# Scan the host through the ports in range 1 through 10000
for port in range(1, 10000):
    port_scanner(port)
