ANALYZE dummytable;


/*1. Multiple filter conditions*/

--a. check no where cases without ExtStat
EXPLAIN ANALYSE SELECT * FROM dummytable;


--b. check one where case  without ExtStat
EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE normal_dist =0;

EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE poisson_dist =0;


EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE dummytable.exponential_dist =0;

EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE dummytable.uniform_dist =0;

EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE dummytable.random_dist =0;

--с. check one where case with ExtStat
EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE dummytable.modulo =0;

EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE dummytable.modulo =11;