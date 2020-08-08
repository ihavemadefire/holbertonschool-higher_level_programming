#!/usr/bin/python3
"""This module creates a select all function"""
import sys
from sqlalchemy.sql import select
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == sys.argv[4])
    if result.count() == 0:
        print("Not found")
    else:
        for row in result:
            print(row.id)
