# app/controllers/bicycles_controller.py
from rethinkdb import RethinkDB
from flask import current_app
import yaml
from cerberus import Validator

r = RethinkDB()

RETHINKDB_HOST = current_app.config["RETHINKDB_HOST"]
RETHINKDB_PORT = current_app.config["RETHINKDB_PORT"]
RETHINKDB_DB   = current_app.config["RETHINKDB_DB"]

# Load schema from app/schemas/bicycle_schema.yml
with open('app/schemas/bicycle_schema.yml', 'r') as file:
    schema = yaml.safe_load(file)
    bicycle_schema = schema['bicycle_schema']

# Cerberus Validator initialized with the loaded schema
v = Validator(bicycle_schema)

def create_bicycle(data):
    """ Insert a new bicycle into the 'bicycles' table """
    # Validate using schema
    if not v.validate(data):
        return jsonify({'error': 'Invalid data', 'details': v.errors}), 400
    
    with r.connect(host=RETHINKDB_HOST, port=RETHINKDB_PORT, db=RETHINKDB_DB) as conn:
        return r.table('bicycles').insert(data).run(conn)

def get_bicycles():
    """ Retrieve all bicycles from the 'bicycles' table """
    with r.connect(host=RETHINKDB_HOST, port=RETHINKDB_PORT, db=RETHINKDB_DB) as conn:
        return list(r.table('bicycles').run(conn))

def get_bicycle(bicycle_id):
    """ Retrieve a single bicycle by ID """
    with r.connect(host=RETHINKDB_HOST, port=RETHINKDB_PORT, db=RETHINKDB_DB) as conn:
        return r.table('bicycles').get(bicycle_id).run(conn)

def update_bicycle(bicycle_id, data):
    """ Update a bicycle by ID """
    # Validate using schema
    if not v.validate(data):
        return jsonify({'error': 'Invalid data', 'details': v.errors}), 400
    
    with r.connect(host=RETHINKDB_HOST, port=RETHINKDB_PORT, db=RETHINKDB_DB) as conn:
        return r.table('bicycles').get(bicycle_id).update(data).run(conn)

def delete_bicycle(bicycle_id):
    """ Delete a bicycle by ID """
    with r.connect(host=RETHINKDB_HOST, port=RETHINKDB_PORT, db=RETHINKDB_DB) as conn:
        return r.table('bicycles').get(bicycle_id).delete().run(conn)