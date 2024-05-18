#!/usr/bin/python3
""" Define module for state class """

from models.base_model import BaseModel


class State(BaseModel):
    """
    Representing a class state(geographical state) that inherits from
    Base class BaseModel

    Attribure:
        name(str): name of a state
    """
    name = ""
