#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import json
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def setUp(self):
        """Move any existing file.json out of the way and empty storage."""
        if os.path.exists("file.json"):
            os.rename("file.json", "tmp_file.json")
        self.saved = dict(storage.all())
        storage.all().clear()

    def tearDown(self):
        """Restore storage and the original file.json."""
        storage.all().clear()
        storage.all().update(self.saved)
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("tmp_file.json"):
            os.rename("tmp_file.json", "file.json")

    def test_docstrings(self):
        """Test that the module, class and methods are documented."""
        import models.engine.file_storage as module
        self.assertTrue(len(module.__doc__) > 5)
        self.assertTrue(len(FileStorage.__doc__) > 5)
        for name in ("all", "new", "save", "reload"):
            self.assertTrue(len(getattr(FileStorage, name).__doc__) > 5)

    def test_storage_is_file_storage(self):
        """Test that storage is an instance of FileStorage."""
        self.assertIsInstance(storage, FileStorage)

    def test_all_returns_dict(self):
        """Test that all returns the dictionary of objects."""
        self.assertIsInstance(storage.all(), dict)
        self.assertIs(storage.all(), storage.all())

    def test_new_uses_class_name_and_id_as_key(self):
        """Test the key format used by new."""
        user = User()
        self.assertIs(storage.all()["User.{}".format(user.id)], user)

    def test_save_writes_json(self):
        """Test that save writes the dictionaries of the objects."""
        model = BaseModel()
        storage.save()
        with open("file.json", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data["BaseModel.{}".format(model.id)],
                         model.to_dict())

    def test_reload_restores_objects(self):
        """Test that reload rebuilds objects of the right classes."""
        model = BaseModel()
        user = User()
        user.email = "a@b.c"
        storage.save()
        storage.all().clear()
        storage.reload()
        restored = storage.all()
        self.assertIsInstance(restored["BaseModel." + model.id], BaseModel)
        self.assertIsInstance(restored["User." + user.id], User)
        self.assertEqual(restored["User." + user.id].email, "a@b.c")
        self.assertEqual(restored["User." + user.id].to_dict(),
                         user.to_dict())

    def test_reload_without_file(self):
        """Test that reload does nothing when the file is missing."""
        storage.reload()
        self.assertEqual(storage.all(), {})


if __name__ == "__main__":
    unittest.main()
