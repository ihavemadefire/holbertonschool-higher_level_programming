#!/usr/bin/python3
"""This displays X-Request-Id in a response header"""
import requests
import sys


if __name__ == "__main__":
    site = sys.argv[1]
    r = requests.get(site)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
