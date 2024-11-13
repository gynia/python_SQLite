SELECT user_id FROM games WHERE user_id = 1

SELECT count(user_id) FROM games WHERE user_id = 1

SELECT count(user_id) AS count FROM games WHERE user_id = 1

SELECT DISTINCT user_id AS "gamers" FROM games

SELECT count(DISTINCT user_id) AS count FROM games

SELECT SUM(score) AS "sum" FROM games WHERE user_id = 1

SELECT user_id, SUM(score) AS "scores" FROM games
GROUP BY user_id

SELECT user_id, SUM(score) AS "scores" FROM games
GROUP BY user_id
ORDER BY scores DESC 


