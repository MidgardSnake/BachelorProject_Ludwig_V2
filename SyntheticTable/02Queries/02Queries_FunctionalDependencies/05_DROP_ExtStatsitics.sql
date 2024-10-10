

DROP STATISTICS modulo_dependency;


ANALYSE synthetictable;

SELECT stxname, stxkeys,stxddependencies
FROM pg_statistic_ext
JOIN pg_statistic_ext_data ON (oid = pg_statistic_ext_data.stxoid)
WHERE stxname = 'modulo_dependency';