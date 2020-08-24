#!/usr/bin/python3
"""This displays X-Request-Id in a response header"""
import requests
import sys

if __name__ == "__main__":
    # Get the letter if any
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    # put letter in a dict
    contents = {"q": letter}
    # post req
    r = requests.post('http://0.0.0.0:5000/search_user', data=contents)
    # try and except incase it isn't jason
    try:
        result = r.json()
        if result == {}:
            print("No result")
        else:
            id_num = result.get("id")
            name = result.get("name")
            print("[{}] {}".format(id_num, name))
    except ValueError:
        print("Not a valid JSON")
