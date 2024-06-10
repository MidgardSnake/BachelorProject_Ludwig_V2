

CREATE STATISTICS modulo_dependency (dependencies )
ON modulo, normal_dist
FROM dummytable;

ANALYSE dummytable;

SELECT stxname, stxkeys,stxddependencies
FROM pg_statistic_ext
JOIN pg_statistic_ext_data ON (oid = pg_statistic_ext_data.stxoid)
WHERE stxname = 'modulo_dependency';