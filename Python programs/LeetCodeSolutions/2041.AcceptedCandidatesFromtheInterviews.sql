"""
LeetCode 2041. Accepted Candidates From the Interviews

Table: Candidates
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| candidate_id| int   |
| score       | int   |
+-------------+-------+
candidate_id is the primary key for this table.

Write an SQL query to return the candidate_id of all candidates with a score >= 60.

Example:
Candidates table:
| candidate_id | score |
|--------------|-------|
| 1            | 80    |
| 2            | 55    |
| 3            | 60    |

Output:
| candidate_id |
|--------------|
| 1            |
| 3            |
"""

-- SQL Solution
SELECT candidate_id
FROM Candidates
WHERE score >= 60;
