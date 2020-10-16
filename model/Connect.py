import sqlite3
import os


def connect():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    database = os.path.join(BASE_DIR, '../sqlite.db')

    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    # cursor.execute("INSERT INTO test(name, pwd) VALUES('Bilal Ahmed', '123456')")
    cursor.execute("SELECT * FROM test")
    connection.commit()
    print(cursor.fetchall())
