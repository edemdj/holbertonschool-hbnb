#!/usr/bin/python3
import uuid
from datetime import datetime

class Place:
    def __init__(self, city_id, country_id, name, description, address, host, num_rooms, num_bathrooms, price, num_guests, coordinate):
        self.place_id = str(uuid.uuid4())
        self.city_id = city_id
        self.country_id = country_id
        self.name = name
        self.description = description
        self.address = address
        self.host = host
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price = price
        self.num_guests = num_guests
        self.coordinate = coordinate
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.review_place = []

    def add_review(self, review):
        self.review_place.append(review)
        self.updated_at = datetime.now()

    def __str__(self):
        return "[Place] ({}) {} by {}\n{}".format(self.place_id, self.name, self.host, self.updated_at)

# Exemple d'utilisation
place = Place(
    city_id="city_123",
    country_id="country_123",
    name="Beautiful Beach House",
    description="A lovely house by the beach.",
    address="123 Ocean Drive",
    host="Host_123",
    num_rooms=3,
    num_bathrooms=2,
    price=200.00,
    num_guests=6,
    coordinate=(34.052235, -118.243683)
)

print(place)
