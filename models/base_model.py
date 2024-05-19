#!/usr/bin/python3
'''The module is the Base Model class which is the parent class'''
from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self):
        '''
        Initializing parent class Base Model
        Creating attributes id, created_at, and updated_at
        '''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        '''Function to return attribute as string'''
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self) -> None:
        '''method to save updated data'''
        self.updated_at = datetime.now()
        '''call save(self) method of storage'''


    def to_dict(self):

        '''method to store obj in dictionary'''
        air_dict = self.__dict__.copy()
        air_dict['created_at'] = self.created_at.isoformat()
        air_dict['updated_at'] = self.updated_at.isoformat()
        air_dict['__class__'] = self.__class__.__name__
        return air_dict
