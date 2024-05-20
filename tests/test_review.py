#!/usr/bin/python3
'''This module is the Review class unittest'''
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
from uuid import uuid4


class TestReview(unittest.TestCase):
    def setUp(self):
        '''Set up test methods'''
        self.review = Review()

    def test_place_id(self):
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id(self):
        self.assertIsInstance(self.review.user_id, str)

    def test_text(self):
        self.assertIsInstance(self.review.text, str)


if __name__ == '__main__':
    unittest.main()
