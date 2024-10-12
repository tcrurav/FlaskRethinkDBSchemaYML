# app/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    RETHINKDB_HOST = os.getenv("RETHINKDB_HOST", "localhost")
    RETHINKDB_PORT = os.getenv("RETHINKDB_PORT", 28015)
    RETHINKDB_DB = os.getenv("RETHINKDB_DB", "db_bicycles")