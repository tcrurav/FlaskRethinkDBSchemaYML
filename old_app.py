from flask import Flask, request, jsonify
import yaml
from cerberus import Validator

import os
from dotenv import load_dotenv
load_dotenv()

from rethinkdb import RethinkDB
r = RethinkDB()

# Connect to RethinkDB
r.connect('localhost', 28015).repl()

# Ensure the database and table exist
db_name = os.getenv("RETHINKDB_DB")
db_port = os.getenv("RETHINKDB_PORT")
table_name = os.getenv("RETHINKDB_TABLE")

# Create DB and Table if they don't exist
if db_name not in r.db_list().run():
    r.db_create(db_name).run()

if table_name not in r.db(db_name).table_list().run():
    r.db(db_name).table_create(table_name).run()

# Load schema from schema.yml
with open('schemas/bicycles.yml', 'r') as file:
    schema = yaml.safe_load(file)
    bicycle_schema = schema['bicycle_schema']

# Cerberus Validator initialized with the loaded schema
v = Validator(bicycle_schema)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask is working! Lluuujuuuu!!!"

# Get all bicycles
@app.route('/bicycles', methods=['GET'])
def get_bicycles():
    with r.connect(host='localhost', port=28015, db=db_name) as conn:
        bicycles = list(r.table(table_name).run(conn))
        return jsonify(bicycles), 200

# Create a new bicycle
@app.route('/bicycles', methods=['POST'])
def create_bicycle():
    data = request.get_json()

    # Validate using schema
    if not v.validate(data):
        return jsonify({'error': 'Invalid data', 'details': v.errors}), 400

    # Insert data into RethinkDB
    with r.connect(host='localhost', port=28015, db=db_name) as conn:
        result = r.table(table_name).insert(data).run(conn)
        return jsonify({'message': 'Bicycle created', 'bicycle_id': result['generated_keys'][0]}), 201

# Get a specific bicycle by ID
@app.route('/bicycles/<bicycle_id>', methods=['GET'])
def get_bicycle(bicycle_id):
    with r.connect(host='localhost', port=28015, db=db_name) as conn:
        bicycle = r.table(table_name).get(bicycle_id).run(conn)
        if not bicycle:
            return jsonify({'error': 'Bicycle not found'}), 404
        return jsonify(bicycle), 200

# Update a bicycle
@app.route('/bicycles/<bicycle_id>', methods=['PUT'])
def update_bicycle(bicycle_id):
    data = request.get_json()

    # Validate using schema (excluding required for updates)
    if not v.validate(data, update=True):
        return jsonify({'error': 'Invalid data', 'details': v.errors}), 400

    # Update bicycle in RethinkDB
    with r.connect(host='localhost', port=28015, db=db_name) as conn:
        result = r.table(table_name).get(bicycle_id).update(data).run(conn)

        if result['replaced'] == 0:
            return jsonify({'error': 'Bicycle not found'}), 404

        return jsonify({'message': 'Bicycle updated'}), 200

# Delete a bicycle
@app.route('/bicycles/<bicycle_id>', methods=['DELETE'])
def delete_bicycle(bicycle_id):
    with r.connect(host='localhost', port=28015, db=db_name) as conn:
        result = r.table(table_name).get(bicycle_id).delete().run(conn)

        if result['deleted'] == 0:
            return jsonify({'error': 'Bicycle not found'}), 404

        return jsonify({'message': 'Bicycle deleted'}), 200

if __name__ == "__main__":
    app.run(debug=True)