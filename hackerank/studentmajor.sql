-- A university maintains data on students and their majors in three tables: STUDENTS, MAJORS, and REGISTER. The university needs a list of the STUDENT_NAME and MAJOR_NAME of, at most, the first 20 students. Write a query to print that list.

-- John Microbiology
-- Harry Computer Science
-- Matthew History
-- Geoffrey Computer Science
-- Jeniffer Geography
-- Johni Microbiology
-- Harryi Computer Science
-- Matthewi Geography
-- Geoffreyi Computer Science
-- Jenifferi Geography
-- Johno Microbiology
-- Harryo Computer Science
-- Matthewo Geography
-- Geoffreyo Computer Science
-- Jeniffero Microbiology
-- Johnq Microbiology
-- Harryq Computer Science
-- Matthewq Physical Education
-- Geoffreyq Computer Science
-- Jenifferq Microbiology

SELECT s.STUDENT_NAME, m.MAJOR_NAME
FROM STUDENTS AS s
INNER JOIN REGISTER AS r
ON s.STUDENT_ID = r.STUDENT_ID 
INNER JOIN MAJORS AS m
ON r.MAJOR_ID = m.MAJOR_ID 
LIMIT 20;
