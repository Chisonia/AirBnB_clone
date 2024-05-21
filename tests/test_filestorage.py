#!/usr/bin/python3
'''This module tests the file storage class'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test methods"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.storage.new(self.base_model)

    def test_all(self):
        """Test that all() returns the correct dictionary of objects"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn('BaseModel.{}'.format(self.base_model.id), objects)
        self.assertEqual(objects['BaseModel.{}'.format(self.base_model.id)], self.base_model)

    def test_objects_attribute(self):
        """Test that __objects is a dictionary"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

if __name__ == '__main__':
    unittest.main()
