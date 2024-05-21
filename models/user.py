#!/usr/bin/python3
'''This module is the User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User class inherits from BaseModel'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        '''Initialize User'''
        super().__init__(*args, **kwargs)
        