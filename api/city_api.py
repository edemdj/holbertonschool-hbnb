#!/usr/bin/python3
from datetime import datetime
from flask import Flask, jsonify, request
from models.city import City
from models.country import Country

app = Flask(__name__)

# Simuler des données de pays préchargées
countries = [
    Country("France", "FR"),
    Country("Germany", "DE"),
    Country("United States", "US")
]

cities = []

# Endpoint pour créer une nouvelle ville
@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    name = data.get('name')
    country_code = data.get('country_code')

    # Vérifier si le code pays est valide
    if not any(c.code == country_code for c in countries):
        return jsonify({'error': 'Invalid country code'}), 400

    # Vérifier si le nom de la ville est unique dans le pays
    if any(city.name == name and city.country_code == country_code for city in cities):
        return jsonify({'error': 'City name must be unique within the country'}), 409

    city = City(name, country_code)
    cities.append(city)
    return jsonify(city.to_dict()), 201

# Endpoint pour récupérer toutes les villes
@app.route('/cities', methods=['GET'])
def get_cities():
    return jsonify([city.to_dict() for city in cities]), 200

# Endpoint pour récupérer une ville par son ID
@app.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    city = next((c for c in cities if c.id == city_id), None)
    if city:
        return jsonify(city.to_dict()), 200
    else:
        return jsonify({'error': 'City not found'}), 404

# Endpoint pour mettre à jour une ville existante par son ID
@app.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    city = next((c for c in cities if c.id == city_id), None)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    data = request.get_json()
    city_name = data.get('name')
    country_code = data.get('country_code')

    # Vérifier si le code pays est valide
    if not any(c.code == country_code for c in countries):
        return jsonify({'error': 'Invalid country code'}), 400

    # Vérifier si le nom de la ville est unique dans le pays
    if any(c.name == city_name and c.country_code == country_code and c.id != city_id for c in cities):
        return jsonify({'error': 'City name must be unique within the country'}), 409

    city.name = city_name
    city.country_code = country_code
    city.updated_at = datetime.now()
    return jsonify(city.to_dict()), 200

# Endpoint pour supprimer une ville par son ID
@app.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    global cities
    cities = [c for c in cities if c.id != city_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
