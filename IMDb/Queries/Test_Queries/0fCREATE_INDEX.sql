
EXPLAIN ANALYSE
SELECT n.name, Count(*) as counter--n.name, n.id
FROM name AS n
Group by n.name
order by counter desc
;


EXPLAIN ANALYSE
SELECT  n.name
FROM name AS n

WHERE n.name = 'Depp, Johnny'
;

