--SQL with LOTR:Elven Wildcards
--https://www.codewars.com/kata/5ad90fb688a0b74111000055

SELECT CONCAT(INITCAP(firstname),' ',INITCAP(lastname)) as shortlist
FROM Elves
WHERE firstname LIKE '%tegil%' or lastname LIKE '%astar%';
