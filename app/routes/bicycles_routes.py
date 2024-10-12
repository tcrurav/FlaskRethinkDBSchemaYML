# app/routes/bicycles_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.bicycles_controller import create_bicycle, get_bicycles, get_bicycle, update_bicycle, delete_bicycle

main = Blueprint('main', __name__)

@main.route('/bicycles', methods=['GET'])
def list_bicycles():
    bicycles = get_bicycles()
    return jsonify(bicycles), 200

@main.route('/bicycles/<string:bicycle_id>', methods=['GET'])
def get_single_bicycle(bicycle_id):
    bicycle = get_bicycle(bicycle_id)
    if bicycle:
        return jsonify(bicycle), 200
    return jsonify({"error": "Bicycle not found"}), 404

@main.route('/bicycles', methods=['POST'])
def create_new_bicycle():
    data = request.json
    create_bicycle(data)
    return jsonify({"message": "Bicycle created"}), 201

@main.route('/bicycles/<string:bicycle_id>', methods=['PUT'])
def update_existing_bicycle(bicycle_id):
    data = request.json
    update_bicycle(bicycle_id, data)
    return jsonify({"message": "Bicycle updated"}), 200

@main.route('/bicycles/<string:bicycle_id>', methods=['DELETE'])
def delete_existing_bicycle(bicycle_id):
    delete_bicycle(bicycle_id)
    return jsonify({"message": "Bicycle deleted"}), 200