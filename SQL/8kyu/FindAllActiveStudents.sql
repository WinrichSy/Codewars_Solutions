--Find all active students
--https://www.codewars.com/kata/5809b9ef88b750ab180001ec

SELECT FirstName, LastName, isactive
FROM students
LIMIT 4
WHERE students.isactive = 'true' or students.isactive='True'
