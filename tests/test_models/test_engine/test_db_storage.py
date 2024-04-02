#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
db = os.getenv('HBNB_TYPE_STORAGE')


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""
    @unittest.skipIf(db != 'db', "Testing DBStorage")
    def test_all(self):
        """Test the all method"""
        storage = DBStorage()
        storage.reload()
        all_objs = storage.all()
        self.assertIsNot(all_objs, None)
        self.assertEqual(type(all_objs), dict)
        self.assertIs(all_objs, storage._DBStorage__objects)

    @unittest.skipIf(db != 'db', "Testing DBStorage")
    def test_new(self):
        """Test the new method"""
        storage = DBStorage()
        storage.reload()
        all_objs = storage.all()
        state = State(name="California")
        state.save()
        self.assertIn('State.{}'.format(state.id), all_objs.keys())

    @unittest.skipIf(db != 'db', "Testing DBStorage")
    def test_save(self):
        """Test the save method"""
        storage = DBStorage()
        storage.reload()
        state = State(name="California")
        state.save()
        storage.save()
        path = "file.json"
        with open(path, "r") as f:
            self.assertNotEqual(len(f.read()), 0)
        os.remove(path)

    @unittest.skipIf(db != 'db', "Testing DBStorage")
    def test_get(self):
        """Test the get method"""
        storage = DBStorage()
        storage.reload()
        state = State(name="California")
        state.save()
        get_obj = storage.get("State", state.id)
        self.assertEqual(state, get_obj)

    @unittest.skipIf(db != 'db', "Testing DBStorage")
    def test_count(self):
        """Test the count method"""
        storage = DBStorage()
        storage.reload()
        count_states = storage.count("State")
        state = State(name="California")
        state.save()
        new_count_states = storage.count("State")
        self.assertEqual(count_states + 1, new_count_states)
        self.assertEqual(new_count_states, storage.count("State"))

    @unittest.skipIf(db != 'db', "Testing DBStorage")
    def test_delete(self):
        """Test the delete method"""
        storage = DBStorage()
        storage.reload()
        state = State(name="California")
        state.save()
        storage.delete(state)
        self.assertNotIn(state, storage.all().values())

    @unittest.skipIf(db != 'db', "Testing DBStorage")
    def test_close(self):
        """Test the close method"""
        storage = DBStorage()
        storage.reload()
        storage.close()
        with self.assertRaises(AttributeError):
            print(storage._DBStorage__session)
        with self.assertRaises(AttributeError):
            print(storage._DBStorage__engine)

    @unittest.skipIf(db != 'db', "Testing DBStorage")
    def test_all_no_cls(self):
        """Test the all method without passing a class"""
        storage = DBStorage()
        storage.reload()
        state = State(name="California")
        state.save()
        all_objs = storage.all()
        self.assertEqual(all_objs, storage.all())
        self.assertIn(state, all_objs.values())
