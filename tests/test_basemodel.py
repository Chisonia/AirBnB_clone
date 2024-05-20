#!/usr/bin/python3
'''
This module tests the BaseModel class
'''
import unittest
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import time

class TestBaseModel(unittest.TestCase):

    def test_id(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertEqual(len(model.id), 36)  # UUID length is 36 characters

    def test_created_at(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertTrue(hasattr(model, "created_at"))

    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(1)
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)
        self.assertGreater(model.updated_at, old_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_str(self):
        model = BaseModel()
        model_str = str(model)
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model_str, expected_str)


if __name__ == '__main__':
    unittest.main()