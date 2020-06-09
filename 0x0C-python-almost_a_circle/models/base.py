#!/usr/bin/python3
"""This module contains a class called Base"""
import json


class Base():
    """"This is the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is an initialization method"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts to JSON string"""
        if list_dictionaries is None:
            return json.dumps([])
        jsonobj = json.dumps(list_dictionaries)
        return jsonobj

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves json to file"""
        filename = "{}.json".format(cls.__name__)
        tosave = []
        with open(filename, 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_strint(tosave))
            else:
                for i in list_objs:
                    tosave.append(cls.to_dictionary(i))
                tosave = cls.to_json_string(tosave)
                file.write(tosave)

    @staticmethod
    def from_json_string(json_string):
        """Converts json to dictionary"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """From dict to instance"""
        if cls.__name__ == 'Rectangle':
            obj1 = Rectangle(width=1, height=1)
        else:
            obj1 = Square(size=1)
        obj1.update(dictionary)
        return obj1
