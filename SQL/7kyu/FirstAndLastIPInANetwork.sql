--Find and last IP in a network
--https://www.codewars.com/kata/5db5ff03d10bfa001da9cf2e

SELECT c.id, network(c.ip_address) as first_address, broadcast(c.ip_address) as last_address
FROM connections c;
