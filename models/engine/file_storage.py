#!/usr/bin/python3
'''
  This module is class FileStorage that serializes instances
  to a JSON file and deserializes JSON file to instances
  Private class attributes __file_path string path to the JSON file
  and __objects empty dict that will store all objects by <class name>.id
  '''
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
import json
import os


class FileStorage:
    """Class for serializing and deserializing instances"""
    __file_path = os.path.join("./models", "file.json")
    __objects = {}


    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set obj in __objects with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        obj_serialized = {
            key: value.to_dict() for key, value in self.__objects.items()
            }
        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(obj_serialized, file, indent=2)

    def all_classes(self):
        '''Returns a dictionary of valid classes and their references'''
        classes = {
        'BaseModel': BaseModel,
        'User' : User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }
        return classes

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                obj_content = json.load(file)
                obj_content = {key: self.classes()[value['__class__']](**value)
                               for key, value in obj_content}
                self.__objects = obj_content
        except FileNotFoundError:
            pass
