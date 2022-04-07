
## Retrieve weight.json from the Scrapman weighing system using simple sockets.

# Example Python code to retrieve weight.json from the HTTP server
# on the Scrapman computer fitted to your trailer or Playstation.
# using sockets.

# Code tested with Python 3.10.0 and Weighing System software V3.59.1

import socket

target_host = "192.168.0.51" # Change this to the IP address of your trailer or Playstation.
target_page = "weight.json"  # weight.xml will also work.
target_query = ""            # ?tare will tare the current weight, ?untare will clear an existing tare.
                             # leave an empty string to continue in current tare state.
target_port = 5050           # Scrapman weighing system only reponds on port 5050.

# Initialise and connect the socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))

# Build the actual HTTP request. Note the extra blank line on the end (\r\n).
request = f"GET {target_page}{target_query} HTTP/1.1\r\nHost:{target_host}\r\n\r\n"

# Send the request to the server.
client.send(request.encode())

# Receive the server response.
response = client.recv(4096)

# convert the responce into a python string and format it so that it prints sensibly.
http_response = str(response)
http_response = http_response[2:-1]
http_response = http_response.replace('\\n','\n')
http_response = http_response.replace('\\r','\r')

# Show the server response
print(http_response)


