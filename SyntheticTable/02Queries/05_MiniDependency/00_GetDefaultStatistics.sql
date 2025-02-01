

ANALYSE t1 ;
ANALYSE t2 ;



EXPLAIN ANALYZE
SELECT *
FROM  t1
INNER JOIN  t2 ON t1.id = t2.id
    WHERE t1.id = t2.ref_id;


CREATE STATISTICS x_dependency (dependencies )
ON t2.id, t2.ref_id
FROM  t2;

DROP STATISTICS x_dependency;



CREATE STATISTICS t3ab (dependencies )
ON a, b
FROM tablex3;

CREATE STATISTICS t2ab (dependencies )
ON a, b
FROM tablex2;

ANALYZE tablex2;
ANALYZE tablex3;

EXPLAIN ANALYSE
SELECT *
FROM tablex2 t2
    INNER JOIN tablex1 t1 ON t1.ref2 = t2.id
    INNER JOIN tablex3 t3 ON t3.id = t1.ref3
WHERE
    t2.a = 1 AND t2.b= 1
AND t3.a = 1 AND t3.b = 1;



SELECT *
FROM t1, t2
WHERE t1.id = t2.id;

SELECT name
FROM synthetictable_actors
WHERE birthyear = 1977;

