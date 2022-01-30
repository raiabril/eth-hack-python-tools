#!/usr/bin/python3

import gzip
import hashlib

from termcolor import colored


def try_open(wordlist):
    """ 
    Function to open the file. Returns the list of words. 
    Will ignore not UTF-8 characters. 
    """
    try:
        # Sometimes the wordlist are using gz file.
        if wordlist[-3:] == '.gz':
            with gzip.open(wordlist, 'rb', errors='ignore') as pass_file:
                lines = pass_file.readlines()

        else:
            with open(wordlist, 'r', errors='ignore') as pass_file:
                lines = pass_file.readlines()

        lines = [line.strip('\n') for line in lines]
        return lines
    except Exception:
        exit("[!!] File not found")


def hash_compare(pass_hash, lines):
    """ Function to compare the hash with a list of words. """

    for line in lines:
        # Calculate the hash using hashlib
        enc_word = line.encode('utf-8')
        md5_digest = hashlib.md5(enc_word.strip()).hexdigest()

        # Compare the hash
        if md5_digest == pass_hash:
            return True, line

    return False, ""


def main():
    """ Main function. """

    # Request the user the info
    pass_hash = input("[*] Enter MD5 Hash value: ")
    wordlist = input("[*] Enter Path to the password file: ")

    # Obtain the list of words.
    lines = try_open(wordlist)

    # Check if the password is found in the list of words
    result, word = hash_compare(pass_hash, lines)

    if result:
        print(colored(f"[+] Password found: {word}", "green"))
    else:
        print(colored("[-] Password not in list", "red"))


if __name__ == "__main__":
    main()
