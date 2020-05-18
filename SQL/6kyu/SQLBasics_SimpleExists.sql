--SQL Basics: Simple Exists
--https://www.codewars.com/kata/58113a64e10b53ec36000293

SELECT id, name
FROM departments
WHERE EXISTS
  (SELECT *
   FROM sales
   WHERE sales.department_id = departments.id AND price>98);
