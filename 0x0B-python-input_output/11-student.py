#!/usr/bin/python3
"""This module contains a class called Student"""


class Student():
    """this class is called student"""
    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict"""
        return self.__dict__
