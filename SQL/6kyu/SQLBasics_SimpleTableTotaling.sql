--SQL Basics: Simple Table Totaling
--https://www.codewars.com/kata/5809575e166583acfa000083

SELECT *, RANK() OVER (ORDER BY total_points DESC) rank
FROM(
  SELECT COUNT(name) as total_people, SUM(points) as total_points,
    CASE WHEN clan='' THEN '[no clan specified]'
         ELSE clan
    END AS clan
  FROM people
  GROUP BY clan) as subquery
ORDER BY rank;
