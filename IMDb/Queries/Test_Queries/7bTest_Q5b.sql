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

VACUUM "JoinOrderBenchmark".public.movie_companies;


EXPLAIN ANALYSE
SELECT *
FROM movie_companies mc
WHERE  mc.note LIKE '%(VHS)%'
  AND mc.note LIKE '%(USA)%'
  AND mc.note LIKE '%(1994)%';

DROP INDEX idx_mc_partial_note;

ALTER TABLE movie_companies ALTER COLUMN note SET STATISTICS  6000;
ALTER TABLE movie_companies ALTER COLUMN note SET STATISTICS  -1;
SET default_statistics_target = 6000;
SET default_statistics_target =100;
ANALYSE movie_companies;


