

CREATE STATISTICS modulo_dependency (dependencies )
ON modulo, exponential_dist
FROM synthetictable;

ANALYSE synthetictable;

EXPLAIN ANALYZE SELECT * FROM synthetictable
WHERE exponential_dist =140 AND modulo = 0;

SELECT stxname, stxkeys,stxddependencies
FROM pg_statistic_ext
JOIN pg_statistic_ext_data ON (oid = pg_statistic_ext_data.stxoid)
WHERE stxname = 'modulo_dependency';