#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines the class DBStorage"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
=======
"""his module defines a class to manage DB storage for hbnb clone """
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
>>>>>>> 9b452cff39b9b7b6f80dc8b3648b889a85ee5e2d
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


<<<<<<< HEAD
class DBStorage:
    """This class creates a new engine and session"""
=======

class DBStorage:
    """This class manages storage of hbnb models"""
>>>>>>> 9b452cff39b9b7b6f80dc8b3648b889a85ee5e2d
    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        """Initializes the class attributes and retrieves the environment variables"""
        url = 'mysql+mysqldb://{}:{}@{}/{}'
        self.__engine = create_engine(url.format(os.getenv('HBNB_MYSQL_USER'),
                                                 os.getenv('HBNB_MYSQL_PWD'),
                                                 os.getenv('HBNB_MYSQL_HOST'),
                                                 os.getenv('HBNB_MYSQL_DB'),
                                      pool_pre_ping=True)
                        )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects depending on the class"""
        session = self.__session
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        result = {}
        for clas in classes:
            query = session.query(clas).all()
            for value in query:
                key = "{}.{}".format(value.__class__.__name__, value.id)
                result[key] = value
        return result

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session obj if not None"""
        self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session = scoped_session(session_maker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
=======
        """ cretae engine """
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
        if cls == None:
            data = self.__session.query(State).all()
            data.extend(self.__session.query(City).all())
            data.extend(self.__session.query(User).all())
            """data.extend(self.__session.query(Amenity).all())
            data.extend(self.__session.query(Place).all())
            data.extend(self.__session.query(Review).all())"""
        else:
            data = self.__session.query(eval(cls)).all()
        return {"{}.{}".format(type(d).__name__, d.id): d for d in data}

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
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
>>>>>>> 9b452cff39b9b7b6f80dc8b3648b889a85ee5e2d
