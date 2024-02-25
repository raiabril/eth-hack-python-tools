#!/usr/bin/env python
"""
TCP Server (tcpserver.py)

This is the script from freecodecamp.org course on Information security.

"""

import socket

# Create the TCP socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 4444

# Bind the localhost to socket
server_socket.bind((host, port))

# Starting the TCP server.
server_socket.listen(3)

# Run the socket
while True:
    # Recevied connection
    client_socket, address = server_socket.accept()
    print(f"[+] Received connection from {address}")

    # Send message
    message = "Hello, thank you for connecting to the server."
    client_socket.send(message.encode('utf8'))

    # Close connection
    client_socket.close()