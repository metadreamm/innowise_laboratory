-- @block
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS grades;

-- @block
-- 1. Create tables
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  full_name TEXT,
  birth_year INTEGER
);

-- @block
CREATE TABLE grades (
  student_id INTEGER,
  subject TEXT,
  grade INTEGER,
  FOREIGN KEY (student_ID) REFERENCES students(id)
);

-- @block
-- 2. Insert data
INSERT INTO students (id, full_name, birth_year) VALUES (1, 'Alice Johnson', 2005);
INSERT INTO students (id, full_name, birth_year) VALUES (2, 'Brian Smith', 2004);
INSERT INTO students (id, full_name, birth_year) VALUES (3, 'Carla Reyes', 2006);
INSERT INTO students (id, full_name, birth_year) VALUES (4, 'Daniel Kim', 2005);
INSERT INTO students (id, full_name, birth_year) VALUES (5, 'Eva Thompson', 2003);
INSERT INTO students (id, full_name, birth_year) VALUES (6, 'Felix Nguyen', 2007);
INSERT INTO students (id, full_name, birth_year) VALUES (7, 'Grace Patel', 2005);
INSERT INTO students (id, full_name, birth_year) VALUES (8, 'Henry Lopez', 2004);
INSERT INTO students (id, full_name, birth_year) VALUES (9, 'Isabella Martinez', 2006);

-- @block
INSERT INTO grades (student_ID, subject, grade) VALUES (1, 'Math', 88);
INSERT INTO grades (student_ID, subject, grade) VALUES (1, 'English', 92);
INSERT INTO grades (student_ID, subject, grade) VALUES (1, 'Science', 85);
INSERT INTO grades (student_ID, subject, grade) VALUES (2, 'Math', 75);
INSERT INTO grades (student_ID, subject, grade) VALUES (2, 'History', 83);
INSERT INTO grades (student_ID, subject, grade) VALUES (2, 'English', 79);
INSERT INTO grades (student_ID, subject, grade) VALUES (3, 'Science', 95);
INSERT INTO grades (student_ID, subject, grade) VALUES (3, 'Math', 91);
INSERT INTO grades (student_ID, subject, grade) VALUES (3, 'Art', 89);
INSERT INTO grades (student_ID, subject, grade) VALUES (4, 'Math', 84);
INSERT INTO grades (student_ID, subject, grade) VALUES (4, 'Science', 88);
INSERT INTO grades (student_ID, subject, grade) VALUES (4, 'Physical Education', 93);
INSERT INTO grades (student_ID, subject, grade) VALUES (5, 'English', 90);
INSERT INTO grades (student_ID, subject, grade) VALUES (5, 'History', 85);
INSERT INTO grades (student_ID, subject, grade) VALUES (5, 'Math', 88);
INSERT INTO grades (student_ID, subject, grade) VALUES (6, 'Science', 72);
INSERT INTO grades (student_ID, subject, grade) VALUES (6, 'Math', 78);
INSERT INTO grades (student_ID, subject, grade) VALUES (6, 'English', 81);
INSERT INTO grades (student_ID, subject, grade) VALUES (7, 'Art', 94);
INSERT INTO grades (student_ID, subject, grade) VALUES (7, 'Science', 87);
INSERT INTO grades (student_ID, subject, grade) VALUES (7, 'Math', 90);
INSERT INTO grades (student_ID, subject, grade) VALUES (8, 'History', 77);
INSERT INTO grades (student_ID, subject, grade) VALUES (8, 'Math', 83);
INSERT INTO grades (student_ID, subject, grade) VALUES (8, 'Science', 80);
INSERT INTO grades (student_ID, subject, grade) VALUES (9, 'English', 96);
INSERT INTO grades (student_ID, subject, grade) VALUES (9, 'Math', 89);
INSERT INTO grades (student_ID, subject, grade) VALUES (9, 'Art', 92);

-- @block
-- INDEXING FOR OPTIMIZATION
-- Index for Task 3,4,7,8 JOIN condition
CREATE INDEX idx_grades_student_id ON grades (student_ID);

-- Index for Task 3 and 8 WHERE conditions
CREATE INDEX idx_grades_grade ON grades (grade);

-- Index for Task 6 GROUP BY
CREATE INDEX idx_grades_subject ON grades (subject);

-- Index for Task 5 WHERE condition
CREATE INDEX idx_students_birth_year ON students (birth_year);

-- @block
-- 3. Find all grades for a specific student (Alice Johnson)
SELECT
	T2.subject,
  T2.grade
FROM
	students AS T1
JOIN
	grades AS T2 ON T1.id = T2.student_ID
WHERE
	T1.full_name = 'Alice Johnson';

-- @block
-- 4. Calculate the average grade per student
SELECT
  T1.full_name,
  AVG(T2.grade) AS average_grade
FROM
  students AS T1
JOIN
  grades AS T2 ON T1.id = T2.student_ID
GROUP BY 
  T1.full_name
ORDER BY
  average_grade DESC;

-- @block
-- 5. List all students born after 2004
SELECT 
  full_name, birth_year
FROM
  students
WHERE
  birth_year > 2004;

-- @block
-- 6. Create a query that lists all subjects and their average grades
SELECT
  subject,
  AVG(grade) AS average_grade
FROM
  grades
GROUP BY
  subject
ORDER BY
  average_grade DESC;

-- @block
-- 7. Find the top 3 students with the highest average grades
SELECT
  T1.full_name,
  AVG(T2.grade) AS average_grade
FROM
  students AS T1
JOIN
  grades AS T2 ON T1.id = T2.student_ID
GROUP BY
  T1.full_name
ORDER BY
  average_grade DESC
LIMIT 3;

-- @block
-- 8. Show all students who have scored below 80 in any subject
SELECT DISTINCT
  T1.full_name
FROM
  students AS T1
JOIN
  grades AS T2 ON T1.id = T2.student_ID
WHERE
  T2.grade < 80;