#!/usr/bin/python3
'''This module is the Place class unittest'''
import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
from uuid import uuid4


class TestPlace(unittest.TestCase):
    def setUp(self):
        '''Set up test methods'''
        self.place = Place()

    def test_city_id(self):
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id(self):
        self.assertIsInstance(self.place.user_id, str)

    def test_name(self):
        self.assertIsInstance(self.place.name, str)

    def test_description(self):
        self.assertIsInstance(self.place.description, str)

    def test_rooms(self):
        self.assertIsInstance(self.place.number_rooms, int)

    def test_bathrooms(self):
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest(self):
        self.assertIsInstance(self.place.max_guest, int)

    def test_bathrooms(self):
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_price_night(self):
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude(self):
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude(self):
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids(self):
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
