import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE user (
    name TEXT,
    sex INTEGER,
    old INTEGER,
    score INTEGER
    )""")

# con = sq.connect("saper.db")
# cur = con.cursor()
# cur.execute("""
# """)
# con.close()


