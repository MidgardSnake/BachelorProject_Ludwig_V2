

--tatsächliche MCV's
SELECT  exponential_dist, Count(exponential_dist) counter
FROM synthetictable
GROUP BY exponential_dist
ORDER BY counter DESC;
-- mcv 1 = 500/224 ; mcv100 = 244/29 ; mcv101 359/29; mcv200 126/13



EXPLAIN ANALYZE SELECT *
FROM synthetictable
WHERE exponential_dist = 41; -- richtig 41

EXPLAIN SELECT *
FROM synthetictable
WHERE exponential_dist = 40; --richtig 29






