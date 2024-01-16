#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        pass

    def tearDown(self):
        """Tear down for the tests"""
        pass

    def test_review_attributes(self):
        """Test the attributes of the Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_instance(self):
        """Test the Review class instance"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_place_id(self):
        """Test the place_id attribute of the Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_review_user_id(self):
        """Test the user_id attribute of the Review class"""
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_review_text(self):
        """Test the text attribute of the Review class"""
        review = Review()
        self.assertEqual(review.text, "")
