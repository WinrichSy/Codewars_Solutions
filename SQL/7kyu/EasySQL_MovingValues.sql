--Easy SQL: Moving Values
--https://www.codewars.com/kata/594a389387a7c6a77a000005

SELECT LENGTH(name) as id,
       LENGTH(legs::varchar) as name,
       LENGTH(arms::varchar) as legs,
       LENGTH(characteristics) as arms,
       LENGTH(id::varchar) as characteristics
FROM monsters;
