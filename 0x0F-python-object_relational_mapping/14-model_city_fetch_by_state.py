#!/usr/bin/python3
"""This module creates a select all function"""
import sys
from sqlalchemy.sql import select
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    for c, s in session.query(City, State).filter(
            City.state_id == State.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
