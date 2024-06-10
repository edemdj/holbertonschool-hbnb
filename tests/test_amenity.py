import unittest
from datetime import datetime
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity(name="Wi-Fi", user_id="12345")

    def test_amenity_creation(self):
        self.assertIsInstance(self.amenity.amenity_id, str)
        self.assertEqual(self.amenity.name, "Wi-Fi")
        self.assertEqual(self.amenity.user_id, "12345")
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_amenity_add(self):
        old_updated_at = self.amenity.updated_at
        self.amenity.amenity_add("Free Wi-Fi")
        self.assertEqual(self.amenity.name, "Free Wi-Fi")
        self.assertTrue(self.amenity.updated_at > old_updated_at)

if __name__ == "__main__":
    unittest.main()
