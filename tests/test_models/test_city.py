#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class."""

    def test_docstrings(self):
        """Test that the module and the class are documented."""
        import models.city as module
        self.assertTrue(len(module.__doc__) > 5)
        self.assertTrue(len(City.__doc__) > 5)

    def test_inherits_from_base_model(self):
        """Test that City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(City(), BaseModel)

    def test_base_attributes(self):
        """Test the attributes inherited from BaseModel."""
        obj = City()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_default_attributes(self):
        """Test the type and default value of the class attributes."""
        obj = City()
        self.assertEqual(obj.state_id, "")
        self.assertEqual(type(obj.state_id), type(""))
        self.assertEqual(obj.name, "")
        self.assertEqual(type(obj.name), type(""))

    def test_to_dict_and_back(self):
        """Test the round trip through to_dict."""
        obj = City()
        data = obj.to_dict()
        self.assertEqual(data["__class__"], "City")
        self.assertEqual(City(**data).to_dict(), data)


if __name__ == "__main__":
    unittest.main()
