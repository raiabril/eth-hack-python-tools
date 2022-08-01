#!/usr/bin/env python3
"""
ngrok_utils.py - Utils to manage ngrok tunnel

"""

import sys
import requests
import subprocess
import json


def start_ngrok_session(protocol="http", port="8080"):
    """ Start a ngrok session """

    try:
        subprocess.Popen(
            ["ngrok", protocol, port], stdout=subprocess.PIPE)

    except Exception as e:
        print(e)
        sys.exit()


def get_tunnel_url():
    """ Get the tunnel URL from ngrok """
    try:
        tunnel_url = requests.get("http://localhost:4040/api/tunnels").text
        tunnel_url = json.loads(tunnel_url)["tunnels"][0]["public_url"]
        return tunnel_url
    except requests.exceptions.ConnectionError:
        return None


def check_tunnel_active():
    """ Check if the tunnel is active """
    try:
        tunnel_url = requests.get("http://localhost:4040/api/tunnels").status_code
        return True if tunnel_url == 200 else False
    except requests.exceptions.ConnectionError:
        return False

def close_ngrok_session():
    """ Close the ngrok session """
    try:
        subprocess.Popen(
            ["pkill", "ngrok"], stdout=subprocess.PIPE)
    except Exception as e:
        print(e)
        sys.exit()