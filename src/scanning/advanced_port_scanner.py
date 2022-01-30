#!/usr/bin/env python3
"""
Advanced scanner

Allows to check the ports that are open using socket.

Usage python3 advanced_scanner.py -H <host> -p <port>

"""

import optparse
import socket
import threading

from termcolor import colored


def port_scan(target_host, target_ports):
    """ Function to scan the ports using multithreading. """

    # Try to obtain the target IP from the host by name
    try:
        target_ip = socket.gethostbyname(target_host)
        
    except Exception as e:
        print(f"Cannot resolve the name of the host: {e}")

	# Try to obtain the Target name from the IP.
    try:
        target_name = socket.gethostbyaddr(target_ip)
        print("[*] Scan results for: {}".format(target_name[0]))

    except Exception as e:
        print(f"Cannot get the name for IP {target_ip}: {e}")

    socket.setdefaulttimeout(2)

    for target_port in target_ports:
        t = threading.Thread(
			target=conn_scan, 
			args=(target_host, int(target_port)))
        t.start()


def conn_scan(target_host, target_port):
    """ Function to test a particular port using socket. """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_host, target_port))
        print(colored("[+] {target_port}/tcp is open", 'green'))

    except Exception:
        print(colored(f"[-] {target_port}/tcp is closed", 'red'))

    finally:
        sock.close()


def main():
	# Define the parser for user interaction using command line arguments.
    parser = optparse.OptionParser(
        'Usage of program: ' + '-H <target host> -p <target ports>')
    parser.add_option('-H', dest='target_host', type='string',
                      help='Specify the target host')
    parser.add_option('-p', dest='target_ports', type='string',
                      help='Specify target ports separated by comma')

	# parse arguments when received
    (options, args) = parser.parse_args()
    target_host = options.target_host
    target_ports = str(options.target_ports).split(',')

	# If not provided print help
    if (target_host == None) | (target_ports[0] == None):
        print(parser.usage)
        exit(0)
	
	# Run the port scanner
    port_scan(target_host, target_ports)


if __name__ == '__main__':
    main()
