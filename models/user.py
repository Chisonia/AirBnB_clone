#!/usr/bin/python3
from models.base_model import BaseModel 

class User(BaseModel):
    """User class inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")

    def __str__(self):
        """Return string representation of User instance"""
        user = "[User] ({}) {}".format(self.id, self.__dict__)
        return user