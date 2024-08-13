
-------------------------------------------------------
--1. Default Statistiken anschauen
SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =   'movie_companies';

--2. welche Schätzungen rows?  13372 vs 28889
EXPLAIN ANALYSE SELECT *
FROM movie_companies
WHERE note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%' AND (note LIKE '%(co-production)%' OR note LIKE '%(presents)%');


-- 3. DEFAULT Statistics target checken (=100)
SHOW default_statistics_target;


-- 4. Anpassen auf DISTINCT VALUE
ALTER DATABASE "JoinOrderBenchmark" SET default_statistics_target = 5883;

ANALYSE "JoinOrderBenchmark".public.movie_companies ;

--!!!!Unbedingt die Datenbankverbindung trennen, damit Änderungen gesetzt sind .. detach session und dann neu connecten!!
-- 5. DEFAULT Statistics target checken (=5883)
SHOW default_statistics_target;

--6. Erneut Kardinalität checken
EXPLAIN ANALYSE SELECT *
FROM movie_companies
WHERE note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%' AND (note LIKE '%(co-production)%' OR note LIKE '%(presents)%');


-- 7. Reseten
ALTER DATABASE "JoinOrderBenchmark" RESET default_statistics_target;
ANALYSE "JoinOrderBenchmark".public.movie_companies ;

-- 8. DEFAULT Statistics target checken (=100)
SHOW default_statistics_target;
-------------------------------------------Übertrag auf 1a


--1.
SHOW default_statistics_target;

EXPLAIN ANALYZE SELECT MIN(mc.note) AS production_note,
       MIN(t.title) AS movie_title,
       MIN(t.production_year) AS movie_year
FROM company_type AS ct,
     info_type AS it,
     movie_companies AS mc,
     movie_info_idx AS mi_idx,
     title AS t
WHERE ct.kind = 'production companies'
  AND it.info = 'top 250 rank'
  AND mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'
  AND (mc.note LIKE '%(co-production)%'
       OR mc.note LIKE '%(presents)%')
  AND ct.id = mc.company_type_id
  AND t.id = mc.movie_id
  AND t.id = mi_idx.movie_id
  AND mc.movie_id = mi_idx.movie_id
  AND it.id = mi_idx.info_type_id;


ALTER DATABASE "JoinOrderBenchmark" SET default_statistics_target = 5000;
ANALYSE "JoinOrderBenchmark".public.movie_companies ;
--reconnect to Database, detach session
SHOW default_statistics_target;

EXPLAIN ANALYZE SELECT MIN(mc.note) AS production_note,
       MIN(t.title) AS movie_title,
       MIN(t.production_year) AS movie_year
FROM company_type AS ct,
     info_type AS it,
     movie_companies AS mc,
     movie_info_idx AS mi_idx,
     title AS t
WHERE ct.kind = 'production companies'
  AND it.info = 'top 250 rank'
  AND mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'
  AND (mc.note LIKE '%(co-production)%'
       OR mc.note LIKE '%(presents)%')
  AND ct.id = mc.company_type_id
  AND t.id = mc.movie_id
  AND t.id = mi_idx.movie_id
  AND mc.movie_id = mi_idx.movie_id
  AND it.id = mi_idx.info_type_id;

ALTER DATABASE "JoinOrderBenchmark" RESET default_statistics_target ;
ANALYSE "JoinOrderBenchmark".public.movie_companies ;
--reconnect to Database, detach session
SHOW default_statistics_target;