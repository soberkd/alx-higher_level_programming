#!/usr/bin/python3
"""
This python script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    account = argv[1]
    token = argv[2]
    url = "https://api.github.com/user"
    respnd = requests.get(url, auth=HTTPBasicAuth(account, token))
    json = respnd.json()
    print(json.get('id'))
