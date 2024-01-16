#!/usr/bin/python3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        pass

    def tearDown(self):
        """Tear down for the tests"""
        pass

    def test_init(self):
        """Test the __init__ method of BaseModel"""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        base_model = BaseModel()
        string_representation = str(base_model)
        self.assertEqual(string_representation,
                         "[BaseModel] ({}) {}".format(base_model.id,
                                                      base_model.__dict__))

    def test_save(self):
        """Test the save method of BaseModel"""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        new_updated_at = base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertEqual(base_model_dict["id"], base_model.id)
        self.assertEqual(base_model_dict["created_at"],
                         base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"],
                         base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
