#!/usr/bin/python3
"""
 a python file that contains the class definition of a City
 and an instance Base = declarative_base():
"""
from sqlalchemy import ForeignKey, Column
from sqlalchemy import String, CHAR, Integer
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()


class City(Base):
    """
    City class:

    - inherits from Base (imported from model_state)

    - links to the MySQL table cities
    - class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key

    - class attribute name that represents a column of a string of
    128 characters and can’t be null

    - class attribute state_id that represents a column of an integer,
    can’t be null and is a foreign key to states.id
    """
    __tablename__ = "cities"

    id = Column("id", Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer,
                      ForeignKey('states.id'), nullable=False)

    def __init__(self, name, state_id):
        """the constructor method"""
        self.name = name
        self.state_id = state_id
