--On the Canadian Border
--https://www.codewars.com/kata/590ba881fe13cfdcc20001b4

SELECT *
FROM travelers
WHERE country NOT IN ('Canada', 'Mexico', 'USA')
