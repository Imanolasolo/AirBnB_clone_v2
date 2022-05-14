#!/usr/bin/python3
# File: city.py
# Main Authors: Justin Majetich - Ezra Nobrega
# email(s): <justinmajetich@gmail.com>
#           <ezra.nobrega@outlook.com>
# Collaborators: Imanol Asolo - Alex Arévalo
# email(s): <3848@holbertonschool.com>
#           <3915@holbertonschool.com>

""" City Module for HBNB project """

import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(
        String(60), ForeignKey('states.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'Place',
        cascade='all, delete, delete-orphan',
        backref='cities'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
