#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Review class."""

    def test_docstrings(self):
        """Test that the module and the class are documented."""
        import models.review as module
        self.assertTrue(len(module.__doc__) > 5)
        self.assertTrue(len(Review.__doc__) > 5)

    def test_inherits_from_base_model(self):
        """Test that Review inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(Review(), BaseModel)

    def test_base_attributes(self):
        """Test the attributes inherited from BaseModel."""
        obj = Review()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_default_attributes(self):
        """Test the type and default value of the class attributes."""
        obj = Review()
        self.assertEqual(obj.place_id, "")
        self.assertEqual(type(obj.place_id), type(""))
        self.assertEqual(obj.user_id, "")
        self.assertEqual(type(obj.user_id), type(""))
        self.assertEqual(obj.text, "")
        self.assertEqual(type(obj.text), type(""))

    def test_to_dict_and_back(self):
        """Test the round trip through to_dict."""
        obj = Review()
        data = obj.to_dict()
        self.assertEqual(data["__class__"], "Review")
        self.assertEqual(Review(**data).to_dict(), data)


if __name__ == "__main__":
    unittest.main()
