from utils import read_database, write_database

def delete(key):
    database = read_database()
    if key in database:
        del database[key]
        write_database(database)
        print(f"Key '{key}' removed from the database.")
    else:
        print(f"Key '{key}' not found in the database.")