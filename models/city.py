#!/usr/bin/python3
'''This module is the City class'''
from models.base_model import BaseModel 


class City(BaseModel):
    '''City class inherits from BaseModel'''

    def __init__(self, *args, **kwargs):
        '''Initialize City instance'''
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')

    def __str__(self):
        '''Return string representation of City instance'''
        city = '[City] ({}) {}'.format(self.id, self.__dict__)
        return 