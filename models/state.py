#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import Base
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
>>>>>>> 9b452cff39b9b7b6f80dc8b3648b889a85ee5e2d
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
<<<<<<< HEAD
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False
    )
    cities = relationship('City',
                          backref='state',
                          cascade='all,delete-orphan',
                          uselist=True)
=======
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    city = relationship("City", cascade="delete")

    @property
    def cities(self):
        session = Session(engine)
        states = session.query(City).filter(City.state_id == id).all()
        return states
>>>>>>> 9b452cff39b9b7b6f80dc8b3648b889a85ee5e2d
