import cmd

from ops import put, get, delete, list_keys
from config import initialize_database


class MiniDBShell(cmd.Cmd):
    intro = "Welcome to the Mini Database shell. Type 'help' or '?' to list commands.\n"
    prompt = "(mini_db) "
    file = None

    def do_put(self, arg):
        """Add a key-value pair to the database. Usage: put <key> <value>"""
        args = arg.split()
        if len(args) == 2:
            put(args[0], args[1])
        else:
            print("Invalid usage. Usage: put <key> <value>")

    def do_get(self, arg):
        """Retrieve the value associated with a given key. Usage: get <key>"""
        args = arg.split()
        if len(args) == 1:
            get(args[0])
        else:
            print("Invalid usage. Usage: get <key>")

    def do_delete(self, arg):
        """Remove a key-value pair from the database. Usage: delete <key>"""
        args = arg.split()
        if len(args) == 1:
            delete(args[0])
        else:
            print("Invalid usage. Usage: delete <key>")

    def do_list_keys(self, arg):
        """List all the keys in the database. Usage: list_keys"""
        list_keys()

    def do_exit(self, arg):
        """Exit the Mini Database shell. Usage: exit"""
        print("Exiting Mini Database shell.")
        return True

    def emptyline(self):
        pass

    def default(self, line):
        print(f"Invalid command: {line}. Type 'help' or '?' to list commands.")

if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Start the interactive shell
    MiniDBShell().cmdloop()
    
# directory structure:

# xyz
# ├── config.py
# ├── xyz.db.py
# ├── mini_db
# │   └── db.json
# ├── ops
# │   ├── __init__.py
# │   ├── get.py
# │   ├── list_keys.py
# │   ├── put.py
# │   └── delete.py
# └── utils
#     ├── __init__.py
#     ├── database.py
#     ├── read.py
#     └── write.py


