#!/usr/bin/python3
'''This module is the City class unittest'''
import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from uuid import uuid4


class TestCity(unittest.TestCase):
    def layOut(self):
        '''Set up test methods'''
        self.city = City()

    def test_inherit(self):
        '''Test that City inherits from BaseModel'''
        self.assertIsInstance(self.city, City)
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_init_without_kwargs(self):
        '''Test __init__ without kwargs'''
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertEqual(self.city.state_id, '')
        self.assertEqual(self.city.name, '')

    def test_init_with_kwargs(self):
        '''Test __init__ with kwargs'''
        test_dict = {
            'id': str(uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'state_id': '12345',
            'name': 'Test City'
        }
        city = City(**test_dict)
        self.assertEqual(city.id, test_dict['id'])
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(city.created_at.isoformat(), test_dict['created_at'])
        self.assertEqual(city.updated_at.isoformat(), test_dict['updated_at'])
        self.assertEqual(city.state_id, test_dict['state_id'])
        self.assertEqual(city.name, test_dict['name'])

    def test_str(self):
        '''Test __str__ method'''
        city_str = '[City] ({}) {}'.format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), city_str)

    def test_save(self):
        '''Test save method'''
        prev_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, prev_updated_at)

    def test_to_dict(self):
        '''Test to_dict method'''
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(
                city_dict['created_at'], self.city.created_at.isoformat()
                )
        self.assertEqual(
                city_dict['updated_at'], self.city.updated_at.isoformat()
                )
        self.assertEqual(city_dict['state_id'], self.city.state_id)
        self.assertEqual(city_dict['name'], self.city.name)


if __name__ == '__main__':
    unittest.main()
