ANALYZE dummytable;


/*1. Multiple filter conditions*/



--b. check two where cases without FD
EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE normal_dist =0 AND poisson_dist = 18;

EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE poisson_dist =0 AND exponential_dist = 12;

--b. check two where cases with FD
EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE normal_dist =0 AND modulo = 2;

EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE normal_dist =10 AND modulo = 2;

EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE normal_dist =10 AND modulo = 0;


EXPLAIN ANALYZE SELECT * FROM dummytable
WHERE poisson_dist =10 AND modulo = 0;