#!/usr/bin/python3
"""
Defines Modules for FileStorage class
for serialization and deserialization.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Stores all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        cls_name = obj.__class__.__name__
        key = "{}.{}".format(cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_all = FileStorage.__objects
        obj_dict = {}
        for obj in obj_all.keys():
            obj_dict[obj] = obj_all[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        cls_name = value['__class__']
                        if cls_name == "BaseModel":
                            self.__objects[key] = BaseModel(**value)
                        elif cls_name == "User":
                            self.__objects[key] = User(**value)
                        elif cls_name == "State":
                            self.__objects[key] = State(**value)
                        elif cls_name == "City":
                            self.__objects[key] = City(**value)
                        elif cls_name == "Amenity":
                            self.__objects[key] = Amenity(**value)
                        elif cls_name == "Place":
                            self.__objects[key] = Place(**value)
                        elif cls_name == "Review":
                            self.__objects[key] = Review(**value)
                except Exception:
                    pass
