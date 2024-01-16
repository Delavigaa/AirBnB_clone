#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        pass

    def tearDown(self):
        """Tear down for the tests"""
        pass

    def test_place_attributes(self):
        """Test the attributes of the Place class"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_instance(self):
        """Test the Place class instance"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_city_id(self):
        """Test the city_id attribute of the Place class"""
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_place_user_id(self):
        """Test the user_id attribute of the Place class"""
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_place_name(self):
        """Test the name attribute of the Place class"""
        place = Place()
        self.assertEqual(place.name, "")

    def test_place_description(self):
        """Test the description attribute of the Place class"""
        place = Place()
        self.assertEqual(place.description, "")

    def test_place_number_rooms(self):
        """Test the number_rooms attribute of the Place class"""
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_place_number_bathrooms(self):
        """Test the number_bathrooms attribute of the Place class"""
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_place_max_guest(self):
        """Test the max_guest attribute of the Place class"""
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_place_price_by_night(self):
        """Test the price_by_night attribute of the Place class"""
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_place_latitude(self):
        """Test the latitude attribute of the Place class"""
        place = Place()
        self.assertEqual(place.latitude, 0.0)

    def test_place_longitude(self):
        """Test the longitude attribute of the Place class"""
        place = Place()
        self.assertEqual(place.longitude, 0.0)

    def test_place_amenity_ids(self):
        """Test the amenity_ids attribute of the Place class"""
        place = Place()
        self.assertEqual(place.amenity_ids, [])
