#!/usr/bin/python3
import unittest
from models.review import Review
from datetime import datetime
from uuid import uuid4

class TestReview(unittest.TestCase):
    def layout(self):
        '''Set up test methods'''
        self.review = Review()

    def test_inheritance(self):
        '''Test if Review inherits from BaseModel class'''
        self.assertIsInstance(self.review.id, str)
