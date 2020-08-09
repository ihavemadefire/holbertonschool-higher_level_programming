#!/usr/bin/python3
"""The declares a model for states"""
from model_state import Base
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """This is the state model"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'))
