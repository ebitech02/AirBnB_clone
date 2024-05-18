#!/usr/bin/python3
"""
Unittest for User class

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""

import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_different_created_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_users_different_updated_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        user = User()
        user.id = "234567"
        user.created_at = user.updated_at = dt
        userstr = user.__str__()
        self.assertIn("[User] (234567)", userstr)
        self.assertIn("'id': '234567'", userstr)
        self.assertIn("'created_at': " + dt_repr, userstr)
        self.assertIn("'updated_at': " + dt_repr, userstr)

    def test_args_unused(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the class."""

    @classmethod
    def setUp(self):
        try:
            # self.test_file = "file.json"
            # models.storage.__file_path = self.test_file
            # models.storage.save()
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            # if os.path.exists(self.test_file):
            #     os.remove(self.test_file)
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_two_saves(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        user = User()
        user.save()
        userid = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(userid, f.read())

    # def test_user_attributes(self):
    #     # Create a new User instance
    #     test_user = User()
    #     # Check if the defaults values of email, password, firstname,
    #     # and lastname are empty strings
    #     self.assertEqual(test_user.email, "")
    #     self.assertEqual(test_user.password, "")
    #     self.assertEqual(test_user.first_name, "")
    #     self.assertEqual(test_user.last_name, "")

    # def test_user_str_representation(self):
    #     test_user = User()
    #     # Set the attributes of the user instance
    #     test_user.email = "johnDoe@gmail.com"
    #     test_user.password = "John123"
    #     test_user.first_name = "John"
    #     test_user.last_name = "Doe"
    #     # Get the string representation of the User instance
    #     user_str = str(test_user)
    #     # Check if the user, email, password, firstname
    #     # and lastname are present in the string representation
    #     self.assertIn("User", user_str)
    #     self.assertIn("johnDoe@gmail.com", user_str)
    #     self.assertIn("John123", user_str)
    #     self.assertIn("John", user_str)
    #     self.assertIn("Doe", user_str)

    # def test_user_instance_creation(self):
    #     test_user = User(email="johnDoe@gmail.com", password="John123",
    #                      first_name="John", last_name="Doe")
    #     # Check if the attributes are set correctly
    #     self.assertEqual(test_user.email, "johnDoe@gmail.com")
    #     self.assertEqual(test_user.password, "John123")
    #     self.assertEqual(test_user.first_name, "John")
    #     self.assertEqual(test_user.last_name, "Doe")

    # def test_user_id_generation(self):
    #     test_user = User()
    #     user2 = User()
    #     # Ensure the id attribute of each user instance is unique
    #     self.assertNotEqual(test_user.id, user2.id)


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user = User()
        user.middle_name = "Betty"
        user.my_number = 98
        self.assertEqual("Betty", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        user = User()
        user.id = "234567"
        user.created_at = user.updated_at = dt
        to_dict = {
            'id': '234567',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
