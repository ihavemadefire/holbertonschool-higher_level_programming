#!/usr/bin/python3
"""This displays either test or error code"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    site = sys.argv[1]
    try:
        with urllib.request.urlopen(site) as response:
            response = response.read()
            print(response.decode("UTF-8"))
    except Exception as e:
        print("Error code: {}".format(e.status))
