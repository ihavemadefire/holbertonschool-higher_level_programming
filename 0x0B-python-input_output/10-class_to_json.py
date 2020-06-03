#!/usr/bin/python3
"""This module defines a function that converts a json objet to class"""


def class_to_json(obj):
    """function that converts a json objet to class"""
    return obj.__dict__
