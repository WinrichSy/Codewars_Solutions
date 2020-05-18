--SQL with Sailor Moon: Thinking about JOINS...
--https://www.codewars.com/kata/5ab7a736edbcfc8e62000007

SELECT senshi_name as sailor_senshi, real_name_jpn as real_name, cats.name as cat, schools.school as school
FROM sailorsenshi
LEFT JOIN cats ON cats.id = sailorsenshi.cat_id
LEFT JOIN schools ON schools.id = sailorsenshi.school_id;
