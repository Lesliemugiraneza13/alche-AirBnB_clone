#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class."""

    def test_docstrings(self):
        """Test that the module and the class are documented."""
        import models.user as module
        self.assertTrue(len(module.__doc__) > 5)
        self.assertTrue(len(User.__doc__) > 5)

    def test_inherits_from_base_model(self):
        """Test that User inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(User(), BaseModel)

    def test_base_attributes(self):
        """Test the attributes inherited from BaseModel."""
        obj = User()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_default_attributes(self):
        """Test the type and default value of the class attributes."""
        obj = User()
        self.assertEqual(obj.email, "")
        self.assertEqual(type(obj.email), type(""))
        self.assertEqual(obj.password, "")
        self.assertEqual(type(obj.password), type(""))
        self.assertEqual(obj.first_name, "")
        self.assertEqual(type(obj.first_name), type(""))
        self.assertEqual(obj.last_name, "")
        self.assertEqual(type(obj.last_name), type(""))

    def test_to_dict_and_back(self):
        """Test the round trip through to_dict."""
        obj = User()
        data = obj.to_dict()
        self.assertEqual(data["__class__"], "User")
        self.assertEqual(User(**data).to_dict(), data)


if __name__ == "__main__":
    unittest.main()
