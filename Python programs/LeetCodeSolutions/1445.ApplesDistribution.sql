"""
LeetCode 1445. Apples Distribution

Table: Boxes
+-------------+------+
| Column Name | Type |
+-------------+------+
| box_id      | int  |
| apple_count | int  |
+-------------+------+
box_id is the primary key for this table.

Write an SQL query to report the number of apples in each box. Return the result table ordered by box_id.

Example:
Input:
Boxes table:
| box_id | apple_count |
|--------|-------------|
| 1      | 7           |
| 2      | 4           |
| 3      | 9           |
Output:
| box_id | apple_count |
|--------|-------------|
| 1      | 7           |
| 2      | 4           |
| 3      | 9           |
"""

--SQL Query:
SELECT box_id, apple_count
FROM Boxes
ORDER BY box_id;
