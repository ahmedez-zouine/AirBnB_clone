#!/usr/bin/python3

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity class."""

    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()

    def test_instantiation(self):
        self.assertEqual(Amenity, type(self.amenity))
        self.assertEqual(str, type(self.amenity.id))
        self.assertEqual(datetime, type(self.amenity.created_at))
        self.assertEqual(datetime, type(self.amenity.updated_at))

    def test_attributes(self):
        self.assertIn("name", dir(self.amenity))
        self.assertNotIn("name", self.amenity.__dict__)

    def test_uniqueness(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)
        self.assertLess(am1.created_at, am2.created_at)
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_save(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_to_dict(self):
        self.assertTrue(dict, type(self.amenity.to_dict()))
        self.assertIn("id", self.amenity.to_dict())
        self.assertIn("created_at", self.amenity.to_dict())
        self.assertIn("updated_at", self.amenity.to_dict())
        self.assertIn("__class__", self.amenity.to_dict())


if __name__ == "__main__":
    unittest.main()
