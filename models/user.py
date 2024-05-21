#!/usr/bin/python3
'''This module is the User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User class inherits from BaseModel'''

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
           
    def __str__(self) -> str:
        return 'email: {}, firstname: {}, last_name: {}, password: {}'.format(
            self.email, self.first_name, self.last_name, self.password)

        