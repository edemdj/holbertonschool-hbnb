#!/usr/bin/python3
import uuid
from datetime import datetime
from user import User
from place import Place


class Review:
    def __init__(self, place, user, note, comment=""):
        self.id = str(uuid.uuid4())
        self.user = user
        self.note = note
        self.comment = comment
        self.place = place
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        def write_comment(self, comment=""):
            self.comment = comment
            self.updated_at = datetime.now()

        def __str__(self):
            return "[Review] ({}) {} by {}\n{}".format(self.id, self.comment, self.user_id, self.updated_at)
