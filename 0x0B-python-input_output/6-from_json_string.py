#!/usr/bin/python3
"""This module contains many characters, some more savory than others"""
import json


def from_json_string(my_str):
    """This file converts the string to a python obj"""
    return json.loads(my_str)
