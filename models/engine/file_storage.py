#!/usr/bin/python3

""" the file storage class """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """the FileStorate class that stores our data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all the stored objects"""
        return self.__objects

    def new(self, obj):
        """save the new object in the objects dict"""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """save the objects dict to the json file"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """reads from the json file and stores it in object dict"""
        try:
            with open(self.__file_path, "r") as f:
                objects_str = f.read()
            if (objects_str):
                json_content = json.loads(objects_str)
                for key, value in json_content.items():
                    class_name = globals()[value.get("__class__")]
                    self.__objects[key] = class_name(**value)
        except (FileNotFoundError, FileExistsError):
            pass
