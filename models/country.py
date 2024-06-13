#!/usr/bin/python3
import uuid
from datetime import datetime

class Country:
    def __init__(self, name, code):
        self.id = str(uuid.uuid4())
        self.name = name
        self.code = code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
