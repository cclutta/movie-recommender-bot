#!/usr/bin/python3
""" User model module
"""
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
 
class User(Base):
    """User model """
    __tablename__ = "users"
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False)
    
