/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

SELECT *,
CASE WHEN marks > 90 THEN 'A+'
WHEN marks > 70 THEN 'A'
WHEN marks > 50 THEN 'B'
WHEN marks >= 40 THEN 'C'
ELSE 'Fail'
END AS grade
FROM students;