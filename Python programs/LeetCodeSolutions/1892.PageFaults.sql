"""
LeetCode 1892. Page Faults

Table: Pages
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| page_id     | int   |
| process_id  | int   |
| time_stamp  | int   |
+-------------+-------+
page_id is the primary key for this table.

Write an SQL query to find the number of page faults for each process.

Example:
Pages table:
| page_id | process_id | time_stamp |
|---------|------------|------------|
| 1       | 1          | 1          |
| 2       | 1          | 2          |
| 3       | 2          | 1          |

Output:
| process_id | faults |
|------------|--------|
| 1          | 2      |
| 2          | 1      |
"""

-- SQL Solution
SELECT process_id, COUNT(DISTINCT page_id) AS faults
FROM Pages
GROUP BY process_id;
