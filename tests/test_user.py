#!/usr/bin/python3
'''This module is the User class unittest'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        '''Set up test methods'''
        self.user = User()

    def test_email(self):
        self.assertIsInstance(self.user.email, str)

    def test_password(self):
        self.assertIsInstance(self.user.password, str)

    def test_first_name(self):
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name(self):
        self.assertIsInstance(self.user.last_name, str)


if __name__ == '__main__':
    unittest.main()
