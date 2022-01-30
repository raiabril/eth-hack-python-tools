
#!/usr/bin/env python3
"""
Banner retriever

This script will allow to retrieve the banner of the IP and port specified.

"""

import socket


def ret_banner(ip, port):
    """ Function to retrieve the banner for IP and Port"""
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner

    except ConnectionRefusedError as e:
        exit(f"Error retrieving banner: {e}")


def main():
    # Specify the IP and port
    ip_address = input("Please specify the IPv4: ")

    for port in range(1, 1000):
        banner = ret_banner(ip_address, port).strip("\n")
        if banner:
            print(f'[+] {ip_address}:{port} - {banner}')


main()
