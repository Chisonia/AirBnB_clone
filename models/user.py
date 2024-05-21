#!/usr/bin/python3
'''This module is the User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User class inherits from BaseModel'''

    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def update_email(self, new_email):
        self.email = new_email

    def __str__(self) -> str:
        return 'Username: {}, Email: {}'.format(self.username, self.email)


        