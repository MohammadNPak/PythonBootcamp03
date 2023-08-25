create table if not EXISTS user(
    id integer primary key,
    username text unique,
    password text,
    email text unique,
    picture text
);

create table if not EXISTS book(
    id integer primary key,
    name text,
    author text,
    picture text,
    user_id integer,
    FOREIGN KEY (user_id) REFERENCES user (id)
);