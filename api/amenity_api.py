#!/usr/bin/python3
from flask import Flask, request, jsonify
from models.amenity import Amenity
from persistence import file_storage


app = Flask(__name__)
storage = file_storage.FileStorage('users.json')

@app.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.json
    amenity = Amenity(name=data['name'], user_id=data['user_id'])
    amenities = storage.load()
    amenities[amenity.amenity_id] = amenity.__dict__
    storage.save(amenities)
    return jsonify(amenity.__dict__), 201

@app.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenities = storage.load()
    amenity = amenities.get(amenity_id)
    if amenity:
        return jsonify(amenity)
    else:
        return jsonify({'error': 'Amenity not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
