#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place',
                           cascade='all,delete-orphan', uselist=True)

    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False, backref="Place")
    amenity_ids = []

    @property
    def reviews(self):
        """Retrieves a list of Review instances"""
        from models.review import Review
        return [rev for rev in self.all(Review) if rev.place_id == self.id]

    @property
    def amenities(self):
        """ get all amenities """
        return [amenity.id for amenity
                in models.storage.all('Amenity').values()]

    @amenities.setter
    def amenities(self, amenity):
        """ set amenity """
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
