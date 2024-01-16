#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down for the tests"""
        del self.amenity

    def test_name_initialization(self):
        """Test the initialization of the name attribute"""
        self.assertEqual(self.amenity.name, "")

    def test_name_assignment(self):
        """Test the assignment of the name attribute"""
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")


if __name__ == '__main__':
    unittest.main()
