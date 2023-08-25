import sqlite3


def create_db():
    schema_address = 's11/schema.sql'
    db_address = 's11/db.sqlite3'
    with open(schema_address,'r') as fp:
        query = fp.read()
        connection = sqlite3.connect(db_address)
        cursor = connection.cursor()
        cursor.executescript(query)
        connection.commit()
        connection.close()

create_db()