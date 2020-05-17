--SQL Basics: Up and Down
--https://www.codewars.com/kata/595a3ba3843b0cbf8e000004

SELECT
  CASE WHEN SUM(number1)%2 = 1 THEN MIN(number1)
       ELSE MAX(number1)
       END as number1,
  CASE WHEN SUM(number2)%2 = 1 THEN MIN(number2)
       ELSE MAX(number2)
       END as number2
FROM numbers;
