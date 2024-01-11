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

    def to_json(self):
        """
        retrieves a dictionary representation of a
        Student instance
        """
        return vars(self)
