#!/usr/bin/python3
'''The module is the Base Model class which is the parent class'''

from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self) -> None:

        '''
        Initializing parent class Base Model
        Creating attributes id, created_at, and updated_at
        '''

        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        


    def __str__(self) -> str:
       '''Function to return attribute as string'''

       return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"
    
    def save(self) -> None:
        '''method to save updated data'''
        self.updated_at = datetime.now().isoformat


    def to_dict(self):

        '''method to store obj in dictionary'''
        air_dict = self.__dict__.copy()
        air_dict["__class__"] = self.__class__.__name__
        air_dict["created_at"] = air_dict["created_at"]
        air_dict["updated_at"] = air_dict["updated_at"]
        return air_dict
    