import uuid

class country:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, name=None):
        if name:
            self.name = name
        self.updated_at = datetime.now()
