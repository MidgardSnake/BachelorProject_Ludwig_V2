ANALYZE table1;

SELECT Count(*) FROM table3;

SELECT *
FROM pg_stats
WHERE tablename = 'table1';


ANALYZE table2;
SELECT *
FROM pg_stats
WHERE tablename = 'table2';

ANALYZE table3;
SELECT *
FROM pg_stats
WHERE tablename = 'table3';


ANALYZE synthetictable;
SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable';
