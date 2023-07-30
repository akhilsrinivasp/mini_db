import json
from config import DATABASE_FILE

def read_database():
    with open(DATABASE_FILE, "r") as f:
        return json.load(f)