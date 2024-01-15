#!/usr/bin/python3
"""
This is a part of alx python tasks.
This module contains a class called Base
"""
import json
import os


class Base:
    """
    This class will be the “base” of all other classes in
    this project. The goal of it is to manage id attribute
    in all your future classes and to avoid duplicating the
    same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of Base class objects"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        a function that returns the JSON representation
        of list_dictionaries
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return '[]'
        return json.dumps(list_dictionaries, default=str)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        a function that writes an Object to a text file,
        using a JSON representation
        """
        ls_dic = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                ls_dic.append(list_objs[i].to_dictionary())
        json_objs = cls.to_json_string(ls_dic)
        with open(cls.__name__ + '.json', 'w') as f:
            return f.write(json_objs)

    @staticmethod
    def from_json_string(json_string):
        """
        a function that returns an object (Python data structure)
        represented by a JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls is Base:
            if 'id' in dictionary.keys():
                id = dictionary['id']
                return Base(id)
            return Base()
        obj = cls.dummy()
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """A method that returns a list of instances using json files"""
        filename = (cls.__name__ + '.json')
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            json_objs = f.read()
            objs_dic = Base.from_json_string(json_objs)
            objs = []
            for i in range(len(objs_dic)):
                objs.append(cls.create(**objs_dic[i]))
            return objs
