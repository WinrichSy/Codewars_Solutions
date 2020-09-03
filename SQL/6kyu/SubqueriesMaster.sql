--Subqueries Master
--https://www.codewars.com/kata/594323fde53209e94700012a

SELECT
  (CASE WHEN sub_query.test = '' THEN sub_query.name ELSE CONCAT(sub_query.name,' ',sub_query.first_lastname) END) as name,
  (CASE WHEN sub_query.test = '' THEN sub_query.first_lastname ELSE sub_query.second_lastname END) as first_lastname,
  (CASE WHEN sub_query.test = '' THEN sub_query.second_lastname ELSE test END) as second_lastname
  FROM(
SELECT split_part(name, ' ', 1) as name, split_part(name, ' ',2) as first_lastname, split_part(name, ' ', 3) as second_lastname, split_part(name, ' ',4) as test
FROM people) AS sub_query
