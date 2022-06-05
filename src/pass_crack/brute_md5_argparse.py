#!/usr/bin/env python3

"""
brute_md5_argparse.py

Function to brute force a MD5 hash.

Usage: python3 brute_md5_argparse.py <hash> <wordlist>

"""

import hashlib
import argparse
from termcolor import colored
import gzip


parser = argparse.ArgumentParser(description="Brute force a MD5 hash.")
parser.add_argument("-md5", dest="hash",
                    help="MD5 hash to brute force.", required=True)
parser.add_argument("-w", dest="wordlist",
                    help="Path to the wordlist.", required=True)


def try_open(wordlist):
    """ Try to open the wordlist. """
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


def hash_compare(hash_to_check, lines):
    """ Compare the hash with the list of words. """
    for word in lines:
        if hashlib.md5(word.encode()).hexdigest() == hash_to_check:
            return True, word
    return False, None


def main():
    """ Main function. """

    # Request the user the info
    args = parser.parse_args()
    hash_to_check = args.hash
    wordlist = args.wordlist

    # Obtain the list of words.
    lines = try_open(wordlist)

    # Check if the password is found in the list of words
    result, word = hash_compare(hash_to_check, lines)

    if result:
        print(colored(f"[+] Password found: {word}", "green"))
    else:
        print(colored(f"[!!] Password not found", "red"))


if '__main__' == __name__:
    main()
