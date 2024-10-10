SELECT Count(*) FROM synthetictable;

SELECT * FROM synthetictable FETCH FIRST 15 ROWS ONLY;

ANALYZE table1;

SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable';

--tatsächliche MCV's
SELECT  normal_dist, Count(normal_dist) counter
FROM synthetictable
GROUP BY normal_dist
ORDER BY counter DESC;
-- mcv 1 = 500/224 ; mcv100 = 244/29 ; mcv101 359/29; mcv200 126/13






