from datetime import datetime
import uuid

class Country:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()
