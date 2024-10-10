ANALYZE synthetictable;


SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable' AND attname = 'exponential_dist';

SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable';

SELECT COUNT(*) FROM synthetictable;



