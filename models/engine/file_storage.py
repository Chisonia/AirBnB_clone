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
    ALL_CLASS = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "Review": Review,
            "State": State,
            "City": City,
            "Amenity": Amenity
            }
    __file_path = os.path.join("./models", "file.json")
    __objects = {}

    def all(self):
        '''
        Public instance method that
        returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id
        '''
        obj_dict = obj.to_dict()
        key = "{}.{}".format(obj_dict['__class__'], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        serializes __objects to the JSON file (path: __file_path)
        '''
        obj_serialized = {}
        for key, value in self.__objects.items():
            obj_serialized[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(obj_serialized, file, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                obj_content = json.load(file)
                for key, value in obj_content.items():
                    class_name = value.get("__class__")
                    if class_name in self.ALL_CLASS:
                        new_instance = self.ALL_CLASS[class_name](**value)
                        self.__objects[key] = new_instance
        except FileNotFoundError:
            pass
