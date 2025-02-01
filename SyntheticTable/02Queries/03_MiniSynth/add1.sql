

/*Possibility ONE to extend statistcs for amount of MCV and MCF*/
ALTER TABLE synthetictable_actors ALTER COLUMN birthyear  SET STATISTICS 102;

/*Possibility TWO to extend statistcs for amount of MCV and MCF*/
SET default_statistics_target = 101;
ANALYSE synthetictable_actors;


SELECT attname,
       null_frac,
       n_distinct,
       most_common_vals,
       most_common_freqs,
       histogram_bounds,
       correlation
FROM pg_stats
WHERE tablename = 'synthetictable_actors';


SELECT  birthyear , count(*) counter
FROM synthetictable_actors
group by birthyear

ORDER BY counter DESC
FETCH FIRST 201 ROWS ONLY;


EXPLAIN ( ANALYZE  )
SELECT name
FROM synthetictable_actors
WHERE birthyear = 1977;

ANALYSE synthetictable_actors;

EXPLAIN SELECT * FROM Synthetictable_actors WHERE name = 'Emma Watson' OR name = 'Johnny Depp';

EXPLAIN ANALYZE SELECT * FROM Synthetictable_actors WHERE birthyear <= 1940;

EXPLAIN SELECT * FROM Synthetictable_actors WHERE birthyear > 2000;



SELECT birthyear ,Count(*) counter
FROM Synthetictable_actors
GROUP BY birthyear
ORDER BY counter DESC

--FETCH FIRST 201 ROWS ONLY
;



SELECT birthyear, Count(*) counter
FROM synthetictable_actors
WHERE birthyear < 2000
GROUP BY birthyear
ORDER BY counter DESC

;


EXPLAIN ANALYZE
SELECT id
FROM synthetictable_actors
WHERE birthyear > 2000 and id < 3000 ;


SELECT birthyear , Count(*) counter
FROM synthetictable_actors
GROUP BY birthyear
ORDER BY counter DESC;
