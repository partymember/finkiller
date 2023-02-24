import database as db
import pandas as pd


#TODO: Maybe dictionary instead of class
class Expense:
    def __init__ (self):
        _name = ''
        _product = ''
        _category = ''
        _price = ''

    def set_expense(self, x):
        self._name = x[0],
        self._product = x[0]

    def get_expense(self):
        return {'name': self._name, 'product': self._product}


def main():
    print("Finkiller starting...")
    print("Creating db handler")
    database = db.Database()
    database.open_db('db.sq3')
    database.create_tables()
    database.insert_expense("name1", "product1", "category1", 2.32)
    y = database.get_expenses()
    df = pd.DataFrame(y)
    # TODO: Drop while loading, maybe load directly from sql?
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    df.columns = ['rowid', 'name', 'product', 'price']
    sum = df['price'].sum()
    print(df.describe())
    print(f'Total expense = {sum}')
    database.close_db()

    # exp = Expense()
    # exp.set_expense(['raz', 'jeden'])
    # print(exp.get_expense())
    

if __name__ == "__main__":
    main()
