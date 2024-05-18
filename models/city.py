#!/usr/bin/python3
"""
Define Module for the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a city within a state

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
