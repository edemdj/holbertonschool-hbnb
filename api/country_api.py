#!/usr/bin/python3
from flask import Flask, jsonify
from models.country import Country

app = Flask(__name__)

countries = [
    Country(name="France"),
    Country(name="Germany"),
    Country(name="United States")
]

@app.route('/countries', methods=['GET'])
def get_countries():
    return jsonify([country.to_dict() for country in countries]), 200

@app.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    country = next((c for c in countries if c.id == country_code), None)
    if country:
        return jsonify(country.to_dict()), 200
    else:
        return jsonify({'error': 'Country not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
