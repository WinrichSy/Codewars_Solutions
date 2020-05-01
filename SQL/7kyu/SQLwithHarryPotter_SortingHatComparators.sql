--SQL with Harry Potter: Sorting Hat Comparators
--https://www.codewars.com/kata/5abcf0f930488ff1a6000b66

SELECT id, name, quality1, quality2
FROM students
WHERE (quality1='brave' and NOT quality2='evil')
    OR (quality1='evil' and quality2='cunning')
    OR (quality1='studious' OR quality2='intelligent')
    OR (quality1='hufflepuff' OR quality2='hufflepuff')
ORDER BY id
