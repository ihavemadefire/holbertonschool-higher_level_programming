#!/usr/bin/python3
"""This displays X-Request-Id in a response header"""
import urllib.request
import sys


if __name__ == "__main__":
    site = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email})
    data = data.encode("ascii")
    with urllib.request.urlopen(site, data) as response:
        html = response.read()
        html = html.decode("UTF-8")
        print(html)
