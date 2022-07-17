#!/usr/bin/python3
"""

ngrok_start.py - Start a ngrok session and forward the URL to my email account.

"""

import json
import subprocess
import sys
from time import sleep

import requests
import smtplib


def main():
    try:

        email = sys.argv[1]
        password = sys.argv[2]

    except IndexError:
        print("[-] Please provide your email and password")
        sys.exit()

    # Start the ngrok instance
    try:
        ngrok = subprocess.Popen(
            ["ngrok", "http", "8080"], stdout=subprocess.PIPE)

    except Exception as e:
        print(e)
        sys.exit(1)

    # Wait for the server to start
    sleep(3)

    # Request the tunnel url
    localhost_url = "http://localhost:4040/api/tunnels"  # Url with tunnel details
    # Get the tunnel information
    tunnel_status = requests.get(localhost_url).text
    tunnel_json = json.loads(tunnel_status)
    tunnel_url = tunnel_json['tunnels'][0]['public_url']

    # Print the Tunnel URL
    print(f"[+] Tunnel: {tunnel_url}")

    # Send the tunnel url to my email account
    message = f"Subject: ngrok tunnel\n\n{tunnel_url}"
    send_email(email, password, message)


def send_email(email, password, message):
    """ Send an email with the URL of the tunnel"""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    print(f"[+] Email sent to {email}")
    server.quit()


if '__main__' == __name__:
    main()
