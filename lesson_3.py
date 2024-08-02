import sqlite3 as sq

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM user WHERE score > 100 ORDER BY score DESC LIMIT 5")
#     result = cur.fetchall()
#     print(result)

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM user WHERE score > 100 ORDER BY score DESC LIMIT 5")
#     for result in cur:
#         print(result)

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM user WHERE score > 100 ORDER BY score DESC LIMIT 5")
    result = cur.fetchone()
    result2 = cur.fetchmany(2)
    print(result)
    print(result2)

