import sqlite3
import datetime

db = sqlite3.connect('db.db')
c = db.cursor()


def insert_partname(partnumber: str, partname: str, manufacturer: str) -> None:
    """Добавление нового номера компонента"""
    c.execute(
        'INSERT INTO part_names'
        '(number, name, manufacturer)'
        'VALUES (?, ?, ?)',
        (partnumber, partname, manufacturer))
    db.commit()


def insert_request(partnumber: str, price: int, source: str) -> None:
    """Добавление нового запроса"""
    date = datetime.datetime.now()
    c.execute(
        'INSERT INTO requests '
        '(created, price, source, partnumber) '
        'VALUES (?, ?, ?, ?)',
        (date, price, source, partnumber))
    db.commit()


def availability(partnumber: str):
    """Проверка на наличие номера в part_names"""
    x = c.execute(
        "SELECT number "
        "FROM part_names "
        "WHERE number = ?",
        (partnumber,)).fetchall()
    return bool(x)


def get_partname(partnumber: str) -> list:
    """Получение название(name) и производителя(manufacturer) запчасти, которая уже есть в базе"""
    x = c.execute(
        "SELECT name, manufacturer "
        "FROM part_names "
        "WHERE number = ?",
        (partnumber,)).fetchall()
    return x[0]
