ANALYZE synthetictable;


SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable' AND attname IN ('exponential_dist','modulo');

SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable';

SELECT COUNT(*) FROM synthetictable;



