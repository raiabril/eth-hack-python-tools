#!/usr/bin/env python
"""
change-mac.py

This script will allow to change the MAC Address of the machine.
- We have the original permanent hardware address.
- We can set the new address.

We will use the library subprocess that allows us to execute shell commands.

"""
import subprocess

from termcolor import colored


def change_mac_address(interface, mac):
    """ This function will set the mac address for the interface provided."""

    # Set the interface down
    subprocess.call(f"ifconfig {interface} down", shell=True)

    # Set the MAC address
    subprocess.call(f"ifconfig {interface} hw ether {mac}", shell=True)

    # Set the interface up
    subprocess.call(f"ifconfig {interface} up", shell=True)


def main():
    """ Main function to request the interface to the user and set the value for the mac address. """

    # Request the interface and address to the user
    interface = input("[*] Enter the interface to update: ")
    new_mac_address = input("[*] Enter Mac Address to change to: ")

    # Check the address, modify and check again
    before_change_mac_address = subprocess.check_output("ifconfig " + interface,
                                                        stderr=subprocess.STDOUT, shell=True)
    change_mac_address(interface, new_mac_address)
    after_change_mac_address = subprocess.check_output("ifconfig " + interface,
                                                    stderr=subprocess.STDOUT, shell=True)

    if before_change_mac_address == after_change_mac_address:
        print(
            colored(f"[!!] Failed to change the MAC address of {interface}", 'red'))
    else:
        print(
            colored(f"[+] Successfully changed MAC address of {interface}", 'green'))


if __name__ == '__main__':
    main()
