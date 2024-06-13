#!/usr/bin/python3
import uuid
from datetime import datetime
from models.place import Place
from models.user import User

class Review:
    def __init__(self, place, user, rating, comment=""):
        self.id = str(uuid.uuid4())
        self.place_id = place.place_id if isinstance(place, Place) else place
        self.user_id = user.user_id if isinstance(user, User) else user
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def write_comment(self, comment=""):
        self.comment = comment
        self.updated_at = datetime.now()

    def __str__(self):
        return "[Review] ({}) {} by {}\n{}".format(self.id, self.comment, self.user_id, self.updated_at)

    def to_dict(self):
        return {
            'id': self.id,
            'place_id': self.place_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
