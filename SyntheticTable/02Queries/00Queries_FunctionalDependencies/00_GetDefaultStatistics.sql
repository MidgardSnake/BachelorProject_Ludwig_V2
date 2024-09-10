ANALYZE dummytable;


SELECT *
FROM pg_stats
WHERE tablename = 'dummytable' AND attname = 'exponential_dist';

SELECT COUNT(*) FROM Dummytable;



SELECT normal_dist
FROM dummytable
WHERE normal_dist > 0
;
