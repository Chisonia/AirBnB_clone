#!/usr/bin/python3
'''The module is the Base Model class which is the parent class'''
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        '''Function to return attribute as string'''
        result = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return result

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
