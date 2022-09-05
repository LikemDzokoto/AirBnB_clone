#!/usr/bin/python3
"""
BaseModel class
"""

from datetime import datetime
import models
import uuid


class BaseModel():
    ''' defines all common attr and methods for other classes '''
    """
    id = None
    created_at = None
    updated_at = None
    """
    def __init__(self, *args, **kwargs):
        ''' inits this instance '''
        t_format = '%Y-%m-%dT%H:%M:%S.%f'

        if kwargs:
            for k,v in kwargs.items():
                if k == "created_at" or k=="updated_at":
                    v = datetime.strptime(v,t_format)
                elif k =="__class__":
                    continue
                setattr(self, k,v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        ''' prints: [<ClassName>] (<self.id>) <self.__dict__> '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' updates the attr 'updated_at' with current datetime '''
        self.updated_at = datetime.now()
        models.storage.save()

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
