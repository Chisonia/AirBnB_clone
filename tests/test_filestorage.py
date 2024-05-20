#!/usr/bin/python3
'''This module tests the file storage class'''
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects

        # Ensure file.json does not exist before each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Tear down test environment"""
        # Clean up created file.json after each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all() method"""
        self.assertEqual(self.storage.all(), self.objects)

    def test_new(self):
        """Test new() method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "BaseModel." + obj.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, "r") as f:
            content = json.load(f)
        key = "BaseModel." + obj.id
        self.assertIn(key, content)

    def test_reload(self):
        """Test reload() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}  # Clear current objects
        self.storage.reload()
        key = "BaseModel." + obj.id
        self.assertIn(key, self.storage.all())

    def test_file_path(self):
        """Test file path attribute"""
        self.assertEqual(self.storage._FileStorage__file_path, self.file_path)

    def test_objects(self):
        """Test objects attribute"""
        self.assertEqual(self.storage._FileStorage__objects, self.objects)

if __name__ == '__main__':
    unittest.main()
