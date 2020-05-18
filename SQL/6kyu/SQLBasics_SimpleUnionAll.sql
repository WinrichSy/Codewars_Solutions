--SQL Basics: Simple UNION ALL
--https://www.codewars.com/kata/58112f8004adbbdb500004fe

SELECT *
FROM
(SELECT 'US' as location, id, name, price, card_name, card_number, transaction_date
FROM ussales
UNION ALL
SELECT 'EU' as location, id, name, price, card_name, card_number, transaction_date
FROM eusales) AS uaeu
WHERE price >= 50.00
ORDER BY location DESC, id
