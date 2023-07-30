import json 
from config import DATABASE_FILE

def write_database(database):
    with open(DATABASE_FILE, "w") as f:
        json.dump(database, f)