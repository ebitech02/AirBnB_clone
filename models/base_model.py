#!/usr/bin/python3
"""
The imported modules below define the BaseModel class
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    A base class for other models to inherit from,
    providing common attributes and methods.

    Attributes:
        id (str): A unique identifier for each instance, generated using uuid4.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        If kwargs is not empty, each key-value pair in kwargs is used to set an
        attribute on the instance.
        The keys 'created_at' and 'updated_at' are converted from strings
        to datetime objects.

        If kwargs is empty, a new id is generated and created_at and updated_at
        are set to the current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of the instance's __dict__.

        The dictionary includes a key __class__ with
        the class name of the object, and the created_at and updated_at
        attributes are converted to strings in ISO format.
        """
        dict_inst = self.__dict__.copy()
        dict_inst['__class__'] = self.__class__.__name__
        dict_inst['created_at'] = self.created_at.isoformat()
        dict_inst['updated_at'] = self.updated_at.isoformat()
        return dict_inst

    def __str__(self):
        """
        Returns a string representation of the instance.

        The string is formatted as:
        [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    # Create a new instance of BaseModel
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                       my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
