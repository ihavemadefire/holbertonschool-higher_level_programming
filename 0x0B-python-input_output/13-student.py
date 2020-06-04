#!/usr/bin/python3
"""This module contains a class called Student"""


class Student():
    """this class is called student"""
    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict"""
        ret = {}
        if attrs is not None:
            for i in attrs:
                if i in self.__dict__:
                    ret.update({i: self.__dict__.get(i)})
            return ret
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """This is a docstring"""
        if json.get("first_name") is not None:
            self.first_name = json.get("first_name")
        if json.get("last_name") is not None:
            self.last_name = json.get("last_name")
        if json.get("age") is not None:
            self.age = json.get("age")
