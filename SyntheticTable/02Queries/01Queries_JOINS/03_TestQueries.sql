ANALYZE table1;


SELECT Count(Distinct ndependency)
FROM table3
;


ALTER TABLE SyntheticTable_Actors ALTER COLUMN birthyear TYPE VARCHAR;

EXPLAIN ANALYZE
SELECT *
FROM table1 t1
INNER JOIN table2 t2 ON t2.nkey = t1.nkey
INNER JOIN table3 t3 ON t3.nkey = t1.nkey;



