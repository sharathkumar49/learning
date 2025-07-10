"""
LeetCode 1988. Find Cutoff Score for Each School

Table: Scores
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| school_id   | int   |
| score       | int   |
+-------------+-------+
(school_id, score) is the primary key for this table.

Write an SQL query to find the cutoff score for each school.

Example:
Scores table:
| school_id | score |
|-----------|-------|
| 1         | 90    |
| 1         | 80    |
| 2         | 70    |
| 2         | 60    |

Output:
| school_id | cutoff |
|-----------|--------|
| 1         | 85     |
| 2         | 65     |
"""

-- SQL Solution
SELECT school_id, FLOOR(AVG(score)) AS cutoff
FROM Scores
GROUP BY school_id;
