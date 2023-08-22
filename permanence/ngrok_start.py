#!/usr/bin/python3
"""

ngrok_start.py - Start a ngrok session and forward the URL to my email account.

"""

import sys
from time import sleep
from datetime import datetime

import gmail_client as gmail_client
import ngrok_utils as ngrok_utils


def main():

    if ngrok_utils.check_tunnel_active():
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - [+] Tunnel is already active")
        sys.exit()
    else:
        try:

            email = sys.argv[1]
            password = sys.argv[2]

        except IndexError:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - [-] Please provide your email and password")
            sys.exit()

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - [+] Starting tunnel...")
        ngrok_utils.start_ngrok_session("tcp","22")
        sleep(5)
    

    tunnel_url = ngrok_utils.get_tunnel_url()

    # Print the Tunnel URL
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - [+] Tunnel: {tunnel_url}")

    # Send the tunnel url to my email account
    message = f"Subject: ngrok tunnel\n\n{tunnel_url}"
    email_sent = gmail_client.send_email(email, password, message)

    if email_sent:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - [+] Email sent to {email}")


if '__main__' == __name__:
    main()
