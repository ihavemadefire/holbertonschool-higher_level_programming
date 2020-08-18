#!/bin/bash
# curl POST a json object
curl -s -X POST -H "Content-Type: application/json" -d "@"$2"" "$1"
