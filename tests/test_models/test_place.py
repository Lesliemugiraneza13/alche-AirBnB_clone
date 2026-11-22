#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the Place class."""

    def test_docstrings(self):
        """Test that the module and the class are documented."""
        import models.place as module
        self.assertTrue(len(module.__doc__) > 5)
        self.assertTrue(len(Place.__doc__) > 5)

    def test_inherits_from_base_model(self):
        """Test that Place inherits from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(Place(), BaseModel)

    def test_base_attributes(self):
        """Test the attributes inherited from BaseModel."""
        obj = Place()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_default_attributes(self):
        """Test the type and default value of the class attributes."""
        obj = Place()
        self.assertEqual(obj.city_id, "")
        self.assertEqual(type(obj.city_id), type(""))
        self.assertEqual(obj.user_id, "")
        self.assertEqual(type(obj.user_id), type(""))
        self.assertEqual(obj.name, "")
        self.assertEqual(type(obj.name), type(""))
        self.assertEqual(obj.description, "")
        self.assertEqual(type(obj.description), type(""))
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(type(obj.number_rooms), type(0))
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(type(obj.number_bathrooms), type(0))
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(type(obj.max_guest), type(0))
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(type(obj.price_by_night), type(0))
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(type(obj.latitude), type(0.0))
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(type(obj.longitude), type(0.0))
        self.assertEqual(obj.amenity_ids, [])
        self.assertEqual(type(obj.amenity_ids), type([]))

    def test_to_dict_and_back(self):
        """Test the round trip through to_dict."""
        obj = Place()
        data = obj.to_dict()
        self.assertEqual(data["__class__"], "Place")
        self.assertEqual(Place(**data).to_dict(), data)


if __name__ == "__main__":
    unittest.main()
