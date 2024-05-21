#!/usr/bin/python3
""" Test cases for Base model class """

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import os


class TestBaseModel(unittest.TestCase):
    """
    Base class module to test for various instances
    of class basemodel
    """
    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "temp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("temp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test the initialization of BaseModel instances."""
        my_model = BaseModel()
        # self.assertIsNotNone(my_model.id)
        # self.assertIsNotNone(my_model.created_at)
        # self.assertIsNotNone(my_model.updated_at)

        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(my_model.created_at, my_model.updated_at)

    def test_init_with_kwargs(self):
        """Test initializing BaseModel with kwargs."""
        dt = datetime.now().isoformat()
        dict_inst = {
            'id': '1234',
            'created_at': dt,
            'updated_at': dt,
            'name': 'Test'
        }
        my_model = BaseModel(**dict_inst)
        self.assertEqual(my_model.id, '1234')
        self.assertEqual(my_model.created_at, datetime.fromisoformat(dt))
        self.assertEqual(my_model.updated_at, datetime.fromisoformat(dt))
        self.assertEqual(my_model.name, 'Test')

    def test_unique_id(self):
        """Test that each BaseModel instance has a unique id."""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_save(self):
        """Test the save method updates the updated_at attribute."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        new_updated_at = my_model.save()
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test the to_dict method returns the correct dictionary."""
        my_model = BaseModel()
        dict_inst = my_model.to_dict()
        self.assertIsInstance(dict_inst, dict)
        self.assertEqual(dict_inst['id'], my_model.id)
        self.assertEqual(dict_inst["__class__"], 'BaseModel')
        self.assertEqual(dict_inst['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(dict_inst['updated_at'],
                         my_model.updated_at.isoformat())
        self.assertIsInstance(dict_inst['created_at'], str)
        self.assertIsInstance(dict_inst['updated_at'], str)

    def test_str(self):
        """Test the __str__ method returns the correct string."""
        my_model = BaseModel()
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)
        # my_model = BaseModel()
        # self.assertTrue(str(my_model).startswith('[BaseModel]'))
        # self.assertIn(my_model.id, str(my_model))
        # self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == '__main__':
    unittest.main()
