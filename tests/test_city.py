#!/usr/bin/python3
'''This module is the City class unittest'''
import unittest
from models.city import City



class TestCity(unittest.TestCase):
    def setUp(self):
        '''Set up test methods'''
        self.city = City()

    def test_name(self):
        self.assertIsInstance(self.city.name, str)

    def test_state_id(self):
        self.assertIsInstance(self.city.state_id, str)


if __name__ == '__main__':
    unittest.main()
