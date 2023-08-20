#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the hbtn_0e_6_usa database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete State objects with names containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%'))
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()
