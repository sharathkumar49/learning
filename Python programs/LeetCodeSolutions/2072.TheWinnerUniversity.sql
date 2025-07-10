"""
LeetCode 2072. The Winner University

Table: Students
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| id          | int   |
| name        | varchar|
| university  | varchar|
| score       | int   |
+-------------+-------+
id is the primary key for this table.

Write an SQL query to return the university with the highest average score.

Example:
Students table:
| id | name | university | score |
|----|------|------------|-------|
| 1  | A    | X          | 90    |
| 2  | B    | Y          | 80    |
| 3  | C    | X          | 100   |

Output:
| university |
|------------|
| X          |
"""

-- SQL Solution
SELECT university
FROM Students
GROUP BY university
ORDER BY AVG(score) DESC
LIMIT 1;
