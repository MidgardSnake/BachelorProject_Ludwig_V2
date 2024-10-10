ANALYZE synthetictable;


/*1. Multiple filter conditions*/

--a. check no where cases without ExtStat
EXPLAIN ANALYSE SELECT * FROM synthetictable;


--b. check one where case  without ExtStat
EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE normal_dist =0;

EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE poisson_dist =0;


EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE synthetictable.exponential_dist =0;

EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE synthetictable.uniform_dist =0;

EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE synthetictable.random_dist =0;

--с. check one where case with ExtStat
EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE synthetictable.modulo =0;

EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE synthetictable.modulo =11;