import unittest
from datetime import datetime
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_creation(self):
        city = City(name="Paris", country_id="12345")
        self.assertIsNotNone(city.id)
        self.assertEqual(city.name, "Paris")
        self.assertEqual(city.country_id, "12345")
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_city_update(self):
        city = City(name="Paris", country_id="12345")
        old_updated_at = city.updated_at
        city.update(name="Berlin", country_id="67890")
        self.assertEqual(city.name, "Berlin")
        self.assertEqual(city.country_id, "67890")
        self.assertNotEqual(city.updated_at, old_updated_at)

if __name__ == "__main__":
    unittest.main()
