

--tatsächliche MCV's
SELECT  normal_dist, Count(normal_dist) counter
FROM synthetictable
GROUP BY normal_dist
ORDER BY counter DESC;
-- mcv 1 = 500/224 ; mcv100 = 244/29 ; mcv101 359/29; mcv200 126/13



EXPLAIN SELECT *
FROM synthetictable
WHERE normal_dist = 500; -- richtig 500

EXPLAIN SELECT *
FROM synthetictable
WHERE normal_dist = 244; --richtig 29

EXPLAIN (ANALYZE,BUFFERS) SELECT *
FROM synthetictable
WHERE normal_dist = 359;-- falsch 13 vs 29

EXPLAIN SELECT *
FROM synthetictable
WHERE normal_dist = 126;-- falsch 13 vs 29




