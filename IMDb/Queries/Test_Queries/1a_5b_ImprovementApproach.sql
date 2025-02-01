/*0ß Check statistic target*/
show default_statistics_target;

SET default_statistics_target = 100;


/*0ß Check active indices*/
SELECT
    tablename AS table_name,
    indexname AS index_name,
    indexdef AS index_definition
FROM
    pg_indexes
WHERE
    tablename IN ('company_type', 'info_type', 'movie_companies', 'movie_info', 'title');


/*01 Queryplan in general*/
EXPLAIN ANALYZE

SELECT MIN(t.title) AS american_vhs_movie
FROM company_type AS ct,
     info_type AS it,
     movie_companies AS mc,
     movie_info AS mi,
     title AS t
WHERE ct.kind = 'production companies'
  AND mc.note LIKE '%(VHS)%'
  AND mc.note LIKE '%(USA)%'
  AND mc.note LIKE '%(1994)%'
  AND mi.info IN ('USA',
                  'America')
  AND t.production_year > 2010
  AND t.id = mi.movie_id
  AND t.id = mc.movie_id
  AND mc.movie_id = mi.movie_id
  AND ct.id = mc.company_type_id
  AND it.id = mi.info_type_id;

/*02 actual Query*/
SELECT Count(*)
FROM movie_companies mc
WHERE mc.note LIKE '%(VHS)%'
  AND mc.note LIKE '%(USA)%'
  AND mc.note LIKE '%(1994)%';

/*03 estimated Queryplan*/
EXPLAIN  ANALYZE SELECT *--Count(*)
FROM movie_companies mc
WHERE mc.note LIKE '%(VHS)%'
  AND mc.note LIKE '%(USA)%'
  AND mc.note LIKE '%(1994)%';

/*04 create index on wildcards*/
CREATE INDEX idx_mc_partial_note ON movie_companies (note)
WHERE note LIKE '%(VHS)%' AND note LIKE '%(USA)%' AND note LIKE '%(1994)%';

DROP INDEX idx_mc_partial_note;

/*05 enhance statistics on movie_companies*/
ALTER TABLE movie_companies ALTER COLUMN note SET STATISTICS 6000;
ALTER TABLE movie_companies ALTER COLUMN note SET STATISTICS -1;

ANALYZE movie_companies;



/*Step2 movie_info*/
SELECT Count(*)
FROM movie_info mi
WHERE mi.info IN ('USA','America');

EXPLAIN ANALYSE
SELECT *
FROM movie_info mi
WHERE mi.info IN ('USA','America');


SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'movie_info';

ALTER TABLE movie_info ALTER COLUMN note SET STATISTICS 10000;
ANALYZE movie_info;

-- BAD Erstelle eine multivariate Statistik für die Tabellen movie_info und movie_companies
CREATE STATISTICS movie_info_mc_stats (dependencies)
ON movie_id, info
FROM movie_info;

CREATE STATISTICS movie_companies_mc_stats (dependencies)
ON movie_id, company_type_id
FROM movie_companies;

CREATE INDEX idx_movie_info_hash ON movie_info (md5(movie_id::text));

CREATE INDEX idx_movie_companies_movie_id_note ON movie_companies (movie_id, note);

DROP INDEX idx_movie_companies_movie_id_note;
DROP STATISTICS movie_companies_mc_stats;


ANALYZE movie_info;
ANALYZE movie_companies;

SELECT MIN(t.title)
FROM title t,
     movie_info mi ,
     movie_companies mc


WHERE mi.info  IN ('USA','America')
AND mc.note LIKE '%(VHS)%'
  AND mc.note LIKE '%(USA)%'
  AND mc.note LIKE '%(1994)%'
AND mc.movie_id = mi.movie_id
  --AND t.production_year > 2010
  AND t.id = mi.movie_id
  AND t.id = mc.movie_id
;

    ;





