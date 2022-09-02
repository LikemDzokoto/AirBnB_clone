#!/usr/bin/python3
"""
BaseModel class
"""

from datetime import datetime
import uuid


class BaseModel():
    ''' defines all common attributes and methods for other classes '''

    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        ''' inits this instance '''
        for k, v in kwargs.items():
            if k == 'created_at' or k == 'updated_at':
                v = datetime.fromisoformat(v)
            if k != '__class__':
                setattr(self, k, v)
            else:
                pass

        if self.id is None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        ''' prints: [<ClassName>] (<self.id>) <self.__dict__> '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' updates the attr 'updated_at' with current datetime '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns a dict representation of this instance '''
        my_dict = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                ''' datetime.isoformat() '''
                v = v.isoformat()
            my_dict[k] = v

        my_dict["__class__"] = self.__class__.__name__
        return my_dict
