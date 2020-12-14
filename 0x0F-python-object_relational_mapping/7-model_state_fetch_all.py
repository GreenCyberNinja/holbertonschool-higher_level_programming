#!/usr/bin/python3
"""displays all states with sqlalchemy"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def printall_states():
    """prints all the states"""
    ngin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                         .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=ngin)
    s = Session()
    for state in s.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    s.close()


if __name__ == "__main__":
    printall_states()
