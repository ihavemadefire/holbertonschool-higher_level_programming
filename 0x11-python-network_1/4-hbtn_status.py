#!/usr/bin/python3
"""Let's play with the requests module"""

import requests

if __name__ == "__main__":
    http = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("    - type: {}".format(type(http.text)))
    print("    - content: {}".format(http.text))
