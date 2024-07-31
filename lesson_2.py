import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    # cur.execute("DROP TABLE IF EXISTS user")
    cur.execute("""CREATE TABLE IF NOT EXISTS  user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")

# con = sq.connect("saper.db")
# cur = con.cursor()
# cur.execute("""
# """)
# con.close()


