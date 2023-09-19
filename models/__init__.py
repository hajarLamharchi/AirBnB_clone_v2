#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
<<<<<<< HEAD
from models.engine.file_storage import FileStorage
import os
from models.engine.db_storage import DBStorage

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
=======
import os


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
>>>>>>> 9b452cff39b9b7b6f80dc8b3648b889a85ee5e2d
    storage = FileStorage()
    storage.reload()
