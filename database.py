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

    def create_tables(self):
        #TODO: if table exists?
        try:
            self._connection.execute(
            '''CREATE TABLE EXPENSES
            (NAME           TEXT    NOT NULL,
            PRODUCT        TEXT     NOT NULL,
            CATEGORY       TEXT,
            PRICE         REAL);''')
        except:
            print('database already created')

    def insert_expense(self, name, product,category, price):
        #TODO: try catch if ID already exists
         self._connection.execute(f"INSERT INTO EXPENSES (NAME,PRODUCT,CATEGORY,PRICE) \
            VALUES (?,?,?,?)", (name, product, category, price))
         self._connection.commit()
         print("inserted")

    def get_expenses(self):
        cursor = self._connection.execute("SELECT rowid, * from EXPENSES")
        x = []
        for row in cursor:
            x.append(row)
        return x

    def close_db(self):
        self._connection.close()
        print("Database disconnected")

    def get_from_database(self):
        pass

    def save_to_database(self, item):
        pass