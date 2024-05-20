#!/usr/bin/python3
'''
  This module is class FileStorage that serializes instances
  to a JSON file and deserializes JSON file to instances
  Private class attributes __file_path string path to the JSON file
  and __objects empty dict that will store all objects by <class name>.id
  '''
from models.base_model import BaseModel
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

    classes = {
        'BaseModel': BaseModel,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

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
        with open(self.__file_path, "w") as file:
            json.dump(obj_serialized, file, indent=2)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                obj_content = json.load(file)
                for key, value in obj_content.items():
                    class_name = value.get("__class__")
                    if class_name in self.classes:
                        new_instance = self.classes[class_name](**value)
                        self.__objects[key] = new_instance
        except FileNotFoundError:
            pass
