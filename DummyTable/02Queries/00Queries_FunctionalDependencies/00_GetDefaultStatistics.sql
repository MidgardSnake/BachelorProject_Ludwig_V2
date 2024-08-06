ANALYZE dummytable;


SELECT *
FROM pg_stats
WHERE tablename = 'dummytable';



SELECT normal_dist
FROM dummytable
WHERE normal_dist > 0
;
