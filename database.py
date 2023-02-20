import sqlite3


class Database:
    def __init__ (self):
        self._name = 'DB'
        self._connection = None
        print("Creating database handle")

    def __str__(self):
        return self._name

    def open_db(self, path):
        self._connection = sqlite3.connect(path)
        print("Connected to database")

    def close_db(self):
        self._connection.close()
        print("Database disconnected")

    def get_from_database(self):
        pass

    def save_to_database(self, item):
        pass