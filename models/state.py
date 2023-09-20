#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False
                  )

    """cities = relationship('City',
                          backref='state',
                          cascade='all,delete-orphan',
                          uselist=True)
    @property
    def cities(self):
        session = Session(engine)
        states = session.query(City).filter(City.state_id == id).all()
        return states
        """
