ANALYZE synthetictable;



SELECT Count(*)
    FROM synthetictable;
/*1. Multiple filter conditions*/



--b. check two where cases without FD
EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE exponential_dist =140 AND modulo = 0;





SELECT Count(*)
FROM synthetictable
WHERE modulo = 0 ;




SELECT *
FROM pg_stats
WHERE tablename = 'synthetictable' and attname IN ('normal_dist','modulo') ;

