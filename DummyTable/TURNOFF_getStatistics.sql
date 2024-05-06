VACUUM FULL ANALYZE;


ALTER SYSTEM SET autovacuum = off; -- autovacuum ausschalten
ALTER SYSTEM SET autovacuum_analyze_threshold = 1000000;
ALTER SYSTEM SET autovacuum_analyze_scale_factor = 0;

SELECT pg_reload_conf(); -- umsetzung bestätigen lassen


EXPLAIN ANALYSE
       SELECT normal_distribution

       FROM "DummyTable"

       WHERE normal_distribution between -250 and 250;

