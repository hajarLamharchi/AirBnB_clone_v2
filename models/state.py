#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import Base
from sqlalchemy.orm import relationship, Session
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False
                  )

    cities = relationship('City',
                          backref='state',
                          cascade='all,delete-orphan',
                          uselist=True)

    @property
    def cities(self):
        """function documentation"""
        cities = []
        all_cities = storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
