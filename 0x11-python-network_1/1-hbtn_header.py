#!/usr/bin/python3
"""This displays X-Request-Id in a response header"""
import urllib.request
import sys


if __name__ == "__main__":
    site = sys.argv[1]
    with urllib.request.urlopen(site) as response:
        html = (response.headers)
        val = dict(html)
        xwing = val.get("X-Request-Id")
        print(xwing)
