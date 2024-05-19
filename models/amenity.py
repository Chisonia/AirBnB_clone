#!/usr/bin/python3
'''This module is the Amenity class'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity class inherits from BaseModel'''

    def __init__(self, *args, **kwargs):
        '''Initialize Amenity instance'''
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')

    def __str__(self):
        '''Return string representation of Amenity instance'''
        amenity = '[Amenity] ({}) {}'.format(self.id, self.__dict__)
        return amenity
