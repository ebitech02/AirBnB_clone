#!/usr/bin/python3
""" Define Module for the Review class. """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class to represent a user's review of a place

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
