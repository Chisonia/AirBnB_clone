#!/usr/bin/python3
'''This module is the State class'''
from models.base_model import BaseModel


class State (BaseModel):
    '''State class inherits from BaseModel'''

    def __init__(self, *args, **kwargs):
        '''Initialize State instance'''
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
