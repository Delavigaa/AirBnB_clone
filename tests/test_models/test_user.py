#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        pass

    def tearDown(self):
        """Tear down for the tests"""
        pass

    def test_user_attributes(self):
        """Test the attributes of the User class"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_instance(self):
        """Test the User class instance"""
        user = User()
        self.assertIsInstance(user, BaseModel)


if __name__ == '__main__':
    unittest.main()
