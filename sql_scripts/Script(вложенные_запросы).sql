SELECT mark FROM marks
WHERE id = 2 AND subject LIKE 'Си'

SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > 3 AND subject LIKE 'Си'

SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > 
( SELECT mark FROM marks
WHERE id = 2 AND subject LIKE 'Си' ) 
AND subject LIKE 'Си'

SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > 
( SELECT mark FROM marks
WHERE id = 2 ) 
AND subject LIKE 'Си'

SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > ( SELECT avg(mark) FROM marks
WHERE id = 2 ) 
AND subject LIKE 'Си'



