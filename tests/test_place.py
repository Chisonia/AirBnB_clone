#!/usr/bin/python3
'''This module is the Place class unittest'''
import unittest
from models.base_model import BaseModel 
from models.place import Place
from datetime import datetime
from uuid import uuid4


class TestPlace(unittest.TestCase):
    def layout(self):
        '''Set up test methods'''
        self.place = Place()

    def test_inherit(self):
        '''Test that Place inherits from BaseModel'''
        self.assertIsInstance(self.place, Place)
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_init_without_kwargs(self):
        '''Test __init__ without kwargs'''
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertEqual(self.place.city_id, '')
        self.assertEqual(self.place.user_id, '')
        self.assertEqual(self.place.name, '')
        self.assertEqual(self.place.description, '')
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_init_with_kwargs(self):
        '''Test __init__ with kwargs'''
        test_dict = {
            'id': str(uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'city_id': '12345',
            'user_id': '67890',
            'name': 'Test Place',
            'description': 'Test Description',
            'number_rooms': 3,
            'number_bathrooms': 2,
            'max_guest': 5,
            'price_by_night': 100,
            'latitude': 12.34,
            'longitude': 56.78,
            'amenity_ids': ['987', '654']
        }
        place = Place(**test_dict)
        self.assertEqual(place.id, test_dict['id'])
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertEqual(place.created_at.isoformat(), test_dict['created_at'])
        self.assertEqual(place.updated_at.isoformat(), test_dict['updated_at'])
        self.assertEqual(place.city_id, test_dict['city_id'])
        self.assertEqual(place.user_id, test_dict['user_id'])
        self.assertEqual(place.name, test_dict['name'])
        self.assertEqual(place.description, test_dict['description'])
        self.assertEqual(place.number_rooms, test_dict['number_rooms'])
        self.assertEqual(place.number_bathrooms, test_dict['number_bathrooms'])
        self.assertEqual(place.max_guest, test_dict['max_guest'])
        self.assertEqual(place.price_by_night, test_dict['price_by_night'])
        self.assertEqual(place.latitude, test_dict['latitude'])
        self.assertEqual(place.longitude, test_dict['longitude'])
        self.assertEqual(place.amenity_ids, test_dict['amenity_ids'])

    def test_str(self):
        '''Test __str__ method'''
        place_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), place_str)

    def test_save(self):
        '''Test save method'''
        prev_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, prev_updated_at)

    def test_to_dict(self):
        '''Test to_dict method'''
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['created_at'], self.place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'], self.place.updated_at.isoformat())
        self.assertEqual(place_dict['city_id'], self.place.city_id)
        self.assertEqual(place_dict['user_id'], self.place.user_id)
        self.assertEqual(place_dict['name'], self.place.name)
        self.assertEqual(place_dict['description'], self.place.description)
        self.assertEqual(place_dict['number_rooms'], self.place.number_rooms)
        self.assertEqual(place_dict['number_bathrooms'], self.place.number_bathrooms)
        self.assertEqual(place_dict['max_guest'], self.place.max_guest)
        self.assertEqual(place_dict['price_by_night'], self.place.price_by_night)
        self.assertEqual(place_dict['latitude'], self.place.latitude)
        self.assertEqual(place_dict['longitude'], self.place.longitude)
        self.assertEqual(place_dict['amenity_ids'], self.place.amenity_ids)

if __name__ == '__main__':
    unittest.main()