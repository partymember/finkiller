import datetime

import database

INCOMES_TABLE = 'INCOMES'
EXPENSES_TABLE = 'EXPENSES'

incomes_columns = {'date': datetime.date, 'name': str, 'source': str, 'category': str, 'quote': float}
expenses_columns = {'date': datetime.date, 'name': str, 'product': str, 'category': str, 'quote': float}


class Exporter:
    def __init__(self, user):
        self._username = user
        self._db_handle = None
        self._db_connect()

    def __del__(self):
        self._db_disconnect()

    def _db_connect(self):
        self._db_handle = database.Database()
        self._db_handle.open_db(self._username + '.sq3')
        self._db_handle.create_tables(name=INCOMES_TABLE, cols=incomes_columns)
        self._db_handle.create_tables(name=EXPENSES_TABLE, cols=expenses_columns)
        print('Database_connected')

    def _db_disconnect(self):
        self._db_handle.close_db()
        print('Database_disconnected')

    # TODO: Get object instead of values, fix names, make independent of input
    def export_expense(self, date, name, pr, cat, qu):
        data = (date, name, pr, cat, qu)
        self._db_handle.insert(incomes_columns, INCOMES_TABLE, data)

    def import_expenses(self, from_date, to_date):
        assert from_date <= to_date
        x = self._db_handle.query(INCOMES_TABLE, from_date, to_date)
        return x
