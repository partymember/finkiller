import database as db


def main():
    print("Finkiller starting...")
    print("Creating db handler")
    database = db.Database()
    database.open_db('db.sq3')
    # database.create_tables()
    # database.insert_expense(2, "name1", "product1", "category1", 2.32)
    database.get_expenses()
    database.close_db()
    

if __name__ == "__main__":
    main()
