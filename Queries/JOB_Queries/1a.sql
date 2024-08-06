
SELECT MIN(mc.note) AS production_note,
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

---------------------------------------------------
EXPLAIN SELECT MIN(mc.note) AS production_note,
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
---------------------------------------------------
--wieviele null werte für note?
EXPLAIN ANALYZE SELECT *
FROM movie_companies
WHERE note  LIKE '%(as Metro-Goldwyn-Mayer Pictures)%' OR note  NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%' ;

EXPLAIN ANALYSE SELECT *
    FROM movie_companies
        WHERE note LIKE '%(co-production)%';

--wieviele werte für not like Metro?
EXPLAIN ANALYSE SELECT *
FROM movie_companies
WHERE note LIKE '%(presents)%';
;



EXPLAIN ANALYSE SELECT *
FROM movie_companies
WHERE note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%' AND (note LIKE '%(co-production)%' OR note LIKE '%(presents)%');

SELECT Count(*)
FROM movie_companies
WHERE note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%' AND (note LIKE '%(co-production)%'OR note LIKE '%(presents)%');
;

EXPLAIN ANALYZE SELECT *
FROM movie_companies
WHERE note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%' AND (note LIKE '%(co-production)%'OR note LIKE '%(presents)%')
AND note is not null
;

CREATE STATISTICS mcv_stats_Q1a ON note FROM movie_companies;
ANALYZE movie_companies;

