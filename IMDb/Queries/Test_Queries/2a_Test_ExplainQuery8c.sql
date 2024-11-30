/*00 check statistics*/
SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'cast_info';

/*01 enhance statistics*/
SET default_statistics_target = 10000;
RESET default_statistics_target ;


CREATE INDEX idx_cast_info_person_movie_role ON cast_info (person_id, movie_id, role_id);
CREATE INDEX idx_company_name_country_code ON company_name (country_code);
CREATE INDEX idx_role_type_role ON role_type (role);
CREATE INDEX idx_movie_companies_movie_company ON movie_companies (movie_id, company_id);
CREATE INDEX idx_aka_name_person_id ON aka_name (person_id);

DROP INDEX idx_cast_info_person_movie_role;
DROP INDEX idx_company_name_country_code;
DROP INDEX idx_role_type_role;
DROP INDEX idx_movie_companies_movie_company;
DROP INDEX idx_aka_name_person_id;


SET max_parallel_workers_per_gather = 1;
RESET max_parallel_workers_per_gather;

ANALYSE ;


EXPLAIN (ANALYZE,BUFFERS) SELECT MIN(a1.name) AS writer_pseudo_name,
       MIN(t.title) AS movie_title
FROM aka_name AS a1,
     cast_info AS ci,
     company_name AS cn,
     movie_companies AS mc,
     name AS n1,
     role_type AS rt,
     title AS t
WHERE cn.country_code ='[us]'
  AND rt.role ='writer'
  AND a1.person_id = n1.id
  AND n1.id = ci.person_id
  AND ci.movie_id = t.id
  AND t.id = mc.movie_id
  AND mc.company_id = cn.id
  AND ci.role_id = rt.id
  AND a1.person_id = ci.person_id
  AND ci.movie_id = mc.movie_id;



EXPLAIN ANALYZE SELECT *
FROM cast_info as ci ,role_type AS rt
WHERE ci.role_id = rt.id
;

EXPLAIN ANALYZE SELECT *
FROM role_type AS rt
WHERE rt.role ='writer'
;


