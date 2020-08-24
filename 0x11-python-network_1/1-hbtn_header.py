#!/usr/bin/python3
"""This displays X-Request-Id in a response header"""
import urllib.request
import sys


site = sys.argv[1]
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = (response.headers)
        val = dict(html)
        xwing = val.get("X-Request-Id")
        print(xwing)
