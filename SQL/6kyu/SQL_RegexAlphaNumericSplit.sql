--SQL: Regex AlphaNumeric Split
--https://www.codewars.com/kata/594257d4db68b6e99200002c

SELECT project, REGEXP_REPLACE(address, '[A-Za-z]', '', 'g') as numbers, REGEXP_REPLACE(address, '[0-9]', '', 'g') as letters
FROM repositories
