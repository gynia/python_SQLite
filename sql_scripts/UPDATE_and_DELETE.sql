UPDATE user SET score = 0

UPDATE user SET score = 1000 WHERE rowid = 1

UPDATE user SET score = score + 500 WHERE sex = 2

UPDATE user SET score = score + 500 WHERE name LIKE "Федор"

UPDATE user SET score = 600 WHERE name LIKE "М%"

UPDATE user SET score = 700 WHERE name LIKE "С_рг%"

DELETE FROM user WHERE rowid IN (1, 17)







