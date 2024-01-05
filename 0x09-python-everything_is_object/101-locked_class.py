#!/usr/bin/python3
""" 101- LockedClass task """


class LockedClass:
    """ LockedClass implementation """
    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        """ initialize first name """
        self.first_name = first_name
