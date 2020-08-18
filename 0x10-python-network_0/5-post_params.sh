#!/bin/bash
# Sends a POST curl req and prints the response
ES="email=hr@holbertonschool.com&subject=I will always be here for PLD"
curl -s -d "$ES" -X "POST" "$1"
