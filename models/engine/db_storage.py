#!/usr/bin/python3
"""This module defines the class DBStorage"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the class attributes and retrieves the environment
        variables"""
        url = 'mysql+mysqldb://{}:{}@{}/{}'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.environ["HBNB_MYSQL_USER"],
                                              os.environ["HBNB_MYSQL_PWD"],
                                              os.environ["HBNB_MYSQL_HOST"],
                                              os.environ["HBNB_MYSQL_DB"]),
                                      pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """get all data or by class """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        if cls is None:
            classes = [State, City, User, Amenity, Place, Review]
        else:
            classes = [cls]
        data = {}
        for clas in classes:
            result = self.__session.query(clas).all()
            for obj in result:
                key = "{}.{}".format(clas.__name__, obj.id)
                data[key] = obj
        return data

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """  delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """documented func"""
        return self.__session.close()
