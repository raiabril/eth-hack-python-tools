#!/usr/bin/python3
"""

ngrok_start.py - Start a ngrok session and forward the URL to my email account.

"""

import sys
from time import sleep

import ngrok_utils as ngrok_utils
import gmail_client as gmail_client


def main():

    if ngrok_utils.check_tunnel_active():
        print("[+] Tunnel is already active")
        sys.exit()
    else:
        try:

            email = sys.argv[1]
            password = sys.argv[2]

        except IndexError:
            print("[-] Please provide your email and password")
            sys.exit()

        print("[+] Starting tunnel...")
        ngrok_utils.start_ngrok_session()
        sleep(5)
    

    tunnel_url = ngrok_utils.get_tunnel_url()

    # Print the Tunnel URL
    print(f"[+] Tunnel: {tunnel_url}")

    # Send the tunnel url to my email account
    message = f"Subject: ngrok tunnel\n\n{tunnel_url}"
    gmail_client.send_email(email, password, message)


if '__main__' == __name__:
    main()
