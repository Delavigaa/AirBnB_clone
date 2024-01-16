#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.state = State()

    def tearDown(self):
        """Tear down for the tests"""
        del self.state

    def test_name_initial_value(self):
        """Test the initial value of name"""
        self.assertEqual(self.state.name, "")

    def test_name_assignment(self):
        """Test assigning a value to name"""
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")


if __name__ == '__main__':
    unittest.main()
