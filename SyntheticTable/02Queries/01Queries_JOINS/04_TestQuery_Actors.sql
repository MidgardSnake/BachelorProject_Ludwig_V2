ANALYZE synthetictable_actors;

CREATE INDEX idx_name ON synthetictable_actors (name);
CREATE INDEX idx_birthyear ON synthetictable_actors (birthyear);
ANALYZE synthetictable_actors;
CREATE INDEX idx_id ON synthetictable_actors (id);

DROP INDEX idx_birthyear;
DROP INDEX idx_name;
DROP INDEX idx_id;

--@ vorhandene Indexe checken
SELECT
    indexname,
    indexdef
FROM
    pg_indexes
WHERE
    tablename = 'synthetictable_actors';






------------------------------------------------------------------------
SELECT Count(*)
FROM synthetictable_actors;

SELECT n_distinct, most_common_vals, most_common_freqs
FROM pg_stats
WHERE tablename= 'synthetictable_actors'
ORDER BY most_common_freqs DESC
;
------------------------------------------------------------------------

SELECT birthyear  ,Count(*) as Counter
FROM synthetictable_actors
GROUP BY birthyear
ORDER BY counter desc
;


SELECT SUM(counter)
FROM (
SELECT birthyear  ,Count(*) as Counter
FROM synthetictable_actors
GROUP BY birthyear
ORDER BY counter desc)
WHERE counter =1
;


------------------------------------------------------------------------

-- bitmap cost = 316  vs indexscan 1074 vs seqscan 505 --> seqscan
-- idx = 1074   vs seq = 505 --> seq
EXPLAIN  SELECT  name -- mcv platz 1--> Seq Scan? --> cardinality 2436
FROM synthetictable_actors
WHERE birthyear = (2053)
;

-- bitmap cost 122 vs index scan 173 vs seqscan 505 --341 idx
--idx 341.95 vs seq 505
--idx 76.71  vs seq 93.50
EXPLAIN (ANALYZE, BUFFERS) SELECT  name  --mcv platz 101
FROM synthetictable_actors
WHERE birthyear = 2041
;


-- idx 48.50 -- seq 93.5
EXPLAIN (ANALYZE, BUFFERS) SELECT  name -- not mcv platz 150 Index Scan vermutet --> cardinality 42
FROM synthetictable_actors
WHERE birthyear = 1923
;

--bitmap cost 122 vs index scan 173 vs seqscan 505
-- idx 169
EXPLAIN SELECT  name -- not mcv platz 176 Index Scan vermutet --> cardinality 42
FROM synthetictable_actors
WHERE birthyear = 1906
;

--bitmap cost 122 vs index scan 173 vs seqscan 505
-- idx 169
EXPLAIN SELECT   name -- not mcv platz 200 Index Scan vermutet --> cardinality 1
FROM synthetictable_actors
WHERE birthyear = 1959
;


SET enable_bitmapscan =off;
SET enable_indexscan =on;
SET enable_seqscan =off;



ALTER TABLE synthetictable_actors ALTER COLUMN birthyear SET STATISTICS 102;
ANALYSE synthetictable_actors;

SHOW default_statistics_target ;

ANALYSE synthetictable_actors;

SELECT name, setting
FROM pg_settings
WHERE name LIKE 'enable_seq%' OR  name LIKE 'enable_ind%' OR  name LIKE 'enable_bit%';

SELECT n_distinct, most_common_vals, most_common_freqs
FROM pg_stats
WHERE tablename= 'synthetictable_actors'
ORDER BY most_common_freqs DESC
;

--@Pages und Cardinality der gesamten Tabelle
SELECT reltuples, relpages
FROM pg_class
WHERE relname = 'synthetictable_actors';

--@Pages für mcv 102
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM SyntheticTable_Actors WHERE birthyear = 2085;

EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM SyntheticTable_Actors WHERE birthyear = 1969;











