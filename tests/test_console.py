#!/usr/bin/python3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        pass

    def tearDown(self):
        """Tear down for the tests"""
        pass

    def test_do_quit(self):
        """Test the do_quit method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), '')

    def test_do_EOF(self):
        """Test the do_EOF method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), '')

    def test_do_create(self):
        """Test the do_create method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_show(self):
        """Test the do_show method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_destroy(self):
        """Test the do_destroy method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_all(self):
        """Test the do_all method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_update(self):
        """Test the do_update method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_count(self):
        """Test the do_count method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_update_with_dict(self):
        """Test the do_update_with_dict method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "update BaseModel 1234-1234-1234 {'name': 'test'}"
                                )
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_default(self):
        """Test the default method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("randomcommand")
            self.assertEqual(f.getvalue(),
                             "*** Unknown syntax: randomcommand\n")


if __name__ == '__main__':
    unittest.main()
