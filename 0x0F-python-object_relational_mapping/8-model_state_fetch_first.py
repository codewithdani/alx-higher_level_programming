#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    instance = session.query(State).order_by(State.id).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")

    session.close()
