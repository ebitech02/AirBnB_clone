#!/usr/bin/python3
""" Define Module for the Amenity class. """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class to represent a feature or service offered.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
