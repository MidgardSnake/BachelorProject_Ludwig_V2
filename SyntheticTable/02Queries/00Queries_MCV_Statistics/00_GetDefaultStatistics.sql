SELECT Count(*) FROM synthetictable;

SELECT * FROM synthetictable FETCH FIRST 100 ROWS ONLY;

ANALYZE synthetictable;

SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable';

--tatsächliche MCV's
SELECT  exponential_dist, Count(exponential_dist) counter
FROM synthetictable
GROUP BY exponential_dist
ORDER BY counter DESC;
-- mcv 1 = 500/224 ; mcv100 = 244/29 ; mcv101 359/29; mcv200 126/13






