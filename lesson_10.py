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
#     # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
#     cur.execute("SELECT model, price FROM cars")
#
#     # rows = cur.fetchall()
#     # print(rows)
#
#     # rows = cur.fetchone()
#     # print(rows)
#
#     # rows = cur.fetchmany(4)
#     # print(rows)
#
#     for result in cur:
#         print(result)


# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#
#     cur.execute("SELECT model, price FROM cars")
#
#     for result in cur:
#         print(result['model'], result['price'])
#         # print(result)


# import sqlite3 as sq
#
#
# def read_ava(n):
#     try:
#         with open(f"avas/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     finally:
#         f.close()
#         return True
#
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#                     name TEXT,
#                     ava BLOB,
#                     score INTEGER)
#     """)
#     cur.execute("SELECT ava FROM users LIMIT 1")
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sq.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Николай', ?, 1000)", (binary,))
#
#     img = cur.fetchone()['ava']
#     write_ava("out.png", img)


# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     for sql in con.iterdump():
#         print(sql)


import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()
    with open("sql_damp.sql", "w") as f:
        for sql in con.iterdump():
            f.write(sql)
