ANALYZE dummytable;


SELECT *
FROM pg_stats
WHERE tablename = 'dummytable';
