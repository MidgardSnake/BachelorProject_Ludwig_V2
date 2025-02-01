ANALYZE tablex1;
ANALYZE tablex2;
ANALYZE tablex3;

SELECT * FROM tablex1;


SELECT relpages,reltuples
FROM pg_class
WHERE relname = 'tablex3'
;
SELECT *
FROM pg_stats
WHERE tablename = 'tablex3';


--test2
EXPLAIN ANALYSE
SELECT *
FROM tablex2 t2
    INNER JOIN tablex1 t1 ON t1.ref2 = t2.id
    INNER JOIN tablex3 t3 ON t3.id = t1.ref3
WHERE
    t2.a = 1 AND t2.b= 1
AND t3.a = 1 AND t3.b = 1
;



CREATE STATISTICS ab_dep (dependencies)
ON a, b
FROM tablex2;


CREATE STATISTICS ab_dep2 (dependencies)
ON a, b
FROM tablex3;


SELECT *
FROM pg_statistic_ext;



DROP STATISTICS ab_dep;
DROP STATISTICS ab_dep2;
