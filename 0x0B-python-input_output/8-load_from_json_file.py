#!/usr/bin/python3
"""This module is a module"""
import json


def load_from_json_file(filename):
    """this function loads from a json file"""
    with open(filename, 'r', encoding="utf-8") as file:
        parsed_json = (json.load(file))
    return parsed_json
