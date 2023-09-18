#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = from sqlalchemy import Column, String, Integer
    password = from sqlalchemy import Column, String, Integer
    first_name = from sqlalchemy import Column, String, Integer
    last_name = from sqlalchemy import Column, String, Integer
