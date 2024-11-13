SELECT name, sex, games.score FROM games
JOIN user ON games.user_id = user.rowid

SELECT name, sex, games.score FROM games, user

SELECT name, sex, games.score FROM user, games

SELECT name, sex, games.score FROM games
LEFT JOIN user ON games.user_id = user.rowid

SELECT user.name, SUM(games.score) AS "sum" FROM games
LEFT JOIN user ON games.user_id = user.rowid
GROUP BY games.user_id
ORDER BY sum DESC

