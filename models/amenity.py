#!/usr/bin/python3
import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name, user_id):
        self.amenity_id = str(uuid.uuid4())
        self.name = name
        self.user_id = user_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def amenity_add(self, new_name):
        self.name = new_name
        self.updated_at = datetime.now()

    def __str__(self):
        return f"Amenity(ID: {self.amenity_id}, Name: {self.name}, User ID: {self.user_id}, Created At: {self.created_at}, Updated At: {self.updated_at})"


if __name__ == "__main__":

    amenity = Amenity(name="Wi-Fi", user_id="12345")
    print(amenity)

    amenity.amenity_add("Free Wi-Fi")
    print(amenity)
