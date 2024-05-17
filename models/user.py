#!/usr/bin/python3
"""
Define Module for the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that handles users' information and inherits
    from the BaseModel class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
