#!/usr/bin/env python3
"""
url_shortener_tinyurl.py - Create a short version of a URL using tinyurl.

Author: @raiabril
"""

import pyshorteners
import sys

if len(sys.argv) != 2:
	print("[!!] Please provide a URL to shorten.")
	sys.exit()
	

try:
	long_url = sys.argv[1]
	shortener = pyshorteners.Shortener()
	short_url = shortener.tinyurl.short(long_url)
	
	print(f"[+] TinyURL: {short_url}")

except KeyboardInterrupt:
	print("[!!] Exiting ...")
	sys.exit()