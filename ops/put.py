from utils import read_database, write_database

"""
This module contains the put function.
"""

def put(key, value):
    database = read_database()
    database[key] = value
    write_database(database)
    print(f"Key '{key}' with value '{value}' added to the database.")