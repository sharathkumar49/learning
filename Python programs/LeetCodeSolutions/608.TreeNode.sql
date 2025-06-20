"""
608. Tree Node (SQL)
Difficulty: Medium

Table: Tree
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| p_id        | int  |
+-------------+------+
id is the primary key for this table.
p_id is the parent id of id.

Write an SQL query to report the type of each node in the tree:
- 'Root' if the node is the root.
- 'Leaf' if the node is a leaf node.
- 'Inner' if the node is neither root nor leaf.

Example:
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+

Result table:
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+

SQL Solution:
SELECT id,
  CASE
    WHEN p_id IS NULL THEN 'Root'
    WHEN id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
    ELSE 'Inner'
  END AS type
FROM Tree;
