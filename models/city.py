import uuid
from datetime import datetime

class city:
    def __init__(self, name, country_id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, name=None, country_id=None):
        if name:
            self.name = name
        if country_id:
            self.country_id = country_id
        self.updated_at = datetime.now()
