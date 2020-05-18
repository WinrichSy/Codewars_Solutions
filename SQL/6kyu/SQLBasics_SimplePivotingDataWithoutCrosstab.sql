--SQL Basics: Simple PIVOTING data WITHOUT CROSSTAB
--https://www.codewars.com/kata/5982020284a83baf2f00001c

SELECT name,
        SUM(CASE WHEN detail='good' THEN 1 ELSE 0 END) as good,
        SUM(CASE WHEN detail='ok' THEN 1 ELSE 0 END) as ok,
        SUM(CASE WHEN detail='bad' THEN 1 ELSE 0 END) as bad
FROM (
      SELECT
          name,
          detail
      FROM products
      INNER JOIN details
      ON products.id = details.product_id) as sub_query
GROUP BY name
ORDER BY name
