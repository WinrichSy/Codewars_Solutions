--SQL easy regex extraction
--https://www.codewars.com/kata/5c0ae69d5f72394e130025f6

SELECT name, greeting, unnest(REGEXP_MATCHES(greeting, '#([0-9]+)')) as user_id
FROM greetings
