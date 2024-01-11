#!/usr/bin/python3
"""
This is a part of alx python tasks.
This module contains class Student
"""


class Student:
    """
    Student class definition.
    It has public instance attribuites: (first_name,
    last_name, age)
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor for the student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a
        Student instance, (If attrs is a list of strings,
        only attribute names contained in this list must be
        retrieved.Otherwise, all attributes must be retrieved
        """
        if not isinstance(attrs, list):
            return vars(self)
        if not all(isinstance(v, str) for v in attrs):
            return vars(self)
        my_obj = {}
        objects = vars(self)
        for key, value in objects.items():
            if key in attrs:
                my_obj[key] = value
        return my_obj

    def reload_from_json(self, json):
        """
        a method that replaces all attributes of the
        Student instance:
        1-You can assume json will always be a dictionary
        2-A dictionary key will be the public attribute name
        3-A dictionary value will be the value of the public attribute
        """
        for key, value in json.items():
            setattr(self, key, value)
