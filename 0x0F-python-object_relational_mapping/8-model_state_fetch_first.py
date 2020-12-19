#!/usr/bin/python3
"""displays the first states with sqlalchemy"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def printall_states():
    """prints the first states"""
    ngin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                         .format(argv[1], argv[2], argv[3]),
                         pool_pre_ping=True)
    Session = sessionmaker(bind=ngin)
    s = Session()
    state = s.query(State).order_by(State.id).first
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    s.close()


if __name__ == "__main__":
    printall_states()
