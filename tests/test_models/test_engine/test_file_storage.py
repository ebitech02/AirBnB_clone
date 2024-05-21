#!/usr/bin/python3
""" Define Module for FilStorage unittest """

import unittest
import os
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    Unittests for testing methods of the FileStorage class.
    """
    def setUp(self):
        """Set up test methods by creating a temporary test file if needed."""
        try:
            os.rename("file.json", "temp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("temp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new(self):
        """Test the new method adds an object to __objects."""
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        cty = City()
        amenty = Amenity()
        rev = Review()
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(cty)
        models.storage.new(amenty)
        models.storage.new(rev)
        self.assertIn("BaseModel." + base_model.id,
                      models.storage.all().keys())
        self.assertIn(base_model, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + amenty.id, models.storage.all().keys())
        self.assertIn(amenty, models.storage.all().values())
        self.assertIn("Review." + rev.id, models.storage.all().keys())
        self.assertIn(rev, models.storage.all().values())

    def test_new_with_args(self):
        """
        Test creating a new object with additional arguments
        It raises TypeError exception
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """
        Test creating a new object with None
        It raises AttributeError
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """Test the save method serializes __objects to the JSON file."""
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        cty = City()
        amenty = Amenity()
        rev = Review()
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(cty)
        models.storage.new(amenty)
        models.storage.new(rev)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + cty.id, save_text)
            self.assertIn("Amenity." + amenty.id, save_text)
            self.assertIn("Review." + rev.id, save_text)
            self.assertTrue(os.path.exists
                            (models.storage._FileStorage__file_path))

    def test_reload(self):
        """Test the reload method deserializes the JSON file to __objects."""
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        cty = City()
        amenty = Amenity()
        rev = Review()
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(cty)
        models.storage.new(amenty)
        models.storage.new(rev)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + cty.id, objs)
        self.assertIn("Amenity." + amenty.id, objs)
        self.assertIn("Review." + rev.id, objs)

    def test_reload_empty_file(self):
        """Test that reload does nothing if the JSON file does not exist."""
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()

    def test_save_and_reload(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        models.storage.new(base_model1)
        models.storage.new(base_model2)
        models.storage.save()

        # Create new storage instance to stimulate reloading
        new_storage = FileStorage()
        new_storage.reload()

        # Check if reloaded objects match the original objects
        self.assertTrue(new_storage.all().
                        get("BaseModel.{}".format(base_model1.id)) is not None)
        self.assertTrue(new_storage.all().
                        get("BaseModel.{}".format(base_model2.id)) is not None)

    def test_all_storage_returns_dictionary(self):
        """Test the all method returns the __objects dictionary."""
        self.assertEqual(dict, type(models.storage.all()))


if __name__ == '__main__':
    unittest.main()
