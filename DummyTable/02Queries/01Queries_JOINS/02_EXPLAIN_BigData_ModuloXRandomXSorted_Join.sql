ANALYZE table1;
ANALYZE table2;
ANALYZE table3;

/* Gib zuerst den allgemeinen Queryplan für alle Tabellen an*/
EXPLAIN
SELECT *
FROM table3 t3
INNER JOIN table1 t1 ON t1.nkey = t3.nkey
INNER JOIN table2 t2 ON t2.nkey = t1.nkey;

/* Gib den  Queryplan für alle Tabellen an, wobei t1 mit t2 über distinct gejoined wird*/
EXPLAIN
SELECT *
FROM table3 t3
INNER JOIN table1 t1 ON t1.nkey = t3.nkey
INNER JOIN table2 t2 ON t2.ndependency = t1.ndependency;


/* Gib den  Queryplan für alle Tabellen an, wobei t1 mit t3 über distinct gejoined wird*/
EXPLAIN
SELECT *
FROM table3 t3
INNER JOIN table1 t1 ON t1.ndependency = t3.ndependency
INNER JOIN table2 t2 ON t2.nkey = t1.nkey;


/* Gib den  Queryplan für alle Tabellen an, wobei t2 mit t3 über distinct gejoined wird*/
EXPLAIN
SELECT *
FROM table3 t3
INNER JOIN table1 t1 ON t1.nkey = t3.nkey
INNER JOIN table2 t2 ON t2.ndependency = t3.ndependency;


/* Gib mir einen einfachen Output aus*/

EXPLAIN
SELECT *
FROM table1 t1
LEFT JOIN table2 t2 ON t2.nkey = t1.nkey
--RIGHT JOIN table3 t3 ON t3.ndependency = t1.ndependency

--ORDER BY t3.nkey ASC
;

SELECT *
FROM table3 t3

ORDER BY ndependency DESC
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
