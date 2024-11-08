# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS cars(
#                         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         model TEXT,
#                         price INTEGER
#     )""")
#
#     cur.execute("INSERT INTO cars VALUES(1, 'Audi', '52642')")
#     cur.execute("INSERT INTO cars VALUES(2, 'Mercedes', '57127')")
#     cur.execute("INSERT INTO cars VALUES(3, 'Skoda', '9000')")
#     cur.execute("INSERT INTO cars VALUES(4, 'Volvo', '29000')")
#     cur.execute("INSERT INTO cars VALUES(5, 'Bentley', '350000')")

# import sqlite3 as sq
#
# cars = [
#     ('Audi', 52642),
#     ('Mercedes', 57127),
#     ('Skoda', 9000),
#     ('Volvo', 29000),
#     ('Bentley', 350000),
# ]
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS cars(
#                     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     model TEXT,
#                     price INTEGER
#     )""")
#
#     # for car in cars:
#     #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
#     # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
#     # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price': 0})
#     cur.executescript("""DELETE FROM cars WHERE model LIKE 'A%';
#                          UPDATE cars SET price = price + 1000
#                       """)

# import sqlite3 as sq
#
#
# con = None
# try:
#
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#
#     cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
#                          car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                          model TEXT,
#                          price INTEGER
#                );
#                BEGIN;
#                INSERT INTO cars VALUES(NULL, 'Audi', '52642');
#                INSERT INTO cars VALUES(NULL, 'Mercedes', '57127');
#                INSERT INTO cars VALUES(NULL, 'Skoda', '9000');
#                INSERT INTO cars VALUES(NULL, 'Volvo', '29000');
#                INSERT INTO cars VALUES(NULL, 'Bentley', '350000');
#                UPDATE cars SET price = price + 1000
#                """)
#
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#         print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()

import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars(
                    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    model TEXT,
                    price INTEGER
                );

                CREATE TABLE IF NOT EXISTS cust (
                name TEXT,
                tr_in INTEGER,
                buy INTEGER
                );
    """)

    cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
    last_row_id = cur.lastrowid
    buy_car_id = 2
    cur.execute("INSERT INTO cust VALUES('Федор', ?, ?)", (last_row_id, buy_car_id))



