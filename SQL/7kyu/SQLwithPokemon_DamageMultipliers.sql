--SQL with Pokemon: Damage Multipliers
--https://www.codewars.com/kata/5ab828bcedbcfc65ea000099

SELECT *
FROM(
  SELECT pokemon_name, pokemon.str * multipliers.multiplier as modifiedStrength, multipliers.element as element
  FROM pokemon
  LEFT JOIN multipliers
  ON pokemon.element_id = multipliers.id) AS subquery
WHERE modifiedStrength >= 40
ORDER BY modifiedStrength DESC;
