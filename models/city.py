#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import Base
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
>>>>>>> 9b452cff39b9b7b6f80dc8b3648b889a85ee5e2d


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
<<<<<<< HEAD
    state_id = Column(String(60),
                      ForeignKey('states.id'),
                      nullable=False
    )
    name = Column(String(128),
                  nullable=False
    )
=======
    state_id = Column(String(60), ForeignKey('states.id'))
    name =  Column(String(128), nullable=False)
>>>>>>> 9b452cff39b9b7b6f80dc8b3648b889a85ee5e2d
