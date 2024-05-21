#!/usr/bin/python3
'''This module is the State class unittest'''
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4


class TestState(unittest.TestCase):
    def setUp(self):
        '''Set up test methods'''
        self.state = State()

    def test_name(self):
        self.assertIsInstance(self.state.name, str)


if __name__ == '__main__':
    unittest.main()
