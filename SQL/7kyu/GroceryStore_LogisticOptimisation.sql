--Grocery Store: Logistic Optimisation
--https://www.codewars.com/kata/5a8ec692b17101bfc70001ba

SELECT producer, COUNT(DISTINCT(id)) as unique_products
FROM products
GROUP BY producer
ORDER BY unique_products DESC, producer;
