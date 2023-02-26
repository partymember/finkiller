import pandas as pd
import impexp as ie


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
    exp.export_expense('1', 'name1', 'product1', 'cat12', 2.12)
    print(exp.import_expenses())

    # df = pd.DataFrame(y)
    # # TODO: Drop while loading, maybe load directly from sql?
    # df.drop(columns=df.columns[0], axis=1, inplace=True)
    # df.columns = ['rowid', 'name', 'product', 'price']
    # sum = df['price'].sum()
    # print(df.describe())
    # print(f'Total expense = {sum}')


if __name__ == "__main__":
    main()
