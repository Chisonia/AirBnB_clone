#!/usr/bin/python3
'''
This module tests the BaseModel class
'''
import unittest
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import models


class TestBaseModel(unittest.TestCase):
    def layOut(self):
        '''Set up test methods'''
        self.base_model = BaseModel()

    def test_init_without_kwargs(self):
        '''Test __init__ without kwargs'''
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(
            self.base_model.created_at, self.base_model.updated_at
            )

    def test_init_with_kwargs(self):
        '''Test __init__ with kwargs'''
        test_dict = {
            'id': str(uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'name': 'Test'
        }
        model = BaseModel(**test_dict)
        self.assertEqual(model.id, test_dict['id'])
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at.isoformat(), test_dict['created_at'])
        self.assertEqual(model.updated_at.isoformat(), test_dict['updated_at'])
        self.assertEqual(model.name, test_dict['name'])

    def test_str(self):
        '''Test __str__ method'''
        string = '[BaseModel] ({}) {}'.format(
            self.base_model.id, self.base_model.__dict__
            )
        self.assertEqual(str(self.base_model), string)

    def test_save(self):
        '''Test save method'''
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, prev_updated_at)

    def test_to_dict(self):
        '''Test to_dict method'''
        model_dict = self.base_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.base_model.id)
        self.assertEqual(
            model_dict['created_at'], self.base_model.created_at.isoformat()
            )
        self.assertEqual(
            model_dict['updated_at'], self.base_model.updated_at.isoformat()
            )

    def test_new_instance_stored(self):
        '''Test that a new instance is added to the storage'''
        self.assertIn(self.base_model, models.storage.all().values())


if __name__ == '__main__':
    unittest.main()
