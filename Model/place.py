import uuid
from datetime import datetime
from user import User
from amenity import Amenity
from city import City


class Place:
    def __init__(self, place_id, city_id, country_id, Name, Description, Address, Host, Num_rooms, Num_bathrooms, price, Num_guests, Coordinate):
        self.place_id = uuid.uuid4()
        self.city_id = city_id
        self.country_id = country_id
        self.Name = Name
        self.Description = Description
        self.Address = Address
        self.Host = Host
        self.Num_rooms = Num_rooms
        self.Num_bathrooms = Num_bathrooms
        self.price = price
        self.Num_guests = Num_guests
        self.Coordinate = Coordinate
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        @review_place.setter
        def review_place(self, review_place):
            self.review_place.append(review_place)

        def __str__(self):
            return "[Place] ({}) {} by {}\n{}".format(self.place_id, self.Name, self.Host, self.updated_at)