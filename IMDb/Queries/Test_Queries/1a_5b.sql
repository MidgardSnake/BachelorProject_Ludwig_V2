show default_statistics_target;

SET default_statistics_target = 100;

--Queryplan
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


EXPLAIN ANALYSE SELECT Count(*)
FROM movie_companies mc
WHERE mc.note LIKE '%(VHS)%'
  AND mc.note LIKE '%(USA)%'
  AND mc.note LIKE '%(1994)%';

CREATE INDEX idx_mc_partial_note ON movie_companies (note)
WHERE note LIKE '%(VHS)%' AND note LIKE '%(USA)%' AND note LIKE '%(1994)%';
ALTER TABLE movie_companies ALTER COLUMN note SET STATISTICS 100;
ALTER TABLE movie_companies ALTER COLUMN note SET STATISTICS -1;

ANALYZE movie_companies;



--Statistics movie_companies

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =   'movie_companies'
; --> most common vals sind für note inakkurat

CREATE INDEX mov_comp_notes ON movie_companies (note);
DROP INDEX mov_comp_notes;
CREATE INDEX idx_mc_note_movie_id ON movie_companies (note, movie_id);
DROP INDEX idx_mc_note_movie_id;
CREATE INDEX idx_mc_note_vhs_usa_1994 ON movie_companies ((note LIKE '%(VHS)%'::text), (note LIKE '%(USA)%'::text), (note LIKE '%(1994)%'::text));
DROP INDEX idx_mc_note_vhs_usa_1994;


ALTER TABLE movie_companies ALTER COLUMN note SET STATISTICS 100;
ALTER TABLE title ALTER COLUMN production_year SET STATISTICS 100;

ANALYZE movie_companies;

DROP INDEX mov_comp_notes;

