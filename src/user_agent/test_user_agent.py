#!/usr/bin/env python3
"""
Test User agent

This script allows to test the User Agent library and theck if the User agent is valid and if it is a bot.

"""

from user_agents import parse

# Prompt the user to request the agent string
ua_string = input("Enter the User-Agent string: ")

# Check is not an empty array. Exit if not valid.
if ua_string != '':

    # Try to parse the user agent for a valid user agent string.
    try:
        user_agent = parse(ua_string)
        print(f"[+] The user agent is: {user_agent}")
        print(f"[+] The user is bot: {user_agent.is_bot}")

    except Exception as e:
        print(f"[-] Error parsing the User-Agent: {e}")

else:
    exit("[-] Please enter a valid string.")
