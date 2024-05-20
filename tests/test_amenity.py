#!/usr/bin/python3
'''This module is the Amenity class unittest'''
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4


class TestAmenity(unittest.TestCase):
    def setUp(self):
        '''Set up test methods'''
        self.amenity = Amenity()
        print(self.amenity)

    def test_name(self):
        self.assertIsInstance(self.amenity.name, str)

if __name__ == '__main__':
    unittest.main()
