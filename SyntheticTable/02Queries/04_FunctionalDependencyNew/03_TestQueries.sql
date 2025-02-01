

SELECT Count(*)
FROM tablex2 t2
    INNER JOIN tablex1 t1 ON t1.ref2 = t2.id
WHERE t2.a = 1 and t2.b= 1;


EXPLAIN ANALYZE SELECT *
FROM tablex3 t3
    INNER JOIN tablex1 t1 ON t1.ref3 = t3.id
    INNER JOIN tablex2 t2 ON t2.id = t1.ref2
WHERE t3.a = 1 and t3.b= 1;




ALTER TABLE SyntheticTable_Actors ALTER COLUMN birthyear TYPE VARCHAR;

EXPLAIN ANALYZE
SELECT *
FROM table1 t1
INNER JOIN table2 t2 ON t2.nkey = t1.nkey
INNER JOIN table3 t3 ON t3.nkey = t1.nkey;



