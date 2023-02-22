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
        self._connection.execute(
        '''CREATE TABLE EXPENSES
        (ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        PRODUCT        TEXT     NOT NULL,
        CATEGORY       TEXT,
        PRICE         REAL);''')

    def insert_expense(self, key_id, name, product,category, price):
        #TODO: try catch if ID already exists
         self._connection.execute(f"INSERT INTO EXPENSES (ID,NAME,PRODUCT,CATEGORY,PRICE) \
            VALUES (?,?,?,?,?)", (key_id, name, product, category, price))
         self._connection.commit()
         print("inserted")

    def get_expenses(self):
        cursor = self._connection.execute("SELECT * from EXPENSES")
        print("Got:")
        for row in cursor:
            print (f"ID =  {row[0]}")
            print(f"NAME =  {row[1]}")
            print(f"PRODUCT =  {row[2]}")
            print(f"CATEGORY =  {row[3]}")
            print(f"PRICE =  {row[4]}")

    def close_db(self):
        self._connection.close()
        print("Database disconnected")

    def get_from_database(self):
        pass

    def save_to_database(self, item):
        pass