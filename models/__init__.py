#!/usr/bin/python3
# File: __init__.py
# Main Authors: Justin Majetich - Ezra Nobrega
# email(s): <justinmajetich@gmail.com>
#           <ezra.nobrega@outlook.com>
# Collaborators: Imanol Asolo - Alex Arévalo
# email(s): <3848@holbertonschool.com>
#           <3915@holbertonschool.com>

"""This module is A unique FileStorage/DBStorage instance for all models"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()


storage.reload()
