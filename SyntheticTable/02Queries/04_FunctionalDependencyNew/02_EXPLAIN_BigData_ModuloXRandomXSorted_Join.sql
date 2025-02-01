ANALYZE table1;
ANALYZE table2;
ANALYZE table3;



/*------------------------------EXPERIMENT--------------------------------------*/
/* Gib zuerst den allgemeinen Queryplan für alle Tabellen an*/

--0. default
EXPLAIN ANALYZE
SELECT *
FROM table3 t3
INNER JOIN table2 t2 ON t2.id = t3.ref_id
INNER JOIN table1 t1 ON t1.id = t2.ref_id
WHERE t1.a = 43 AND t1.b = 43;


--1. zwei Filterbedingung auf zwei Tabellen ohne stats
EXPLAIN ANALYZE
SELECT *
FROM table1 t1
INNER JOIN table2 t2 ON t2.ref_id = t1.id
INNER JOIN table3 t3 ON t3.ref_id = t2.id
WHERE   t2.a = 43 AND t2.b = 43
AND t3.a = 43 AND t3.b = 43
;

CREATE STATISTICS t3ab (dependencies )
ON a, b
FROM table3;

CREATE STATISTICS t2ab (dependencies )
ON a, b
FROM table2;

CREATE INDEX idx_table2_a_b ON table2 (a, b);
CREATE INDEX idx_table3_a_b ON table3 (a, b);
ANALYZE table3;
ANALYZE table2;



DROP INDEX idx_table2_a_b;
DROP INDEX idx_table3_a_b;



ANALYSE table3;

--2. zwei Filterbedingung auf zwei Tabellen mit stats
EXPLAIN ANALYZE
SELECT *
FROM table1 t1
INNER JOIN table2 t2 ON t2.ref_id = t1.id
INNER JOIN table3 t3 ON t3.ref_id = t2.id
WHERE   t2.a = 43 AND t2.b = 43
AND t3.a = 43 AND t3.b = 43
;

DROP STATISTICS t3ab ;
ANALYSE table3;

--2. hashjoin off
SHOW enable_hashjoin ;
SET enable_hashjoin TO off;

ANALYSE table1;
EXPLAIN ANALYZE
SELECT *
FROM table3 t3
INNER JOIN table1 t1 ON t1.nkey = t3.nkey
INNER JOIN table2 t2 ON t2.nkey = t1.nkey;

SET enable_hashjoin  to on;


SET max_parallel_workers_per_gather = 2;
--3.more workers
SET max_parallel_workers_per_gather = 0;

EXPLAIN (ANALYZE)
SELECT *
FROM table3 t3
INNER JOIN table1 t1 ON t1.nkey = t3.nkey
INNER JOIN table2 t2 ON t2.nkey = t1.nkey;

/*------------------------------EXPERIMENT--------------------------------------*/


CREATE STATISTICS stats_name (dependencies) ON nkey, ndependency FROM table1;
DROP STATISTICS stats_name;
ALTER TABLE table1 ALTER COLUMN nkey SET STATISTICS -1;
CREATE INDEX index_join ON table1 (ndependency);
DROP INDEX index_join;

ANALYZE table1;
/*------------------------------EXPERIMENT--------------------------------------*/

/* Gib den  Queryplan für alle Tabellen an, wobei t1 mit t2 über distinct gejoined wird*/
EXPLAIN ANALYSE
SELECT *
FROM table3 t3
INNER JOIN table1 t1 ON t1.nkey = t3.nkey
INNER JOIN table2 t2 ON t2.ndependency = t1.ndependency;


/* Gib den  Queryplan für alle Tabellen an, wobei t1 mit t3 über distinct gejoined wird*/
EXPLAIN ANALYSE
SELECT *
FROM table3 t3
INNER JOIN table1 t1 ON t1.ndependency = t3.ndependency
INNER JOIN table2 t2 ON t2.nkey = t1.nkey;


/* Gib den  Queryplan für alle Tabellen an, wobei t2 mit t3 über distinct gejoined wird*/
EXPLAIN ANALYSE
SELECT *
FROM table3 t3
INNER JOIN table1 t1 ON t1.nkey = t3.nkey
INNER JOIN table2 t2 ON t2.ndependency = t3.ndependency;


/* Gib mir einen einfachen Output aus*/

EXPLAIN
SELECT Count(*)
FROM table1 t1
INNER JOIN table2 t2 ON t2.nkey = t1.nkey
INNER JOIN table3 t3 ON t3.ndependency = t1.ndependency
--ORDER BY t3.nkey ASC
;

SELECT Count(*)
FROM table3 t3
INNER JOIN table2 t2 ON t2.ndependency =t3.ndependency
;

SELECT *
FROM table1 t1
INNER JOIN table2 t2 ON t2.ndependency = t1.ndependency
ORDER BY t1.nkey ASC
;

EXPLAIN
WITH cte AS (
  SELECT t1.nkey as n1key, t1.ndependency as n1dependency , t2.nkey, t2.ndependency FROM table1 t1
  INNER JOIN table2 t2 ON t1.nkey = t2.nkey
)
SELECT * FROM cte
INNER JOIN table3 t3 ON t3.ndependency = cte.n1dependency;
