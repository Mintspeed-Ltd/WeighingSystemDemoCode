# -*- coding: utf-8 -*-
# @Author: Ian Marks
# @Date:   07/04/22 15:00:18
# @Last Modified by:   Ian Marks
# @Last Modified time: 09/02/24 14:57:23

# Example Python code to retrieve the weight and battery voltage
# from the HTTP server on the Scrapman computer fitted to your
# trailer or Playstation.


# Code tested with Python 3.10.0 and Weighing System software V3.62

import json
from time import sleep

import requests

# Change root_address to the IP address of your trailer or Playstation.
# root_address = "http://123.1.224.213"  # default Playstation address.
root_address = "http://192.168.1.150"

# Read the weight and batteey voltage every 5 second until stopped with ctrl-c
while True:

    try:
        # Send the request to the server
        r = requests.get(f"{root_address}:5050/weight.json")
    except Exception as e:
        print(e)
    else:
        # Request returned a response, if the status was OK extract the current
        # average weight and battery voltages and print them to the console

        if r.status_code == 200:
            # Convert json string to python dictionary
            json_data = json.loads(r.text)

            # Isolate the sections from the json (keeps the code tidier and saves typing)
            system_d = json_data["MintSpeed"]["TrailerWeighingSystem"]["System"]
            weight_d = json_data["MintSpeed"]["TrailerWeighingSystem"]["Weight"]["Total"]

            # Get the values from the section and convert the string values to tonne and voltage
            g_weight = float(weight_d["CurrentWeight"]) / 1000.0
            ave_weight = float(weight_d["AverageWeight"]) / 1000.0
            bat1 = float(system_d["BatteryVoltage1"])
            bat2 = float(system_d["BatteryVoltage2"])

            print(
                f"Weight: {g_weight:.2f}t, Average Weight: {ave_weight:.2f}t, Battery 1: {bat1:.2f}v, Battery 2: {bat2:.2f}v",
                end="\r",
            )

        else:
            print(f"Page returned an error: {r.status_code}")

    # repeat every 5 seconds
    sleep(5)
