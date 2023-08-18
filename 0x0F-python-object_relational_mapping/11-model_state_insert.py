#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the hbtn_0e_6_usa database.
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create and add the new State object
    new_state = State(name="Louisiana")
    session.add(new_state)
    new_instance = session.query(State).filter_by(name='Louisiana').first()

    # Print the new states.id
    print(new_instance.id)
    session.commit()
    # Close the session
    session.close()
