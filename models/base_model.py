#!/usr/bin/python3
"""Defines the BaseModel class, parent of all the AirBnB models."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines the attributes and methods common to all the models."""

    def __init__(self, *args, **kwargs):
        """Create an instance, from a dictionary (kwargs) if one is given."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return the string [<class name>] (<id>) <__dict__>."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current time and save to storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary with all the instance attributes.

        Adds the __class__ key and converts the dates to ISO strings.
        """
        data = dict(self.__dict__)
        data["__class__"] = type(self).__name__
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data
