#!/usr/bin/python3

""" this is the base for all my models"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ this is the base class for all my classes"""
    def __init__(self, *args, **kwargs):
        """initializes the base class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns the string repr of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves the object to the json filee"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """converts the object to a dictionary"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
