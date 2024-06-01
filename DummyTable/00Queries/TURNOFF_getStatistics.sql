VACUUM FULL ANALYZE;


ALTER SYSTEM SET autovacuum = off; -- autovacuum ausschalten
--ALTER SYSTEM SET autovacuum_analyze_threshold = 1000000;
--ALTER SYSTEM SET autovacuum_analyze_scale_factor = 0;

--SELECT pg_reload_conf(); -- umsetzung bestätigen lassen

SELECT
    *
    --relpages, reltuples
    --correlation
FROM pg_stats
WHERE tablename = 'DummyTable' AND attname = 'normal_distribution';


SELECT * FROM 'DummyTable';


