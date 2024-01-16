#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.city = City()

    def tearDown(self):
        """Tear down for the tests"""
        del self.city

    def test_state_id(self):
        """Test the state_id attribute"""
        self.assertEqual(self.city.state_id, "")

    def test_name(self):
        """Test the name attribute"""
        self.assertEqual(self.city.name, "")


if __name__ == '__main__':
    unittest.main()
