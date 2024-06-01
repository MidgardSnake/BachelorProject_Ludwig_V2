
--get data about database_cluster OIDs (Object identifiers)
SELECT * FROM pg_database;

--get data about database_cluster OIDs (Object identifiers)
SELECT relname, oid , relfilenode FROM pg_class ORDER BY oid desc;



-- oid und relfilenode sind oft gleich, falls nicht, dann TRUNCATE um relfilenode zurückzusetzen
SELECT relname, oid, relfilenode FROM pg_class WHERE relname = 'pg_views';
