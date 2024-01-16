#!/usr/bin/python3
import json
import models


class FileStorage:
    """A class that represents a file storage system for objects in a JSON """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects stored in the file storage."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the file storage."""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Saves all objects in the file storage to a JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Reloads objects from the JSON file into the file storage."""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = key.split('.')[0]
                    if class_name == 'User':
                        obj = models.User(**value)
                    elif class_name == 'Place':
                        obj = models.Place(**value)
                    elif class_name == 'State':
                        obj = models.State(**value)
                    elif class_name == 'City':
                        obj = models.City(**value)
                    elif class_name == 'Amenity':
                        obj = models.Amenity(**value)
                    elif class_name == 'Review':
                        obj = models.Review(**value)
                    else:
                        obj = models.BaseModel(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
