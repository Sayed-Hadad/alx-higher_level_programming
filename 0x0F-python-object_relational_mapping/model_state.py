#!/usr/bin/python3
"""
 a python file that contains the class definition of a State
 and an instance Base = declarative_base():
"""
from sqlalchemy import ForeignKey, Column
from sqlalchemy import String, CHAR, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class:

    - inherits from Base Tips

    - links to the MySQL table states

    - class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key

    - class attribute name that represents a column of a string with maximum
    128 characters and can’t be null
    """
    __tablename__ = "states"

    id = Column("id", Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)

    def __init__(self, name):
        """the constructor method"""
        self.name = name

    def __str__(self):
        """providing a way to display the results"""
        return f'{self.id}: {self.name}'
