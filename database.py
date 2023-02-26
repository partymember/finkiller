import sqlite3


class Database:
    def __init__ (self):
        self._name = 'DB'
        self._connection = None

    def __str__(self):
        return self._name

    def _parse_type(self, x):
        if x == str:
            return "TEXT"
        if x == float:
            return "REAL"

    def open_db(self, path):
        self._connection = sqlite3.connect(path)

    def create_tables(self, name, cols):
        cmd = f'CREATE TABLE {name}('
        for key in cols:
            cmd = cmd + f'{key} {self._parse_type(cols[key])},\n'

        cmd = cmd[:-2] + ');'
        try:
            self._connection.execute(cmd)
        except:
            print('Exception: table already exists')

    def insert(self, cols, table, data):
        cmd = f'INSERT INTO {table}('
        for key in cols:
            cmd = cmd + f'{key}, '
        txt = '?,'*len(cols)
        cmd = cmd[:-2] + f') VALUES ({txt}'
        cmd = cmd[:-1]+ ');'

        try:
            self._connection.execute(cmd, data)
            self._connection.commit()
        # TODO: catch errors
        except:
            print('Insert error')



        # self._connection.execute(f"INSERT INTO EXPENSES (NAME,PRODUCT,CATEGORY,PRICE) \
        #     VALUES (?,?,?,?)", (name, product, category, price))
        # self._connection.commit()
        print("inserted")

    # TODO: Add data range, limit
    def query(self, table):
        cmd = f'SELECT rowid, * from {table};'
        cursor = self._connection.execute(cmd)
        x = []
        for row in cursor:
            x.append(row)
        return x

    def close_db(self):
        self._connection.close()

    # def get_from_database(self):
    #     pass
    #
    # def save_to_database(self, item):
    #     pass