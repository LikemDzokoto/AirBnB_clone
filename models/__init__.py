#!/usr/bin/python3
''' creates a unique FileStorage instance '''

from models.base_model import BaseModel
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
