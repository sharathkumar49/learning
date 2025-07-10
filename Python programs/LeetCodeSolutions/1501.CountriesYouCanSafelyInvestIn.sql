"""
LeetCode 1501. Countries You Can Safely Invest In

Table: Person
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | text |
| phone_number| text |
+-------------+------+
id is the primary key for this table.

Table: Country
+-------------+------+
| Column Name | Type |
+-------------+------+
| name        | text |
| country_code| text |
+-------------+------+
name is the primary key for this table.

Write an SQL query to find the countries where all phone numbers of people from that country start with the country code.

Example:
Input:
Person table:
| id | name | phone_number |
|----|------|--------------|
| 1  | A    | +1-123-456   |
| 2  | B    | +44-123-456  |
| 3  | C    | +1-987-654   |
Country table:
| name    | country_code |
|---------|--------------|
| USA     | +1           |
| UK      | +44          |
Output:
| name |
|------|
| USA  |
"""

-- SQL Query:
SELECT c.name
FROM Country c
JOIN Person p ON p.phone_number LIKE c.country_code || '%'
GROUP BY c.name
HAVING COUNT(*) = (
    SELECT COUNT(*) FROM Person p2 WHERE p2.phone_number LIKE c.country_code || '%'
);
