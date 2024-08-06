
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
