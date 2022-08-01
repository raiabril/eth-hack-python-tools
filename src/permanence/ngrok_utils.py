#!/usr/bin/env python3
"""
ngrok_utils.py - Utils to manage ngrok tunnel

"""

import requests
import subprocess
import json


def start_ngrok_session():
    """ Start a ngrok session """

    try:
        subprocess.Popen(
            ["ngrok", "http", "8080"], stdout=subprocess.PIPE)

    except Exception as e:
        print(e)
        sys.exit()


def get_tunnel_url():
    """ Get the tunnel URL from ngrok """
    tunnel_url = requests.get("http://localhost:4040/api/tunnels").text
    tunnel_url = json.loads(tunnel_url)["tunnels"][0]["public_url"]
    return tunnel_url


def check_tunnel_active():
    """ Check if the tunnel is active """
    tunnel_url = requests.get("http://localhost:4040/api/tunnels").status_code
    return True if tunnel_url == 200 else False
