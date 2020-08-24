#!/usr/bin/python3
"""Let's play with the requests module"""
import requests
import sys


if __name__ == "__main__":
    site = sys.argv[1]
    http = requests.get(site)
    headers = http.headers
    xwing = headers.get('X-Request-Id')
    print(xwing)
