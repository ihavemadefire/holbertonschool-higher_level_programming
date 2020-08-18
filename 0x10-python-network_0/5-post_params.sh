#!/bin/bash
# Sends a POST curl req and prints the response
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
