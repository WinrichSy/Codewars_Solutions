--Countries Capitals for Trivia Night (SQL for Beginners #6)
--https://www.codewars.com/kata/5e5f09dc0a17be0023920f6f

SELECT capital
FROM countries
WHERE continent = 'Africa' AND country LIKE 'E%' OR continent = 'Afrika' AND country LIKE 'E%'
ORDER BY capital
LIMIT 3;
