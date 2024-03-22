#!/usr/bin/python3
"""
a script that lists all City objects from the database hbtn_0e_6_usa
"""
import sys
from model_city import City
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(City).filter(
        State.id == City.state_id).order_by(City.id)
    results2 = session.query(State).filter(
        State.id == City.state_id).order_by(City.id)
    for index, result in enumerate(results):
        print(f"{results2[index].name}: ({result.id}) {result.name}")
