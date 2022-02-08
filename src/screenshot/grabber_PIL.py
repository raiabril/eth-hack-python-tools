#!/usr/bin/env python3

"""
Grabber

Used to take screenshots and send to our server using ftp.

It uses PIL

"""

from PIL import ImageGrab
import os
import ftplib

# Credentials
IP = '127.0.0.1'
USER = 'ftp'
PASSWORD = '12345'

# Initialize the wx, screen and size
ss_region = (0,0,600, 600)
ss_img = ImageGrab.grab(ss_region, xdisplay="0")
ss_img.save("screen.png")

# Send to FTP

ftp_session = ftplib.FTP(IP, USER, PASSWORD)

with open('grabbed.png', 'rb') as f:
    ftp_session.storbinary("STOR screen.png", f)

ftp_session.close()