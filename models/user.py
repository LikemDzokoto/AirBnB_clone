#!/usr/bin/python3

import models


class User(models.base_model.BaseModel):
    ''''''
    def __init__(self):
        ''' inits a new user '''
        self.email = ''
        self.password = ''
        first_name = ''
        last_name = ''
        models.storage().new(self)
        models.storage.save()
