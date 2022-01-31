#!/usr/bin/python3

import socket
import os
import sys


def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner, filename):
	with open(filename, 'r') as myfile:
		lines = myfile.readlines()
	for line in lines:
		if banner == line:
			print("[+] Server is vulnerable {line}")



def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print('[-] File doesnt exist!')
			exit(0)
		if not os.access(filename, os.R_OK):
			print('[-] Access denied!')
			exit(0)
	else:
		print(f'[-] Usage: {sys.argv[0]} + <vuln filename>')
		exit(0)


	portlist = [21, 22, 25, 80, 110, 443, 445]

	for x in range(1, 255):
		ip = '10.0.2.' + str(x)
		for port in portlist:
			banner = retBanner(ip, port)
			if banner:
				print(f'[+] {ip} : {port} - {banner}')
				checkVulns(banner, filename)

if __name__ == "__main__":
	main()
