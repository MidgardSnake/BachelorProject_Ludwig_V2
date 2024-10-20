

ALTER TABLE synthetictable ALTER COLUMN exponential_dist  SET STATISTICS 101;

ANALYSE synthetictable;

EXPLAIN (ANALYZE) SELECT *
FROM synthetictable
WHERE exponential_dist = 42;


