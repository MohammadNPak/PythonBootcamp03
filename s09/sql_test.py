import sqlite3



def create_db(address):
    connection = sqlite3.connect(address)
    cursor = connection.cursor()
    cursor.execute("create table user(id integer primary key,username text,password text,picture text);")
    connection.close()


def create_user(address,user:dict):
    connection = sqlite3.connect(address)
    cursor = connection.cursor()
    cursor.execute(f"""
        insert into
            user (username, password, picture)
            values
                (
                    '{user['username']}',
                    '{user['password']}',
                    '{user['picture']}'
                );
                   """)
    connection.commit()
    connection.close()

create_db("user.sqlite3")

u = {
    "username":"mohammad",
    "password":"123",
    "picture":"data/mohammad_picture.jpg"
}
create_user("user.sqlite3",u)

