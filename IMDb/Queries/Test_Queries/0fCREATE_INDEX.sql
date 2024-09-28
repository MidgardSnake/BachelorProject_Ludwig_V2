SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'company_name';

SELECT name, Count(*) counter
FROM company_name
GROUP BY name
ORDER by counter desc;

----------Change Factory ---------

--CREATE INDEX idx_company_name__name ON  company_name(name);
DROP INDEX idx_company_name__name ;

ALTER TABLE company_name ALTER COLUMN name SET STATISTICS 800;


ANALYZE company_name;


EXPLAIN ANALYZE --6
SELECT name, id
FROM company_name
WHERE name = 'Victoria Film';

EXPLAIN ANALYZE --52
SELECT name, id
FROM company_name
WHERE name = 'Universal Pictures International (UPI)'
;




ALTER TABLE title ALTER COLUMN title SET STATISTICS 100;





EXPLAIN ANALYSE SELECT * FROM name WHERE name = 'Smith, David';

SELECT name, count(*) counter
FROM name
Group by name
order by counter desc;


-- Falsche Join Reihenfolge (zuerst werden große Tabellen gejoined
EXPLAIN ANALYSE
SELECT t.title, t.production_year
FROM aka_name n
JOIN cast_info ci ON n.id = ci.person_id
JOIN title t ON ci.movie_id = t.id
WHERE n.name = 'Billy';

EXPLAIN ANALYSE
SELECT t.title, t.production_year
FROM aka_name n
JOIN cast_info ci ON n.id = ci.person_id
JOIN title t ON ci.movie_id = t.id
WHERE n.name = 'Sylvika';







