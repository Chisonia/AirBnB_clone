import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, str)
        self.assertIsInstance(self.base_model.updated_at, str)

    def test_str(self):
        expected_str = f"[BaseModel] ({self.base_model.id}) <{self.base_model.__dict__}>"
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        expected_dict = {
            "id": self.base_model.id,
            "class": "BaseModel",
            "created_at": self.base_model.created_at,
            "updated_at": self.base_model.updated_at
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()