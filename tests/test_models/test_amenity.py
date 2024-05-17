#!/usr/bin/python3
""" Define Module for Place class unittest

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""

import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Amenity class.
    """
    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amenty = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenty.__dict__)

    def test_two_amenities_unique_ids(self):
        amenty = Amenity()
        amenty2 = Amenity()
        self.assertNotEqual(amenty.id, amenty2.id)

    def test_two_amenities_different_created_at(self):
        amenty = Amenity()
        sleep(0.05)
        amenty2 = Amenity()
        self.assertLess(amenty.created_at, amenty2.created_at)

    def test_two_amenities_different_updated_at(self):
        amenty1 = Amenity()
        sleep(0.05)
        amenty2 = Amenity()
        self.assertLess(amenty1.updated_at, amenty2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        amenty = Amenity()
        amenty.id = "234567"
        amenty.created_at = amenty.updated_at = dt
        amentystr = amenty.__str__()
        self.assertIn("[Amenity] (234567)", amentystr)
        self.assertIn("'id': '234567'", amentystr)
        self.assertIn("'created_at': " + dt_repr, amentystr)
        self.assertIn("'updated_at': " + dt_repr, amentystr)

    def test_args_unused(self):
        amenty = Amenity(None)
        self.assertNotIn(None, amenty.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenty = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenty.id, "345")
        self.assertEqual(amenty.created_at, dt)
        self.assertEqual(amenty.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        amenty = Amenity()
        sleep(0.05)
        first_updated_at = amenty.updated_at
        amenty.save()
        self.assertLess(first_updated_at, amenty.updated_at)

    def test_two_saves(self):
        amenty = Amenity()
        sleep(0.05)
        first_updated_at = amenty.updated_at
        amenty.save()
        second_updated_at = amenty.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenty.save()
        self.assertLess(second_updated_at, amenty.updated_at)

    def test_save_with_arg(self):
        amenty = Amenity()
        with self.assertRaises(TypeError):
            amenty.save(None)

    def test_save_updates_file(self):
        amenty = Amenity()
        amenty.save()
        amentyid = "Amenity." + amenty.id
        with open("file.json", "r") as f:
            self.assertIn(amentyid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amenty = Amenity()
        self.assertIn("id", amenty.to_dict())
        self.assertIn("created_at", amenty.to_dict())
        self.assertIn("updated_at", amenty.to_dict())
        self.assertIn("__class__", amenty.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amenty = Amenity()
        amenty.middle_name = "Tucky"
        amenty.my_number = 345
        self.assertEqual("Tucky", amenty.middle_name)
        self.assertIn("my_number", amenty.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amenty = Amenity()
        amenty_dict = amenty.to_dict()
        self.assertEqual(str, type(amenty_dict["id"]))
        self.assertEqual(str, type(amenty_dict["created_at"]))
        self.assertEqual(str, type(amenty_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        amenty = Amenity()
        amenty.id = "234567"
        amenty.created_at = amenty.updated_at = dt
        to_dict = {
            'id': '234567',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(amenty.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        amenty = Amenity()
        self.assertNotEqual(amenty.to_dict(), amenty.__dict__)

    def test_to_dict_with_arg(self):
        amenty = Amenity()
        with self.assertRaises(TypeError):
            amenty.to_dict(None)


if __name__ == "__main__":
    unittest.main()
