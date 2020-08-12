--SQL Basics: Simple WITH
--https://www.codewars.com/kata/5811501c2d35672d4f000146

WITH special_sales as
  (SELECT *
   FROM sales
   WHERE price > 90.00)
   SELECT id, name
   FROM departments
