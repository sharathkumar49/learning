"""
LeetCode 1811. Find Interview Candidates

Table: Candidates
+-------------+------+
| Column Name | Type |
+-------------+------+
| candidate_id| int  |
| skill       | varchar |
+-------------+------+
(candidate_id, skill) is the primary key.

Write an SQL query to find the candidate_id of candidates who have both 'Python' and 'SQL' skills.

Example:
Candidates table:
| candidate_id | skill  |
|--------------|--------|
| 1            | Python |
| 1            | SQL    |
| 2            | Python |
| 3            | SQL    |

Output:
| candidate_id |
|--------------|
| 1            |

"""
SELECT candidate_id
FROM Candidates
WHERE skill IN ('Python', 'SQL')
GROUP BY candidate_id
HAVING COUNT(DISTINCT skill) = 2;
