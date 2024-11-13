INSERT INTO user VALUES (2, 'Михаил', 1, 19, 1000)
INSERT INTO user (name, old, score) VALUES ('Сергей', 20, 1000)
INSERT INTO user (name, old, score) VALUES ('Федор', 32, 200)

-- Это можно блоком выполнить
INSERT INTO user (name, sex, old, score) VALUES ('masha', 2, 25, 200);
INSERT INTO user (name, sex, old, score) VALUES ('Olia', 2, 30, 200);
INSERT INTO user (name, sex, old, score) VALUES ('Ksuxa', 2, 22, 200);
--

SELECT name, old, score FROM user

SELECT * FROM user
SELECT * FROM user WHERE score >= 1000
SELECT * FROM user WHERE score BETWEEN 500 AND 1000
SELECT * FROM user WHERE score < 1000 AND old > 20

SELECT * FROM user WHERE score < 1000 AND old > 20

SELECT * FROM user 
WHERE old IN (19, 32) AND score <= 1000 OR sex = 1
ORDER BY old

SELECT * FROM user 
WHERE old IN (19, 32) AND score <= 1000 OR sex = 1
ORDER BY old DESC 

SELECT * FROM user 
WHERE old IN (19, 32) AND score <= 1000 OR sex = 1
ORDER BY old ASC 

SELECT * FROM user 
WHERE old IN (19, 32) AND score <= 1000 OR sex = 1
ORDER BY old ASC
LIMIT 3

SELECT * FROM user 
WHERE score > 100 
ORDER BY score DESC 
LIMIT 2, 5




