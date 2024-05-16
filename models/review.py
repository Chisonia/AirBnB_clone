#!/usr/bin/python3
from models.base_model import BaseModel 

class Review(BaseModel):
    """Review class inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize Review instance"""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")

    def __str__(self):
        """Return string representation of Review instance"""
        review = "[Review] ({}) {}".format(self.id, self.__dict__)
        return review