import database as db


def main():
    print("Finkiller starting...")
    print("Creating db handler")
    database = db.Database()
    database.open_db('db.sq3')
    database.close_db()
    

if __name__ == "__main__":
    main()
