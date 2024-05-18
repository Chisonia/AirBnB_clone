#!/usr/bin/python3
'''This module is the Review class unittest'''
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
from uuid import uuid4


class TestReview(unittest.TestCase):
    def layout(self):
        '''Set up test methods'''
        self.review = Review()

    def test_inherit(self):
        '''Test if Review inherits from BaseModel class'''
        self.assertIsInstance(self.review, Review)
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_init_without_kwargs(self):
        '''Test __init__ without kwargs'''
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertIsInstance(self.review.place_id, '')
        self.assertIsInstance(self.review.user_id, '')
        self.assertIsInstance(self.review.text, '')

    def test_init_with_kwargs(self):
        '''Test __init__ with kwargs'''
        test_dict = {
                    'id': str(uuid4()),
                    'created_at': datetime.now().isoformat(),
                    'updated_at': datetime.now().isoformat(),
                    'place_id': '12345',
                    'user_id': '67890',
                    'text': 'Test review'
                }
        review = Review(**test_dict)
        self.assertEqual(review.id, test_dict['id'])
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertEqual(
            review.created_at.isoformat(), test_dict['created_at']
            )
        self.assertEqual(
            review.updated_at.isoformat(), test_dict['updated_at']
            )
        self.assertEqual(
            review.place_id, test_dict['place_id']
            )
        self.assertEqual(
            review.user_id, test_dict['user_id']
            )
        self.assertEqual(review.text, test_dict['text'])

    def test_str(self):
        '''Test __str__ method'''
        review_str = '[Review] ({}) {}'.format(
            self.review.id, self.review.__dict__
            )
        self.assertEqual(str(self.review), review_str)

    def test_save(self):
        '''Test save method'''
        prev_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, prev_updated_at)

    def test_to_dict(self):
        '''Test to_dict method'''
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertEqual(
            review_dict['created_at'], self.review.created_at.isoformat()
            )
        self.assertEqual(
            review_dict['updated_at'], self.review.updated_at.isoformat()
            )
        self.assertEqual(
            review_dict['place_id'], self.review.place_id)
        self.assertEqual(review_dict['user_id'], self.review.user_id
                         )
        self.assertEqual(review_dict['text'], self.review.text)


if __name__ == '__main__':
    unittest.main() 
 