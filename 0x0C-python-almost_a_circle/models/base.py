#!/usr/bin/python3
import json
import os

class Base:
    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def create(cls, **dictionary):
        dummy_instance = None  # Initialize dummy_instance with None
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        class_name = cls.__name__
        file_name = class_name + ".json"

        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                json_data = f.read()
            return [cls.create(**obj) for obj in cls.from_json_string(json_data)]

        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
