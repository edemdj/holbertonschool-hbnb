#!/usr/bin/python3
from persistence.file_storage import FileStorage
from persistence.data_manager import DataManager
from flask import Flask, request, jsonify
from models.user import User

app = Flask(__name__)

file_storage = FileStorage()
data_manager = DataManager(file_storage)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    data_manager.save(user)
    return jsonify(user.to_dict()), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id, User)
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
