ANALYZE synthetictable;



SELECT Count(*)
    FROM synthetictable;
/*1. Multiple filter conditions*/



--b. check two where cases without FD
EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE normal_dist =0 AND poisson_dist = 18;

EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE poisson_dist =0 AND exponential_dist = 12;

--b. check two where cases with FD
EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE normal_dist =0 AND modulo = 2;

EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE normal_dist =10 AND modulo = 2;

EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE normal_dist =500 AND modulo = 0;

SELECT
    normal_dist,
    Count(normal_dist) as Count,
    COUNT(normal_dist) * 1.0 / SUM(COUNT(normal_dist)) OVER () AS Frequency
FROM synthetictable
GROUP BY normal_dist
ORDER BY count DESC;

SELECT Count(*)
FROM synthetictable
WHERE modulo = 0 ;




SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable' and attname IN ('normal_dist','modulo') ;

