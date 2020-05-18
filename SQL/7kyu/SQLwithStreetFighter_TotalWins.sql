--SQL with Street Fighter: Total Wins
--https://www.codewars.com/kata/5ac698cdd325ad18a3000170

SELECT f.name, SUM(f.won) as won, SUM(f.lost)as lost
FROM fighters f
JOIN winning_moves wm
ON f.move_id = wm.id
WHERE wm.move != 'Hadoken' AND wm.move != 'Shouoken' AND wm.move != 'Kikoken'
GROUP BY f.name
ORDER BY won DESC, lost DESC
LIMIT 6;
