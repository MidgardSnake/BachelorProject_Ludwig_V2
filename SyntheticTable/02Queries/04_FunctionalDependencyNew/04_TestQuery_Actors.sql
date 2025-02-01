

-- PyhthonClass 12 liefert hier eine gute Tabelle für die Intro


--@Pages und Cardinality der gesamten Tabelle
SELECT reltuples, relpages
FROM pg_class
WHERE relname = 'synthetictable_actors';



CREATE INDEX idx_birthyear ON synthetictable_actors (birthyear);

ANALYZE synthetictable_actors;

DROP INDEX idx_birthyear;

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

------------------------------------------------------------------------

-- bitmap cost = 316  vs indexscan 1074 vs seqscan 505 --> seqscan
-- idx = 1074   vs seq = 505 --> seq
EXPLAIN (ANALYZE, BUFFERS) SELECT  name -- mcv platz 1--> Seq Scan? --> cardinality 2436
FROM synthetictable_actors
WHERE birthyear = (1987)
;


EXPLAIN (ANALYZE, BUFFERS) SELECT  name  --mcv platz 100
FROM synthetictable_actors
WHERE birthyear = 1924
;

EXPLAIN (ANALYZE, BUFFERS) SELECT  name  --mcv platz 101
FROM synthetictable_actors
WHERE birthyear = 1977
;


-- idx 48.50 -- seq 93.5
EXPLAIN (ANALYZE, BUFFERS) SELECT  name -- not mcv platz 150 Index Scan vermutet --> cardinality 42
FROM synthetictable_actors
WHERE birthyear = 2028
;


--bitmap cost 122 vs index scan 173 vs seqscan 505
-- idx 169
EXPLAIN SELECT   name -- not mcv platz 200 Index Scan vermutet --> cardinality 1
FROM synthetictable_actors
WHERE birthyear = 2032
;


SET enable_bitmapscan =off;
SET enable_indexscan =on;
SET enable_seqscan =off;



ALTER TABLE synthetictable_actors ALTER COLUMN birthyear SET STATISTICS 101;

ALTER TABLE synthetictable_actors ALTER COLUMN birthyear SET STATISTICS -1;

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



SHOW RANDOM_PAGE_COST ;
SHOW seq_page_cost ;

SELECT pg_size_pretty(pg_total_relation_size('SyntheticTable_Actors'));












