#!/usr/bin/python3
"""This module contains no function"""
import sys
import json
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

file = "add_item.json"

try:
    object = load_from_json_file(file)
    for i in range(1, len(sys.argv)):
        object.append(sys.argv[i])
except:
    object = []
save_to_json_file(object, file)
