SELECT Count(*) FROM synthetictable;

SELECT * FROM synthetictable FETCH FIRST 100 ROWS ONLY;

ANALYZE synthetictable;

SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable';

--tatsächliche MCV's für linear
SELECT  linear_dist, Count(linear_dist) counter
FROM synthetictable
GROUP BY linear_dist
ORDER BY counter DESC;
-- mcv 1 = 500/224 ; mcv100 = 244/29 ; mcv101 359/29; mcv200 126/13

--tatsächliche MCV's für modulo
SELECT  modulo, Count(modulo) counter
FROM synthetictable
GROUP BY modulo
ORDER BY counter DESC;

EXPLAIN ANALYSE SELECT *
FROM synthetictable
WHERE linear_dist = '38';






