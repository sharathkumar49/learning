"""
LeetCode 1767. Find the Subtasks That Did Not Execute

Table: Tasks
+-------------+------+
| Column Name | Type |
+-------------+------+
| task_id     | int  |
| subtask_id  | int  |
| status      | enum('completed', 'not_completed') |
+-------------+------+
(task_id, subtask_id) is the primary key.

Write an SQL query to find the task_id and subtask_id of all subtasks that did not execute (status = 'not_completed').

Example:
Tasks table:
| task_id | subtask_id | status        |
|---------|------------|---------------|
| 1       | 1          | completed     |
| 1       | 2          | not_completed |
| 2       | 1          | not_completed |

Output:
| task_id | subtask_id |
|---------|------------|
| 1       | 2          |
| 2       | 1          |

"""
SELECT task_id, subtask_id
FROM Tasks
WHERE status = 'not_completed';
