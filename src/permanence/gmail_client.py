#!/usr/bin/env python3
"""
gmail_client.py - Send an email using Gmail account.

Author: @raiabril
"""

import smtplib

def send_email(email, password, message):
    """ Send an email with the URL of the tunnel"""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    print(f"[+] Email sent to {email}")
    server.quit()