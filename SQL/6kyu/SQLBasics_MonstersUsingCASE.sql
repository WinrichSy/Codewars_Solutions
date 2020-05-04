--SQL Basics - Monsters using CASE
--https://www.codewars.com/kata/593ef0e98b90525e090000b9

SELECT top_half.id, top_half.heads, top_half.arms, bottom_half.tails, bottom_half.legs,
CASE WHEN top_half.heads > top_half.arms OR
          bottom_half.tails > bottom_half.legs THEN 'BEAST' ELSE 'WEIRDO' END AS species
FROM top_half
INNER JOIN bottom_half
ON top_half.id = bottom_half.id
ORDER BY species
