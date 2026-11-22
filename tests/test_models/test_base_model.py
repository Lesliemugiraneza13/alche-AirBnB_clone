#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import os
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""

    def setUp(self):
        """Move any existing file.json out of the way."""
        if os.path.exists("file.json"):
            os.rename("file.json", "tmp_file.json")

    def tearDown(self):
        """Remove the test file.json and restore the original one."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("tmp_file.json"):
            os.rename("tmp_file.json", "file.json")

    def test_docstrings(self):
        """Test that the module, class and methods are documented."""
        import models.base_model as module
        self.assertTrue(len(module.__doc__) > 5)
        self.assertTrue(len(BaseModel.__doc__) > 5)
        for name in ("__init__", "__str__", "save", "to_dict"):
            self.assertTrue(len(getattr(BaseModel, name).__doc__) > 5)

    def test_id_is_unique_string(self):
        """Test that each instance gets a different string id."""
        a, b = BaseModel(), BaseModel()
        self.assertIsInstance(a.id, str)
        self.assertNotEqual(a.id, b.id)

    def test_dates_are_datetimes(self):
        """Test the type and initial value of the date attributes."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_str(self):
        """Test the string representation."""
        model = BaseModel()
        expected = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected)

    def test_save_updates_updated_at(self):
        """Test that save changes updated_at only and writes the file."""
        model = BaseModel()
        first = model.updated_at
        created = model.created_at
        model.save()
        self.assertGreater(model.updated_at, first)
        self.assertEqual(model.created_at, created)
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict(self):
        """Test the content of the dictionary representation."""
        model = BaseModel()
        model.name = "My Model"
        data = model.to_dict()
        self.assertEqual(data["__class__"], "BaseModel")
        self.assertEqual(data["name"], "My Model")
        self.assertEqual(data["id"], model.id)
        self.assertEqual(data["created_at"], model.created_at.isoformat())
        self.assertEqual(data["updated_at"], model.updated_at.isoformat())
        self.assertIsInstance(data["created_at"], str)

    def test_to_dict_does_not_change_instance(self):
        """Test that to_dict leaves the instance attributes untouched."""
        model = BaseModel()
        model.to_dict()
        self.assertNotIn("__class__", model.__dict__)
        self.assertIsInstance(model.created_at, datetime)

    def test_from_dict(self):
        """Test re-creating an instance from its dictionary."""
        model = BaseModel()
        model.name = "My Model"
        new = BaseModel(**model.to_dict())
        self.assertIsNot(model, new)
        self.assertEqual(new.id, model.id)
        self.assertEqual(new.name, "My Model")
        self.assertEqual(new.created_at, model.created_at)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertNotIn("__class__", new.__dict__)
        self.assertEqual(new.to_dict(), model.to_dict())

    def test_args_are_ignored(self):
        """Test that positional arguments are not used."""
        model = BaseModel("ignored", 89)
        self.assertNotIn("ignored", model.__dict__.values())

    def test_new_instance_is_stored(self):
        """Test that a new instance is registered in storage."""
        model = BaseModel()
        self.assertIn("BaseModel.{}".format(model.id), storage.all())

    def test_instance_from_dict_is_not_stored_again(self):
        """Test that rebuilding from a dict does not call storage.new."""
        data = BaseModel().to_dict()
        count = len(storage.all())
        BaseModel(**data)
        self.assertEqual(len(storage.all()), count)


if __name__ == "__main__":
    unittest.main()
