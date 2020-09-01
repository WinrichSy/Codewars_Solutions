--SQL Basics: Truncating
--https://www.codewars.com/kata/594a8fa5a2db9e5f290000c3

SELECT TRUNC(number1::numeric+number2::numeric, 0)::float as towardzero
FROM decimals;
