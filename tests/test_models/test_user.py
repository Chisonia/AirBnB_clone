#!/usr/bin/python3
'''This module is the User class unittest'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        '''Set up test methods'''
        self.user = User(username='testuser', email='testuser@example.com')

    def test_init(self):
        '''Test initialization of User'''
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_update_email(self):
        '''Test update_email method'''
        new_email = 'newemail@example.com'
        self.user.update_email(new_email)
        self.assertEqual(self.user.email, new_email)

    def test_str(self):
        '''Test __str__ method'''
        expected_str = 'Username: testuser, Email: testuser@example.com'
        self.assertEqual(str(self.user), expected_str)

    def test_inheritance(self):
        '''Test that User inherits from BaseModel'''
        from models.base_model import BaseModel
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(self.user, BaseModel)


if __name__ == '__main__':
    unittest.main()
