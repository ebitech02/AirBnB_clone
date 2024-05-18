# #!/usr/bin/python3
"""
Define Module for TestHBNBCommand class.

 Unittest classes:
     TestConsole
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            self.assertNotEqual(f.getvalue().strip(), "0")

    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            self.assertTrue(f.getvalue().strip() ==
                            "*** Unknown syntax: invalid_command")

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_create_user_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_all_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_update_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_count_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            self.assertNotEqual(f.getvalue().strip(), "0")

    def test_invalid_command_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            self.assertTrue(f.getvalue().strip() ==
                            "*** Unknown syntax: invalid_command")

    def test_quit_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
