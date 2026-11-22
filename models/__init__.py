#!/usr/bin/python3
"""Initializes the models package and creates the unique FileStorage."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
