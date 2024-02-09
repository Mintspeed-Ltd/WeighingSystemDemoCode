# -*- coding: utf-8 -*-
# @Author: Ian Marks
# @Date:   07/04/22 15:00:18
# @Last Modified by:   Ian Marks
# @Last Modified time: 09/02/24 13:13:16

## Retrieve weight.json from the Scrapman weighing system using simple sockets.

# Example Python code to retrieve weight.json from the HTTP server
# on the Scrapman computer fitted to your trailer or Playstation.
# using sockets.

# Code tested with Python 3.10.0 and Weighing System software V3.59.1

import socket

# Change target_host to the IP address of your trailer or Playstation.
# target_host = "123.1.224.213" # Default Playstation address
target_host = "192.168.1.150"

# Set target_pageto be either weight.json or weight.xml
target_page = "weight.xml"

# Scrapman weighing system only reponds on port 5050.
target_port = 5050

# Initialise and connect the socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

# Build the actual HTTP request. Note the extra blank line on the end (\r\n).
request = f"GET {target_page} HTTP/1.1\r\nHost:{target_host}\r\n\r\n"

# Send the request to the server.
client.send(request.encode())

# Receive the server response.
response = client.recv(4096)

# convert the responce into a python string and format it so that it prints sensibly.
http_response = str(response)
http_response = http_response[2:-1]
http_response = http_response.replace("\\n", "\n")
http_response = http_response.replace("\\r", "\r")

# Show the server response
print(http_response)
