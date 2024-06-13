#!/usr/bin/python3
from datetime import datetime
from flask import Flask, request, jsonify
from models.review import Review
from persistence.file_storage import FileStorage
from models.user import User
from models.place import Place

app = Flask(__name__)
storage = FileStorage('reviews.json')

def validate_review_data(data):
    if 'user_id' not in data or 'rating' not in data:
        return 'user_id and rating are required fields.', 400
    if not (1 <= data['rating'] <= 5):
        return 'Rating must be between 1 and 5.', 400
    return None

@app.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.json
    error = validate_review_data(data)
    if error:
        return jsonify({'error': error}), 400

    review = Review(place_id, data['user_id'], data['rating'], data.get('comment', ''))
    reviews = storage.load()
    reviews[review.id] = review.to_dict()
    storage.save(reviews)
    return jsonify(review.to_dict()), 201

@app.route('/users/<user_id>/reviews', methods=['GET'])
def get_reviews_by_user(user_id):
    reviews = storage.load()
    user_reviews = [review for review in reviews.values() if review['user_id'] == user_id]
    return jsonify(user_reviews), 200

@app.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews_by_place(place_id):
    reviews = storage.load()
    place_reviews = [review for review in reviews.values() if review['place_id'] == place_id]
    return jsonify(place_reviews), 200

@app.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    reviews = storage.load()
    review = reviews.get(review_id)
    if review:
        return jsonify(review), 200
    else:
        return jsonify({'error': 'Review not found'}), 404

@app.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    error = validate_review_data(data)
    if error:
        return jsonify({'error': error}), 400

    reviews = storage.load()
    review = reviews.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    review['rating'] = data['rating']
    review['comment'] = data.get('comment', review['comment'])
    review['updated_at'] = datetime.now().isoformat()
    storage.save(reviews)
    return jsonify(review), 200

@app.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    reviews = storage.load()
    if review_id in reviews:
        del reviews[review_id]
        storage.save(reviews)
        return '', 204
    else:
        return jsonify({'error': 'Review not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
