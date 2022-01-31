#!/usr/bin/python3

import gzip
import hashlib

from termcolor import colored


def try_open(wordlist):
    try:
        if wordlist[-3:] == '.gz':
            pass_file = gzip.open(wordlist, 'rb')
        else:
            pass_file = open(wordlist, 'r')
        lines = pass_file.readlines()
        lines = [line.decode("utf-8", errors='ignore').strip('\n')
                 for line in lines]
        pass_file.close()
        return lines

    except Exception as e:
        print(e)


value = input("[*] Enter the Sha1 value to crack: ").lower()
wordlist = input("[*] Enter Path to the password file: ")
lines = try_open(wordlist)

for password in lines:
    hash_guess = hashlib.sha1()
    hash_guess.update(password.encode())

    if hash_guess.hexdigest() == value:
        print(colored(f"[+] Password found: {password}", "green"))
        exit()

print(colored("[-] Password not found", "red"))
