"""
175. Combine Two Tables
https://leetcode.com/problems/combine-two-tables/

SQL Schema:
Person table: id, name
Address table: personId, city, state

Write a SQL query to report the name, city, and state of each person in the Person table. If the address of a person is not present, report null for city and state.

Example:
Input:
Person table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Wang     |
| 2  | Alice    |
+----+----------+
Address table:
+-----------+----------+----------+
| personId  | city     | state    |
+-----------+----------+----------+
| 1         | New York | NY       |
+-----------+----------+----------+
Output:
+----------+----------+----------+
| name     | city     | state    |
+----------+----------+----------+
| Wang     | New York | NY       |
| Alice    | null     | null     |
+----------+----------+----------+
"""
-- SQL Solution
SELECT Person.name, Address.city, Address.state
FROM Person
LEFT JOIN Address ON Person.id = Address.personId;
