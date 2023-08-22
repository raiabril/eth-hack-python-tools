#!/usr/bin/env python3
"""
TCP Client


"""

import socket

# Create the client object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 4444

# Start the connection
client_socket.connect((host, port))

# Read the message
message = client_socket.recv(1024)
print(f"Message received: {message}")

# Close the socket
client_socket.close()