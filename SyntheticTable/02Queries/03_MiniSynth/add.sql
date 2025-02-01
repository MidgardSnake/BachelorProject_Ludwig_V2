DELETE FROM SyntheticTablemini;


-- Emma Watson: 10 Zeilen aktualisieren
UPDATE synthetictable_actors
SET name = 'Emma Watson', birthyear = CASE id
    WHEN 1 THEN 1990
    WHEN 2 THEN 1991
    WHEN 3 THEN 1992
    WHEN 4 THEN 1993
    WHEN 5 THEN 1994
    WHEN 6 THEN 1995
    WHEN 7 THEN 1996
    WHEN 8 THEN 1997
    WHEN 9 THEN 1998
    WHEN 10 THEN 1999
    END
WHERE id IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

-- Johnny Depp: 4 Zeilen aktualisieren
UPDATE synthetictable_actors
SET name = 'Johnny Depp', birthyear = CASE id
    WHEN 11 THEN 1963
    WHEN 12 THEN 1964
    WHEN 13 THEN 1965
    WHEN 14 THEN 1966
    END
WHERE id IN (11, 12, 13, 14);

-- Elijah Wood: 3 Zeilen aktualisieren
UPDATE synthetictable_actors
SET name = 'Elijah Wood', birthyear = CASE id
    WHEN 15 THEN 1981
    WHEN 16 THEN 1982
    WHEN 17 THEN 1983
    END
WHERE id IN (15, 16, 17);



SET default_statistics_target = 100;


SELECT Count(*)
FROM synthetictable_actors
--WHERE  name = '12Gn'
;


SELECT Count(*)
FROM synthetictable_actors;


SET default_statistics_target = 100;
ANALYSE synthetictable_actors;

EXPLAIN ANALYSE VERBOSE SELECT *
FROM synthetictable_actors
WHERE name LIKE '12G%';


SELECT *
FROM pg_stats
--WHERE relname = 'pg_stats'
;


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


SELECT  name , count(*) counter
FROM synthetictable_actors
group by name

ORDER BY counter DESC
FETCH FIRST 3 ROWS ONLY;


EXPLAIN ( ANALYZE , BUFFERS )
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
