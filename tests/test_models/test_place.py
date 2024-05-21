#!/usr/bin/python3
""" Define Module for Place class unittest

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""

import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Place class.
    """
    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(plac_nam))
        self.assertNotIn("city_id", plac_nam.__dict__)

    def test_user_id_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(plac_nam))
        self.assertNotIn("user_id", plac_nam.__dict__)

    def test_name_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(plac_nam))
        self.assertNotIn("name", plac_nam.__dict__)

    def test_description_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(plac_nam))
        self.assertNotIn("desctiption", plac_nam.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(plac_nam))
        self.assertNotIn("number_rooms", plac_nam.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(plac_nam))
        self.assertNotIn("number_bathrooms", plac_nam.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(plac_nam))
        self.assertNotIn("max_guest", plac_nam.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(plac_nam))
        self.assertNotIn("price_by_night", plac_nam.__dict__)

    def test_latitude_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(plac_nam))
        self.assertNotIn("latitude", plac_nam.__dict__)

    def test_longitude_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(plac_nam))
        self.assertNotIn("longitude", plac_nam.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        plac_nam = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(plac_nam))
        self.assertNotIn("amenity_ids", plac_nam.__dict__)

    def test_two_places_unique_ids(self):
        plac_nam1 = Place()
        plac_nam2 = Place()
        self.assertNotEqual(plac_nam1.id, plac_nam2.id)

    def test_two_places_different_created_at(self):
        plac_nam1 = Place()
        sleep(0.05)
        plac_nam2 = Place()
        self.assertLess(plac_nam1.created_at, plac_nam2.created_at)

    def test_two_places_different_updated_at(self):
        plac_nam1 = Place()
        sleep(0.05)
        plac_nam2 = Place()
        self.assertLess(plac_nam1.updated_at, plac_nam2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        plac_nam_repr = repr(dt)
        plac_nam = Place()
        plac_nam.id = "234567"
        plac_nam.created_at = plac_nam.updated_at = dt
        plac_nam_str = plac_nam.__str__()
        self.assertIn("[Place] (234567)", plac_nam_str)
        self.assertIn("'id': '234567'", plac_nam_str)
        self.assertIn("'created_at': " + plac_nam_repr, plac_nam_str)
        self.assertIn("'updated_at': " + plac_nam_repr, plac_nam_str)

    def test_args_unused(self):
        plac_nam = Place(None)
        self.assertNotIn(None, plac_nam.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        plac_nam = Place(id="777", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(plac_nam.id, "777")
        self.assertEqual(plac_nam.created_at, dt)
        self.assertEqual(plac_nam.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """
    Unittests for testing save method of the Place class.
    """
    def setUp(self):
        try:
            os.rename("file.json", "temp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("temp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_one_save(self):
        plac_nam = Place()
        sleep(0.05)
        first_updated_at = plac_nam.updated_at
        plac_nam.save()
        self.assertLess(first_updated_at, plac_nam.updated_at)

    def test_two_saves(self):
        plac_nam = Place()
        sleep(0.05)
        first_updated_at = plac_nam.updated_at
        plac_nam.save()
        second_updated_at = plac_nam.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        plac_nam.save()
        self.assertLess(second_updated_at, plac_nam.updated_at)

    def test_save_with_arg(self):
        plac_nam = Place()
        with self.assertRaises(TypeError):
            plac_nam.save(None)

    def test_save_updates_file(self):
        plac_nam = Place()
        plac_nam.save()
        plac_nam_id = "Place." + plac_nam.id
        with open("file.json", "r") as f:
            self.assertIn(plac_nam_id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Place class.
    """
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        plac_nam = Place()
        self.assertIn("id", plac_nam.to_dict())
        self.assertIn("created_at", plac_nam.to_dict())
        self.assertIn("updated_at", plac_nam.to_dict())
        self.assertIn("__class__", plac_nam.to_dict())

    def test_to_dict_contains_added_attributes(self):
        plac_nam = Place()
        plac_nam.middle_name = "Tucky"
        plac_nam.my_number = 333
        self.assertEqual("Tucky", plac_nam.middle_name)
        self.assertIn("my_number", plac_nam.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        plac_nam = Place()
        plac_nam_dict = plac_nam.to_dict()
        self.assertEqual(str, type(plac_nam_dict["id"]))
        self.assertEqual(str, type(plac_nam_dict["created_at"]))
        self.assertEqual(str, type(plac_nam_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        plac_nam = Place()
        plac_nam.id = "234567"
        plac_nam.created_at = plac_nam.updated_at = dt
        to_dict = {
            'id': '234567',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(plac_nam.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        plac_nam = Place()
        self.assertNotEqual(plac_nam.to_dict(), plac_nam.__dict__)

    def test_to_dict_with_arg(self):
        plac_nam = Place()
        with self.assertRaises(TypeError):
            plac_nam.to_dict(None)


if __name__ == "__main__":
    unittest.main()
