#!/usr/bin/python3
"""
This script retrieves a State object by name from the hbtn_0e_6_usa database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_name = sys.argv[4]

    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object by name
    state = session.query(State).filter(State.name == (search_name,))

    try:
        print(state[0].id)
    except IndexError:
        print("Not found")
