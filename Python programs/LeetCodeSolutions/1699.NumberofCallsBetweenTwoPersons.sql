"""
LeetCode 1699. Number of Calls Between Two Persons

Table: Calls
+-------------+------+ 
| Column Name | Type | 
+-------------+------+ 
| from_id     | int  |
| to_id       | int  |
| duration    | int  |
+-------------+------+
There is no primary key for this table. It may contain duplicates.

Write an SQL query to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

Example:
Calls table:
| from_id | to_id | duration |
|---------|-------|----------|
| 1       | 2     | 59       |
| 2       | 1     | 11       |
| 1       | 3     | 20       |
| 3       | 4     | 100      |
| 3       | 4     | 200      |

Output:
| person1 | person2 | call_count | total_duration |
|---------|---------|------------|----------------|
| 1       | 2       | 2          | 70             |
| 1       | 3       | 1          | 20             |
| 3       | 4       | 2          | 300            |

"""

SELECT
    LEAST(from_id, to_id) AS person1,
    GREATEST(from_id, to_id) AS person2,
    COUNT(*) AS call_count,
    SUM(duration) AS total_duration
FROM Calls
WHERE from_id != to_id
GROUP BY person1, person2;
