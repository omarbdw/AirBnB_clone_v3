#!/usr/bin/python3
""" test for api/v1/views/index.py """
import unittest
from api.v1.app import app


class TestIndex(unittest.TestCase):
    """ test for index.py """


def test_status(self):
    """ check status route """
    with app.test_client() as c:
        rv = c.get('/api/v1/status')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.data, b'{\n  "status": "OK"\n}\n')


def test_stats(self):
    """ check stats route """
    with app.test_client() as c:
        rv = c.get('/api/v1/stats')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'users', rv.data)
        self.assertIn(b'places', rv.data)
        self.assertIn(b'states', rv.data)
        self.assertIn(b'cities', rv.data)
        self.assertIn(b'amenities', rv.data)
        self.assertIn(b'reviews', rv.data)


if __name__ == "__main__":
    unittest.main()
