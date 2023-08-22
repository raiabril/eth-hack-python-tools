#!/usr/bin/env python3

"""
banner_grabber.py - A simple banner grabber

Author: @raiabril
"""

import socket

from termcolor import colored


def retrieve_banner(ip, port):
    """ 
    Function to retrieve the banner for IP and Port
    :param ip -> IP from where to read the banners.
    :param port -> Port to retrieve the banner
    :return banner -> first 1024 bits received in the socket
    :except
        ConnectionRefusedError
    """
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner

    except ConnectionRefusedError as e:
        exit(f"Error retrieving banner: {e}")

    except socket.timeout:
        exit(f"Host might be down. Timed out")


def main():
    # Ask the user to specify the IP
    ip_address = input("Please specify the IPv4: ")
    port = input("Please specify the port: ")

    # Run the banner grabber
    banner = retrieve_banner(ip_address, port).strip("\n")

    if banner:
        print(
            colored(f'[+] Found {ip_address}:{port} - {banner}'), "green")


if __name__ == '__main__':
    main()