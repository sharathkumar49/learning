"""
LeetCode 1350. Students With Invalid Departments

Table: Departments
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | varchar |
+-------------+------+
id is the primary key.

Table: Students
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | varchar |
| department_id | int  |
+-------------+------+
id is the primary key.

Write an SQL query to report the id and name of all students with an invalid department_id (not in Departments).

Example:
Departments table:
| id | name      |
|----|-----------|
| 1  | Engineering |
| 2  | Science     |

Students table:
| id | name | department_id |
|----|------|---------------|
| 1  | Jack | 1             |
| 2  | Jane | 2             |
| 3  | Mark | 3             |

Output:
| id | name |
|----|------|
| 3  | Mark |

"""
SELECT s.id, s.name
FROM Students s
LEFT JOIN Departments d ON s.department_id = d.id
WHERE d.id IS NULL;
