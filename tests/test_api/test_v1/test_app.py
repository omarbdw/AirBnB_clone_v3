#!/usr/bin/python3
""" test for app.py """
import unittest
from api.v1.app import app


class TestApp(unittest.TestCase):
    """ test for app.py """


def test_create_app(self):
    """ check app instance with blueprint is created """
    with app.test_client() as c:
        rv = c.get('/api/v1/status')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.data, b'{\n  "status": "OK"\n}\n')
        rv = c.get('/api/v1/unexisting_endpoint')
        self.assertEqual(rv.status_code, 404)
        self.assertEqual(rv.data, b'{\n  "error": "Not found"\n}\n')


if __name__ == "__main__":
    unittest.main()
