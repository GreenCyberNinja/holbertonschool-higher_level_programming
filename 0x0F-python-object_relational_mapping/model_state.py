#!/usr/bin/python3
"""model for state table"""

from sqlalchemy import Column, Integer, String
from sqlachemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class State name and id"""
    __tablename__ = "states"

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
