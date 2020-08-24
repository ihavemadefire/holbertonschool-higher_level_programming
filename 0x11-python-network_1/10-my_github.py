#!/usr/bin/python3
"""Returns a gitup user id"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    name = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    octopus = requests.get("https://api.github.com/user", auth=name)
    octopus = octopus.json()
    idnum = octopus.get("id")
    print(idnum)
