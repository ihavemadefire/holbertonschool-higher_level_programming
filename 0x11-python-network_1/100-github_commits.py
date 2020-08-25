#!/usr/bin/python3
"""This prints the last 10 repo commits"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    commits = requests.get("https://api.github.com/repos/{}/{}/commits".format(owner, repo))
    ac = commits.json()
    for i in range(10):
        print("{}: {}".format(
            ac[i].get("sha"),
            ac[i].get("commit").get("author").get("name"))
          )
