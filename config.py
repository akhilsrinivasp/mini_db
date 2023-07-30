import os, json

DATABASE_FILE = "mini_db/db.json"

def initialize_database():
    if not os.path.isfile(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as f:
            json.dump({}, f)
