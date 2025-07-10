"""
LeetCode 2159. Order Two Columns Independently

Table: Data
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| col1        | int  |
| col2        | int  |
+-------------+------+
id is the primary key.

Write an SQL query to independently order col1 and col2 in ascending order and return the result with the original id.

Example:
Data table:
| id | col1 | col2 |
|----|------|------|
| 1  | 2    | 3    |
| 2  | 4    | 1    |
| 3  | 3    | 2    |

Output:
| id | col1 | col2 |
|----|------|------|
| 1  | 2    | 1    |
| 2  | 3    | 2    |
| 3  | 4    | 3    |

Solution:
WITH c1 AS (
  SELECT id, col1, ROW_NUMBER() OVER (ORDER BY id) rn1, ROW_NUMBER() OVER (ORDER BY col1) rnk1 FROM Data
),
c2 AS (
  SELECT id, col2, ROW_NUMBER() OVER (ORDER BY id) rn2, ROW_NUMBER() OVER (ORDER BY col2) rnk2 FROM Data
)
SELECT c1.id, c1v.col1, c2v.col2
FROM c1
JOIN c1 c1v ON c1.rn1 = c1v.rnk1
JOIN c2 c2v ON c1.rn1 = c2v.rnk2
ORDER BY c1.id;
