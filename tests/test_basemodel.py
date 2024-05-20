#!/usr/bin/python3
'''
This module tests the BaseModel class
'''
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        '''Set up test methods'''
        self.base = BaseModel()

    def test_id(self):
        self.assertIsInstance(self.base.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertTrue(hasattr(self.base, "created_at"))

    def test_updated_at(self):
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertTrue(hasattr(self.base, "updated_at"))

    def test_save(self):
        old_updated_at = self.base.updated_at
        time.sleep(1)  # Ensure there is a time difference between updates
        self.base.save()
        self.assertNotEqual(self.base.updated_at, old_updated_at)
        self.assertGreater(self.base.updated_at, old_updated_at)

    def test_to_dict(self):
        model_dict = self.base.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], self.base.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(
            model_dict['created_at'], self.base.created_at.isoformat()
            )
        self.assertEqual(
            model_dict['updated_at'], self.base.updated_at.isoformat()
            )

    def test_str(self):
        model_str = str(self.base)
        expected_str = f"[BaseModel] ({self.base.id}) {self.base.__dict__}"
        self.assertEqual(model_str, expected_str)


if __name__ == '__main__':
    unittest.main()
