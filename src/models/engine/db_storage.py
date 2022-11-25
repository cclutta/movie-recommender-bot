#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User}

class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        CB_MYSQL_USER = 'root' # getenv('CB_MYSQL_USER')
        CB_MYSQL_PWD = 'root'
        CB_MYSQL_HOST = 'localhost'
        CB_MYSQL_DB = 'testbot'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(CB_MYSQL_USER,
                                             CB_MYSQL_PWD,
                                             CB_MYSQL_HOST,
                                             CB_MYSQL_DB))
    def all(self, cls=None):
        """query on the current database session"""
        return (self.__session.query(cls).all())
     
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
        
    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """reloads data from the database"""
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

