ANALYZE table1;
ANALYZE table2;
ANALYZE table3;

SELECT * FROM table1;

SELECT Count(*) FROM table1;

SELECT relpages,reltuples
FROM pg_class
WHERE relname = 'table3'
;

SELECT *
FROM pg_stats
WHERE tablename = 'table1';




SELECT *
FROM table2
WHERE id BETWEEN 4999999 and 5000005
;
