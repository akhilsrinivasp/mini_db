from utils import read_database

def get(key):
    database = read_database()
    value = database.get(key)
    if value is not None:
        print(f"Value for key '{key}': {value}")
    else:
        print(f"Key '{key}' not found in the database.")