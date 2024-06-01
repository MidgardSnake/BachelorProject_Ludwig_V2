VACUUM FULL ANALYZE;

ALTER SYSTEM SET autovacuum = on; -- Statistiken wieder an schalten
ALTER SYSTEM SET autovacuum_analyze_threshold = 50;
ALTER SYSTEM SET autovacuum_analyze_scale_factor = 0.1;

-- Änderungen laden
SELECT pg_reload_conf();

EXPLAIN ANALYSE
    SELECT normal_distribution

    FROM "DummyTable"

    WHERE normal_distribution between -250 and 250;