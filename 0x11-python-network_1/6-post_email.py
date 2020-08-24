#!/usr/bin/python3
"""This displays X-Request-Id in a response header"""
import requests
import sys


if __name__ == "__main__":
    site = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(site, data={'email': email})
    print(r.text)
