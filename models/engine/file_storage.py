#!/usr/bin/python3
'''
Persistent storage for base_model instances
'''
import json
import models


class FileStorage():
    ''' serializes instances to JSON & deserializes JSON to instances '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' adds obj with key ClassName.id into __objects '''
        my_key = f"BaseModel.{obj.id}"
        self.__objects[my_key] = obj

    def save(self):
        ''' serializes __objects to JSON path is __file_path '''
        my_dict = {}

        for k, v in self.__objects.items():
            # form instances to dictionaries
            my_dict[k] = v.to_dict()

        with open(self.__file_path, mode='w', encoding='UTF-8') as json_file:
            # serialize the list of dictionaries
            json.dump(my_dict, json_file)

    def reload(self):
        ''' deserializes JSON file to __objects '''
        try:
            with open(self.__file_path) as json_file:
                # get the list of dictionaries
                my_dict = json.load(json_file)

            for key, val in my_dict.items():
                # deserialize dicts to instances and add to __objects
                instance = models.BaseModel(**val)
                self.__objects[key] = instance

        except FileNotFoundError:
            pass

        return self.__objects
