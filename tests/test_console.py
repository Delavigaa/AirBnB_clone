#!/usr/bin/python3
"""
there is the unittest for console
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
class TestConsole(unittest.TestCase):
    """
    its a methods for the console to tests it work correctly or not
    """
    def setUp(self):
        """
        setup of the console
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        teardown method
        """
        self.console = None

    def capture_output(self, command):
        """
        return a value for the input command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(command)
            return f.getvalue().strip()

    def test_quit(self):
        """
        check the quit command
        """
        output = self.capture_output("quit")
        self.assertEqual(output, "")

    def test_create(self):
        """
        creat instance for the base model
        """
        output = self.capture_output("create BaseModel")
        self.assertIn("BaseModel", output)

    def test_create_missing_class(self):
        """
        creating missing classes
        """
        output = self.capture_output("create")
        self.assertEqual(output, "** class name missing **")

    def test_show(self):
        """
        check if the output is correct
        """
        output = self.capture_output("show BaseModel 1234-1234-1234")
        self.assertEqual(output, "** no instance found **")

    def test_show_missing_class(self):
        """
        return the missing class
        """
        output = self.capture_output("show")
        self.assertEqual(output, "** class name missing **")



    def test_destroy(self):
        """
        check if it is destoried correctly
        """
        output = self.capture_output("destroy BaseModel 1234-1234-1234")
        self.assertEqual(output, "** no instance found **")

    def test_destroy_missing_class(self):
        """
        fork the missing class check
        """
        output = self.capture_output("destroy")
        self.assertEqual(output, "** class name missing **")



    def test_update(self):
        """
        check if it is updated or not
        """
        output = self.capture_output("update BaseModel 1234-1234-1234 name 'new name'")
        self.assertEqual(output, "** no instance found **")

    def test_update_missing_class(self):
        """
        update missing class check
        """
        output = self.capture_output("update")
        self.assertEqual(output, "** class name missing **")



    def test_all(self):
        """
        return all instance in base model
        """
        output = self.capture_output("all BaseModel")
        self.assertEqual(output, "[]")

    def test_all_missing_class(self):
        """
        all missing class test
        """
        output = self.capture_output("all")
        self.assertEqual(output, "** class name missing **")



    def test_count(self):
        """
        count the base model
        """
        output = self.capture_output("BaseModel.count()")
        self.assertEqual(output, "0")

    def test_count_missing_class(self):
        """
        count the missing class check
        """
        output = self.capture_output("count")
        self.assertEqual(output, "** class name missing **")



if __name__ == '__main__':
    unittest.main()

