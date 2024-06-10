import unittest
from datetime import datetime, timedelta
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(email="example@example.com", password="securepassword", first_name="John", last_name="Doe")

    def test_user_creation(self):
        self.assertIsInstance(self.user.user_id, str)
        self.assertEqual(self.user.email, "example@example.com")
        self.assertEqual(self.user.password, "securepassword")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_login_success(self):
        result = self.user.login(email="example@example.com", password="securepassword")
        self.assertTrue(result)

    def test_login_failure(self):
        result = self.user.login(email="wrong@example.com", password="wrongpassword")
        self.assertFalse(result)

    def test_logout(self):
        self.user.logout()  # Just testing if the method runs without errors

    def test_save_infos(self):
        self.user.save_infos(new_email="new@example.com", new_password="newpassword", new_first_name="Jane", new_last_name="Smith")
        self.assertEqual(self.user.email, "new@example.com")
        self.assertEqual(self.user.password, "newpassword")
        self.assertEqual(self.user.first_name, "Jane")
        self.assertEqual(self.user.last_name, "Smith")
        self.assertTrue(self.user.updated_at > self.user.created_at)

if __name__ == "__main__":
    unittest.main()
