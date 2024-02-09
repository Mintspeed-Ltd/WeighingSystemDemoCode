# -*- coding: utf-8 -*-
# @Author: Ian Marks
# @Date:   07/04/22 15:00:18
# @Last Modified by:   Ian Marks
# @Last Modified time: 09/02/24 12:58:07

# Example Python code to retrieve weight.xml from the HTTP server
# on the Scrapman computer fitted to your trailer or Playstation.
# using the requests module.

# Code tested with Python 3.10.0 and Weighing System software V3.59.1

import requests

# Change root_address to the IP address of your trailer or Playstation.
# root_address = "http://123.1.224.213"  # default Playstation address.
root_address = "http://192.168.1.150"

# Scrapman weighing system only reponds on port 5050.
root_port = "5050"

# Set page_name to be either weight.xml or weight.json
page_name = "weight.json"


# Format thr request for print()
def format_request(req):

    return "\n{}\r\n{}\r\n\r\n{}".format(
        req.method + " " + req.url,
        "\r\n".join("{}: {}".format(k, v) for k, v in req.headers.items()),
        req.body,
    )


try:
    # Send the request to the server
    r = requests.get(f"{root_address}:{root_port}/{page_name}")
except Exception as e:
    print(e)
else:
    # Request returned a response, if the status was OK print the request sent
    # and the servers response
    if r.status_code == 200:
        raw_request = r.request
        print(f"====\nRequest: {format_request(raw_request)}\n====\nResponse:")
        print(r.text)
    else:
        print(f"Page returned an error: {r.status_code}")
