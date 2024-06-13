#!/usr/bin/python3
from flask import Flask, request, abort, jsonify
from models.user import User
from persistence.file_storage import FileStorage
from persistence.data_manager import DataManager

app = Flask(__name__)
file_storage = FileStorage()
data_manager = DataManager(file_storage)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'email' not in data or 'first_name' not in data or 'last_name' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    if not is_valid_email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400
    
    if 'emeil' (data['email']):
        return jsonify({'error': 'Email already exists'}), 409


    user = User(**data)
    data_manager.save(user)
    return jsonify(user.to_dict()), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id, User)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = data_manager.get(user_id, User)
    if user:
        data_manager.delete(user_id, User)
        return '', 204
    else:
        abort(404)

def is_valid_email(email):

    return True

if __name__ == '__main__':
    app.run(debug=True)
