# Mini Database Shell
This is a simple command-line interface (CLI) based mini database project built using Python. The project aims to provide a basic key-value store database with CRUD (Create, Read, Update, Delete) operations. The database stores data in a structured JSON format, making it easy to manage and query.

## Features
- Add key-value pairs to the database
- Retrieve values associated with given keys
- Remove key-value pairs from the database
- List all keys in the database
- Interactive shell environment for easy database interaction

The **Project Directory** structure is organized as follows:
```
xyz
├── config.py
├── mini_db
│   └── db.json
├── ops
│   ├── __init__.py
│   ├── get.py
│   ├── list_keys.py
│   ├── put.py
│   └── delete.py
└── utils
    ├── __init__.py
    ├── database.py
    ├── read.py
    └── write.py
```

`xyz.db.py`: The main Python script that provides the interactive shell for the mini database.
`config.py`: Configuration file (if applicable).
`mini_db`: Directory to store the JSON database file (db.json).
`ops\`: Directory containing modules for different database operations (put.py, get.py, delete.py, and list_keys.py).
`utils\`: Directory containing utility modules for database operations (database.py, read.py, and write.py).

## Getting Started
To run the mini database shell, follow these steps:

- Clone the repository to your local machine:
```
git clone https://github.com/akhilsrinivasp/mini_db.git
cd mini_db
```
Make sure you have Python 3.x installed on your system.

Run the database shell:
```
python xyz.db.py
```
You will be presented with the (mini_db) prompt, and you can start using the available commands to interact with the database.

## Usage
The mini database shell provides the following commands:

- put <key> <value>: Add a key-value pair to the database.
- get <key>: Retrieve the value associated with a given key.
- delete <key>: Remove a key-value pair from the database.
- list_keys: List all the keys in the database.
- exit: Exit the Mini Database shell.

### Examples

Add a key-value pair to the database:
```
(mini_db) put name John
Key 'name' with value 'John' added to the database.
```

Retrieve the value associated with a key:
```
(mini_db) get name
Value for key 'name': John
```

Remove a key-value pair from the database:
```
(mini_db) delete name
Key 'name' removed from the database.
```

List all keys in the database:
```
(mini_db) list_keys
Keys in the database:
name
```

Exit the database shell:
```
(mini_db) exit
Exiting Mini Database shell.
```

## Contribution
Contributions to the project are welcome! If you find any bugs, have feature suggestions, or want to improve the code, feel free to open an issue or submit a pull request.

### License
This project is licensed under the Apache License. Feel free to use, modify, and distribute the code according to the terms of the license.
