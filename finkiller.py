import pandas as pd
import impexp as ie
import datetime
import random


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

    exp = ie.Exporter("adam")
    for x in range(10):
        y = random.randint(-10, 10)
        diff = datetime.timedelta(days=1)*y
        date = datetime.date.today()
        date = date + diff
        exp.export_expense(date, 'name1', 'product1', f'cat{x}', 2.12)

    date1 = datetime.date(year=2023, month=2, day=26)
    date2 = datetime.date(year=2023, month=2, day=28)
    data_to_analyze = (exp.import_expenses(date2, date2))

    df = pd.DataFrame(data_to_analyze)
    # TODO: Drop while loading, maybe load directly from sql?
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    df.columns = ['date', 'name', 'product', 'cat', 'price']
    total_price = df['price'].sum()
    print(df.describe())
    print(f'Total expense = {total_price}')


if __name__ == "__main__":
    main()
