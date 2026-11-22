#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test the State class."""

    def test_docstrings(self):
        """Test that the module and the class are documented."""
        import models.state as module
        self.assertTrue(len(module.__doc__) > 5)
        self.assertTrue(len(State.__doc__) > 5)

    def test_inherits_from_base_model(self):
        """Test that State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(State(), BaseModel)

    def test_base_attributes(self):
        """Test the attributes inherited from BaseModel."""
        obj = State()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_default_attributes(self):
        """Test the type and default value of the class attributes."""
        obj = State()
        self.assertEqual(obj.name, "")
        self.assertEqual(type(obj.name), type(""))

    def test_to_dict_and_back(self):
        """Test the round trip through to_dict."""
        obj = State()
        data = obj.to_dict()
        self.assertEqual(data["__class__"], "State")
        self.assertEqual(State(**data).to_dict(), data)


if __name__ == "__main__":
    unittest.main()
