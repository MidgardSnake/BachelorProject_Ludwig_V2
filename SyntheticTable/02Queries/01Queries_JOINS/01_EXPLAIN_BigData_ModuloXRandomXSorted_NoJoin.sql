ANALYZE table1;
ANALYZE table2;
ANALYZE table3;


EXPLAIN ANALYZE
SELECT *
FROM table1 t1
INNER JOIN table2 t2 ON t2.ref_id = t1.id
INNER JOIN table3 t3 ON t3.ref_id = t2.id
WHERE   t2.a = 43 AND t2.b = 43
AND t3.a = 43 AND t3.b = 43;
