/*Fourth get Statistics for each table*/


SELECT *
FROM pg_stats;

VACUUM FULL ANALYSE ;

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds

       ,correlation
FROM pg_stats
WHERE tablename = 'aka_name'
;
-- id
-- n_distinct = -1 ; mcv = null , mcf = null, correlation = 0.99999887
-- hist = {69,9052,.... 901272}


SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'aka_title'
; -- relpages = 6192 ; reltuples = 361.472


SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'cast_info'
; --!!!relpages = 252.654 ; reltuples = 36.223.048 <> 36.244.344


SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'char_name'
; -- !!!relpages = 36447; reltuples = 3.140.447 <> 3.140.339

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'comp_cast_type'
; --relpages = 1; reltuples = 4

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'company_name'
; --relpages = 2995; reltuples = 234.997 = 234.997

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =   'company_type'
; --relpages = 1; reltuples = 4

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =   'complete_cast'
; --relpages = 731; reltuples = 135.086<>134.086

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename = 'info_type'
; --relpages = 1; reltuples = 113

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename = 'keyword'
; --relpages = 949; reltuples = 134170

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'kind_type' ; -- 7

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename = 'link_type' ; -- 18

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =   'movie_companies'
; --relpages = 18.789; reltuples = 2.609.129 = 2.609.129

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'movie_info'
; --relpages =161.521; reltuples = 14.873.344 <> 14.835.720


SELECT *--attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'movie_info_idx';
--relpages =7935; reltuples = 1.380.035 = 1.380.035

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'movie_keyword'
; --relpages =24.454; reltuples = 4.523.930 = 4.523.930

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename = 'movie_link'
; --relpages =163; reltuples = 29.997

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'name'
; --relpages =55.614; reltuples =4.167.454 <> 4.167.491


SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename = 'person_info';
--relpages =50.923; reltuples = 2.964.713 <> 2.963.664

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename =  'role_type' ; --12

SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename  = 'title'
; --relpages =35.998; reltuples =2.528.560 <> 2.528.312



SELECT table_name
FROM information_schema.tables;