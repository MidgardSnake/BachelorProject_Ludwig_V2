

ALTER TABLE synthetictable ALTER COLUMN linear_dist  SET STATISTICS 101;

ANALYSE synthetictable;

EXPLAIN (ANALYZE) SELECT *
FROM synthetictable
WHERE linear_dist = 42;


