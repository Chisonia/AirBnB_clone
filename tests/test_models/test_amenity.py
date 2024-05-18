#!/usr/bin/python3
'''This module is the Amenity class unittest'''
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4


class TestAmenity(unittest.TestCase):
    def layOut(self):
        '''Set up test methods'''
        self.amenity = Amenity()

    def test_inherit(self):
        '''Test that Amenity inherits from BaseModel'''
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_init_without_kwargs(self):
        '''Test __init__ without kwargs'''
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertEqual(self.amenity.name, '')

    def test_init_with_kwargs(self):
        '''Test __init__ with kwargs'''
        test_dict = {
            'id': str(uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'name': 'Test Amenity'
        }
        amenity = Amenity(**test_dict)
        self.assertEqual(amenity.id, test_dict['id'])
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.created_at.isoformat(), test_dict['created_at'])
        self.assertEqual(amenity.updated_at.isoformat(), test_dict['updated_at'])
        self.assertEqual(amenity.name, test_dict['name'])

    def test_str(self):
        '''Test __str__ method'''
        amenity_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), amenity_str)

    def test_save(self):
        '''Test save method'''
        prev_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, prev_updated_at)

    def test_to_dict(self):
        '''Test to_dict method'''
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['created_at'], self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict['name'], self.amenity.name)

if __name__ == '__main__':
    unittest.main()
