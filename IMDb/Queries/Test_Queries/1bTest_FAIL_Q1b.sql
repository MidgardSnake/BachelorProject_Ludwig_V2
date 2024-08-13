EXPLAIN ANALYZE SELECT *
FROM info_type i, movie_info_idx m
WHERE i.id = m.info_type_id
AND i.info = 'bottom 10 rank' ;

EXPLAIN ANALYZE SELECT *
FROM title t
WHERE t.production_year BETWEEN 2005 AND 2010;

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'movie_info_idx';

SET default_statistics_target = 100;
ANALYSE movie_info_idx;
--Datenbank danach nochmal zurücksetzen

SHOW default_statistics_target ;
RESET default_statistics_target ;

--SHOW all;


EXPLAIN ANALYZE SELECT *
FROM info_type i, movie_info_idx m
WHERE i.id = m.info_type_id
AND i.info = 'bottom 10 rank' ;


RESET default_statistics_target ;
SHOW default_statistics_target ;

EXPLAIN ANALYZE SELECT *
FROM info_type i, movie_info_idx m
WHERE i.id = m.info_type_id
AND i.info = 'bottom 10 rank' ;

-------------------------------Ausführung 1b
show all ;


Explain ANALYSE SELECT MIN(mc.note) AS production_note,
       MIN(t.title) AS movie_title,
       MIN(t.production_year) AS movie_year
FROM company_type AS ct,
     info_type AS it,
     movie_companies AS mc,
     movie_info_idx AS mi_idx,
     title AS t
WHERE ct.kind = 'production companies'
  AND it.info = 'bottom 10 rank'
  AND mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'
  AND t.production_year BETWEEN 2005 AND 2010
  AND ct.id = mc.company_type_id
  AND t.id = mc.movie_id
  AND t.id = mi_idx.movie_id
  AND mc.movie_id = mi_idx.movie_id
  AND it.id = mi_idx.info_type_id;



-- Erweiterte Statistik
CREATE STATISTICS stats_movie_info_type_dependency (dependencies)
ON info_type_id, movie_id
FROM movie_info_idx;

ANALYZE movie_info_idx;



Explain ANALYSE SELECT MIN(mc.note) AS production_note,
       MIN(t.title) AS movie_title,
       MIN(t.production_year) AS movie_year
FROM company_type AS ct,
     info_type AS it,
     movie_companies AS mc,
     movie_info_idx AS mi_idx,
     title AS t
WHERE ct.kind = 'production companies'
  AND it.info = 'bottom 10 rank'
  AND mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'
  AND t.production_year BETWEEN 2005 AND 2010
  AND ct.id = mc.company_type_id
  AND t.id = mc.movie_id
  AND t.id = mi_idx.movie_id
  AND mc.movie_id = mi_idx.movie_id
  AND it.id = mi_idx.info_type_id;

DROP STATISTICS stats_movie_info_type_dependency;



ANALYZE movie_info_idx;










