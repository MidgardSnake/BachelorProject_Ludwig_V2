SELECT Count(*) FROM synthetictablebig;

SELECT * FROM synthetictablebig FETCH FIRST 100 ROWS ONLY;
SELECT * FROM synthetictablebig
         ORDER BY linear_dist desc
         FETCH FIRST 100 ROWS ONLY;

ANALYZE synthetictablebig;

SELECT *
FROM pg_stats
WHERE tablename = 'synthetictablebig';

--tatsächliche MCV's für linear
SELECT  linear_dist, Count(linear_dist) counter
FROM synthetictablebig
GROUP BY linear_dist
ORDER BY counter DESC;
-- mcv 1 = 500/224 ; mcv100 = 244/29 ; mcv101 359/29; mcv200 126/13

--tatsächliche MCV's für modulo
SELECT  modulo, Count(modulo) counter
FROM synthetictable
GROUP BY modulo
ORDER BY counter DESC;

EXPLAIN ANALYZE SELECT *
FROM synthetictablebig
WHERE linear_dist = '1399';






