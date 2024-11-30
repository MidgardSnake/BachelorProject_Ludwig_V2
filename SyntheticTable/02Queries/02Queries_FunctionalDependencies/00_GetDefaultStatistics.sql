ANALYZE synthetictabletest;


SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable' AND attname IN ('linear_dist','modulo');

SELECT *
FROM pg_stats
WHERE tablename = 'synthetictabletest';

SELECT COUNT(*) FROM synthetictable;



EXPLAIN ANALYZE SELECT *
FROM synthetictabletest
WHERE linear_dist = 144;

 SELECT *
FROM synthetictable
WHERE linear_dist = 0;



