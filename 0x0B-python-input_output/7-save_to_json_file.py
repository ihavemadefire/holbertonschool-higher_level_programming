#!/usr/bin/python3
"""This module stared into the abyss too long"""
import json


def save_to_json_file(my_obj, filename):
    """This function saves a JSON object to a file"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
