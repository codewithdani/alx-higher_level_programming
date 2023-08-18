#!/usr/bin/python3
"""
This script defines the State class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_city import Base, City

class State(Base):
    """
    State class with attributes id, name, cities.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")
