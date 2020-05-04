--Conditional Count
--https://www.codewars.com/kata/5816a3ecf54413a113000074

SELECT EXTRACT(MONTH from payment_date) as month, COUNT(payment_id) as total_count, SUM(amount) as total_amount,
SUM (CASE
  WHEN staff_id = 1 THEN 1
                    ELSE 0
  END) AS mike_count,
SUM (CASE
  WHEN staff_id = 1 THEN amount
                    ELSE 0
  END) AS mike_amount,
SUM (CASE
  WHEN staff_id = 2 THEN 1
                    ELSE 0
  END) AS jon_count,
SUM (CASE
  WHEN staff_id = 2 THEN amount
                    ELSE 0
  END) AS jon_amount
from payment
GROUP BY month
ORDER BY month ASC;
