#!/usr/bin/python3
from flask import Flask, request, jsonify
from models.review import Review
from persistence import file_storage
from datetime import datetime

app = Flask(__name__)
storage = file_storage.FileStorage('reviews.json')

def load_data():
    return storage.load()

def save_data(data):
    storage.save(data)

def validate_review_data(data):
    required_fields = ['user_id', 'rating', 'comment']
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
    if not isinstance(data['rating'], int) or not (1 <= data['rating'] <= 5):
        return False, "Invalid rating value. It should be an integer between 1 and 5."
    return True, ""

@app.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.json
    is_valid, message = validate_review_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    review = Review(place_id=place_id, **data)
    reviews = load_data()
    reviews[review.review_id] = review.to_dict()
    save_data(reviews)
    return jsonify(review.to_dict()), 201

@app.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    reviews = load_data()
    user_reviews = [review for review in reviews.values() if review['user_id'] == user_id]
    return jsonify(user_reviews), 200

@app.route('/places/<place_id>/reviews', methods=['GET'])
def get_place_reviews(place_id):
    reviews = load_data()
    place_reviews = [review for review in reviews.values() if review['place_id'] == place_id]
    return jsonify(place_reviews), 200

@app.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    reviews = load_data()
    review = reviews.get(review_id)
    if review:
        return jsonify(review), 200
    else:
        return jsonify({'error': 'Review not found'}), 404

@app.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    is_valid, message = validate_review_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    reviews = load_data()
    review = reviews.get(review_id)
    if review:
        review.update(data)
        review['updated_at'] = datetime.now()
        save_data(reviews)
        return jsonify(review), 200
    else:
        return jsonify({'error': 'Review not found'}), 404

@app.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    reviews = load_data()
    if review_id in reviews:
        del reviews[review_id]
        save_data(reviews)
        return '', 204
    else:
        return jsonify({'error': 'Review not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
