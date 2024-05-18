#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4

class TestUser(unittest.TestCase):
    def layOut(self):
        """Set up test methods"""
        self.user = User()

    def test_inherit(self):
        """Test that User inherits from BaseModel"""
        self.assertIsInstance(self.user, User)
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_init_without_kwargs(self):
        """Test __init__ without kwargs"""
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_init_with_kwargs(self):
        """Test __init__ with kwargs"""
        test_dict = {
            'id': str(uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'First',
            'last_name': 'Last'
        }
        user = User(**test_dict)
        self.assertEqual(user.id, test_dict['id'])
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertEqual(user.created_at.isoformat(), test_dict['created_at'])
        self.assertEqual(user.updated_at.isoformat(), test_dict['updated_at'])
        self.assertEqual(user.email, test_dict['email'])
        self.assertEqual(user.password, test_dict['password'])
        self.assertEqual(user.first_name, test_dict['first_name'])
        self.assertEqual(user.last_name, test_dict['last_name'])

    def test_str(self):
        """Test __str__ method"""
        user_str = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), user_str)

    def test_save(self):
        """Test save method"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'], self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], self.user.updated_at.isoformat())
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last_name)

if __name__ == '__main__':
    unittest.main()