"""
LeetCode 1623. All Valid Triplets That Can Represent a Country

Table: Country
+-------------+------+
| Column Name | Type |
+-------------+------+
| name        | varchar |
| continent   | varchar |
| area        | int  |
| population  | int  |
| gdp         | bigint |
+-------------+------+
name is the primary key for this table.

Write an SQL query to find all valid triplets (name, continent, area) such that the area is greater than 3 million, the population is greater than 25 million, and the gdp is greater than 1 trillion.

Example:
Input:
Country table:
| name    | continent | area    | population | gdp         |
|---------|-----------|---------|------------|-------------|
| China   | Asia      | 9596961 | 1403500365 | 12237700000 |
| India   | Asia      | 3287263 | 1324171354 | 2626110000  |
| USA     | America   | 9372610 | 324459463  | 19485394000 |
Output:
| name  | continent | area    |
|-------|-----------|---------|
| China | Asia      | 9596961 |
| USA   | America   | 9372610 |
"""

-- SQL Query:
SELECT name, continent, area
FROM Country
WHERE area > 3000000 AND population > 25000000 AND gdp > 1000000000000;
