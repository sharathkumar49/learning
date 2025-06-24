-- LeetCode 1384. Total Sales Amount by Year
-- Given a Sales table, write a SQL query to report the total sales amount for each year.

-- Table: Sales
-- +-------------+------+--+
-- | Column Name | Type |
-- +-------------+------+
-- | sale_id     | int  |
-- | product_id  | int  |
-- | year        | int  |
-- | quantity    | int  |
-- | price       | int  |
-- +-------------+------+
-- sale_id is the primary key.
-- Each row of this table shows the ID of the product sold, the year, the quantity, and the price.

-- Write a SQL query to report the total sales amount for each year.

SELECT year, SUM(quantity * price) AS total_amount
FROM Sales
GROUP BY year;
