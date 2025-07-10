"""
LeetCode 1772. Sort Features by Popularity

Table: Features
+-------------+------+
| Column Name | Type |
+-------------+------+
| feature     | varchar |
| popularity  | int  |
+-------------+------+
(feature) is the primary key.

Write an SQL query to return the features sorted by popularity in descending order.

Example:
Features table:
| feature | popularity |
|---------|------------|
| A       | 5          |
| B       | 10         |
| C       | 7          |

Output:
| feature | popularity |
|---------|------------|
| B       | 10         |
| C       | 7          |
| A       | 5          |

"""
SELECT feature, popularity
FROM Features
ORDER BY popularity DESC;
