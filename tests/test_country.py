import unittest
from datetime import datetime
from models.country import Country

class TestCountry(unittest.TestCase):
    def test_country_creation(self):
        country = Country(name="France")
        self.assertIsNotNone(country.id)
        self.assertEqual(country.name, "France")
        self.assertIsInstance(country.created_at, datetime)
        self.assertIsInstance(country.updated_at, datetime)

    def test_country_update(self):
        country = Country(name="France")
        old_updated_at = country.updated_at
        country.update(name="Germany")
        self.assertEqual(country.name, "Germany")
        self.assertNotEqual(country.updated_at, old_updated_at)

if __name__ == "__main__":
    unittest.main()
