--Grocery Store: Real Price!
--https://www.codewars.com/kata/5a8f00745084d718940000c5

SELECT name, weight, price, ROUND((price/(weight/1000))::numeric, 2)::float as price_per_kg
FROM products
ORDER BY price_per_kg ASC, name ASC;
