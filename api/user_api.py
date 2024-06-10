#!/usr/bin/python3
from flask import Flask, request, jsonify
from models.user import User
from persistence.data_manager import DataManager
from persistence.file_storage import FileStorage


app = Flask(__name__)
data_manager = DataManager()
storage = FileStorage()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    data_manager.save(user)
    return jsonify(user.to_dict()), 201


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    users = storage.load()
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
