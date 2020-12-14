#!/usr/bin/python3
"""model for state table"""

from SQLAlchemy import Column, Integer, String
from SQLAlchemy.ext.declaritive import declaritive_base

Base = declaritive_base()


class State(Base):
    """class State name and id"""
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
