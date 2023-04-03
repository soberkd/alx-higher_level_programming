#!/usr/bin/python3
"""
This Python script fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    response = response.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
