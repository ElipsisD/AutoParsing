import sqlite3

db = sqlite3.connect('db.db')

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS part_names (
    number varchar(255) primary key,
    name varchar(255),
    manufacturer varchar(255)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS requests (
    id integer primary key autoincrement,
    created datetime,
    price integer,
    source varchar(255),
    partnumber varchar(255),
    FOREIGN KEY(partnumber) REFERENCES part_names(number)
)""")

db.commit()

c.close()
db.close()
