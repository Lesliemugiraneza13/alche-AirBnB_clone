#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test the Amenity class."""

    def test_docstrings(self):
        """Test that the module and the class are documented."""
        import models.amenity as module
        self.assertTrue(len(module.__doc__) > 5)
        self.assertTrue(len(Amenity.__doc__) > 5)

    def test_inherits_from_base_model(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(Amenity(), BaseModel)

    def test_base_attributes(self):
        """Test the attributes inherited from BaseModel."""
        obj = Amenity()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_default_attributes(self):
        """Test the type and default value of the class attributes."""
        obj = Amenity()
        self.assertEqual(obj.name, "")
        self.assertEqual(type(obj.name), type(""))

    def test_to_dict_and_back(self):
        """Test the round trip through to_dict."""
        obj = Amenity()
        data = obj.to_dict()
        self.assertEqual(data["__class__"], "Amenity")
        self.assertEqual(Amenity(**data).to_dict(), data)


if __name__ == "__main__":
    unittest.main()
