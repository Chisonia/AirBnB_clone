#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4

class TestState(unittest.TestCase):
    def layOut(self):
        """Set up test methods"""
        self.state = State()

    def test_inherit(self):
        """Test that State inherits from BaseModel"""
        self.assertIsInstance(self.state, State)
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_init_without_kwargs(self):
        """Test __init__ without kwargs"""
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertEqual(self.state.name, "")

    def test_init_with_kwargs(self):
        """Test __init__ with kwargs"""
        test_dict = {
            'id': str(uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'name': 'Test State'
        }
        state = State(**test_dict)
        self.assertEqual(state.id, test_dict['id'])
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertEqual(state.created_at.isoformat(), test_dict['created_at'])
        self.assertEqual(state.updated_at.isoformat(), test_dict['updated_at'])
        self.assertEqual(state.name, test_dict['name'])

    def test_str(self):
        """Test __str__ method"""
        state_str = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), state_str)

    def test_save(self):
        """Test save method"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertEqual(state_dict['created_at'], self.state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'], self.state.updated_at.isoformat())
        self.assertEqual(state_dict['name'], self.state.name)

if __name__ == '__main__':
    unittest.main()