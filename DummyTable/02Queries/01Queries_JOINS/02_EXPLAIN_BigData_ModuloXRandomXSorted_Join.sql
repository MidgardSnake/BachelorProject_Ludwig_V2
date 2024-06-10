ANALYZE table1;
ANALYZE table2;
ANALYZE table3;


EXPLAIN
SELECT *
FROM table3 t3
LEFT JOIN table1 t1 ON t1.nummer = t3.nummer
LEFT JOIN table2 t2 ON t2.nummer = t1.nummer;

/*
EXPLAIN
SELECT *
FROM table1 t1
LEFT JOIN table2 t2 ON t1.nummer = t2.nummer
LEFT JOIN table3 t3 ON t3.nummer = t1.nummer;
*/