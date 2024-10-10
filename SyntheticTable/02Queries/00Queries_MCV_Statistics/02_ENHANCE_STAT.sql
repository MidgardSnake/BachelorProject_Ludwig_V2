

ALTER TABLE synthetictable ALTER COLUMN normal_dist  SET STATISTICS 101;

ANALYSE synthetictable;

EXPLAIN (ANALYZE,BUFFERS) SELECT *
FROM synthetictable
WHERE normal_dist = 359;-- falsch 13 vs 29


