import unittest
from datetime import datetime
from models.user import User
from persistence.data_manager import DataManager
from persistence.file_storage import FileStorage

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.data_manager = DataManager(self.storage)
        self.user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")

    def test_save_user(self):
        self.data_manager.save(self.user)
        saved_user = self.storage.get(self.user.user_id, User)
        self.assertIsNotNone(saved_user)
        self.assertEqual(saved_user.email, "test@example.com")

    def test_update_user(self):
        self.data_manager.save(self.user)
        self.user.first_name = "Jane"
        self.data_manager.update(self.user)
        updated_user = self.storage.get(self.user.user_id, User)
        self.assertEqual(updated_user.first_name, "Jane")

    def test_delete_user(self):
        self.data_manager.save(self.user)
        self.data_manager.delete(self.user.user_id, User)
        deleted_user = self.storage.get(self.user.user_id, User)
        self.assertIsNone(deleted_user)

if __name__ == "__main__":
    unittest.main()
