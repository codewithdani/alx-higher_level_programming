#!/usr/bin/python3
"""
This script defines the City class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City class with attributes id, name, and state_id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
