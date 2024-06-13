#!/usr/bin/python3
import uuid
from datetime import datetime

class Review:
    def __init__(self, place_id, user_id, rating, comment):
        self.review_id = str(uuid.uuid4())
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'review_id': self.review_id,
            'place_id': self.place_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
