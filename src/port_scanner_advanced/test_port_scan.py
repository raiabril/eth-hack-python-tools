#!/usr/bin/env python3
"""
Port scan - test

Simple script ot test port scan in localhost and port 80.

"""
import socket

print("Socket library loaded..")

# Connect with TCP so STREAM and AF_INET is for IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = "10.0.2.15"
port = 80


def port_scanner(port):
    """ Function to scan the port using connect_ex() function of socket. """

    # Check with connect_ex function
    if sock.connect_ex((host, port)):
        print(f"Port {port} is closed")
    else:
        print(f"Port {port} is open")


# Execute the function
port_scanner(port)
