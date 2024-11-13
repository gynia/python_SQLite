SELECT score, `from` AS val_score FROM tab1
UNION SELECT val, type FROM tab2

SELECT score, "from" AS val_score FROM tab1
UNION SELECT val, type FROM tab2

SELECT score AS val_score FROM tab1
UNION SELECT val FROM tab2

SELECT score, 'tabel 1' AS tb1 FROM tab1
UNION SELECT val, 'tabel 2' FROM tab2

SELECT score AS s, 'tabel 1' AS tb1 FROM tab1
UNION SELECT val AS s, 'tabel 2' FROM tab2
ORDER BY s DESC

SELECT score AS s, 'tabel 1' AS tb1 FROM tab1 
WHERE s IN (300, 400)
UNION SELECT val AS s, 'tabel 2' FROM tab2
ORDER BY s DESC

SELECT score AS s, 'tabel 1' AS tb1 FROM tab1 
WHERE s IN (300, 400)
UNION SELECT val AS s, 'tabel 2' FROM tab2 
WHERE s IN (300, 400)
ORDER BY s DESC


