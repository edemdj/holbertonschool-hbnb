#!/usr/bin/python3
import uuid
from datetime import datetime

class User:
    def __init__(self, email, password, first_name, last_name):
        self.user_id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def login(self, email, password):

        if self.email == email and self.password == password:
            print("Connexion réussie")
            return True
        else:
            print("Échec de la connexion")
            return False

    def logout(self):

        print(f"L'utilisateur {self.first_name} {self.last_name} s'est déconnecté")

    def save_infos(self, new_email=None, new_password=None, new_first_name=None, new_last_name=None):
        if new_email:
            self.email = new_email
        if new_password:
            self.password = new_password
        if new_first_name:
            self.first_name = new_first_name
        if new_last_name:
            self.last_name = new_last_name
        self.updated_at = datetime.now()

    def __str__(self):
        return f"User(ID: {self.user_id}, Email: {self.email}, First Name: {self.first_name}, Last Name: {self.last_name}, Created At: {self.created_at}, Updated At: {self.updated_at})"

if __name__ == "__main__":

    user = User(email="example@example.com", password="securepassword", first_name="John", last_name="Doe")
    print(user)


    user.login(email="example@example.com", password="securepassword")

    user.save_infos(new_first_name="Jane", new_last_name="Smith")
    print(user)

    user.logout()
