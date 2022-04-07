# Example Python code to retrieve weight.xml from the HTTP server
# on the Scrapman computer fitted to your trailer or Playstation.
# using the requests module.

# Code tested with Python 3.10.0 and Weighing System software V3.59.1

import requests

root_address = 'http://192.168.0.51' # Change this to the IP address of your trailer or Playstation.
root_port = '5050'                   # Scrapman weighing system only reponds on port 5050. 
page_name = 'weight.xml'             # weight.json will also work.
page_args = ''                       # tare will tare the current weight, untare will clear an existing tare.
                                     # leave an empty string to continue in current tare state.

# Format thr request for print()
def format_request(req):
    
    return ('\n{}\r\n{}\r\n\r\n{}'.format(
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))


try:
    # Send the request to the server
    r = requests.get(f"{root_address}:{root_port}/{page_name}", params=page_args)
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

