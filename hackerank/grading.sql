/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
-- 1 Liam 40 C
-- 2 Noah 41 C
-- 3 William 47 C
-- 4 James 53 B
-- 5 Oliver 99 A+
-- 6 Benjamin 15 Fail
-- 7 Elijah 100 A+
-- 8 Lucas 100 A+
-- 9 Mason 51 B
-- 10 Logan 95 A+
-- 11 Alexander 12 Fail
-- 12 Ethan 100 A+

SELECT *,
CASE WHEN marks > 90 THEN 'A+'
WHEN marks > 70 THEN 'A'
WHEN marks > 50 THEN 'B'
WHEN marks >= 40 THEN 'C'
ELSE 'Fail'
END AS grade
FROM students;