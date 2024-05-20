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
    __file_path = os.path.join("./models", "file.json")
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value['__class__']
                    cls = globals().get(cls_name)
                    if cls:
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
