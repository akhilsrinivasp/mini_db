from utils import read_database

def list_keys():
    database = read_database()
    print("Keys in the database:")
    for key in database.keys():
        print(key)