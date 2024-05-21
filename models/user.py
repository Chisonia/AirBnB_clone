#!/usr/bin/python3
'''This module is the User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User class inherits from BaseModel'''

    def __init__(self, email='', first_name='', last_name='', password='', *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.email = email
         self.first_name = first_name
         self.last_name = last_name
         self.paswword = password

    def __str__(self) -> str:
        return (
            'email: {}, first_name: {}, last_name: {}, password: {}'.format(
            self.email, self.first_name, self.last_name, self.paswword
            )
            )

        