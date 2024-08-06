/*Third Queries: getCardinality for each Table after ANALYZE*/
SELECT *
FROM pg_class;

VACUUM FULL ANALYSE ;

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'aka_name'
; -- relpages = 11.396 ; reltuples = 901.343


SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname =  'aka_title'
; -- relpages = 6192 ; reltuples = 361.472


SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'cast_info'
; --!!!relpages = 252.654 ; reltuples = 36.223.048 <> 36.244.344


SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname =  'char_name'
; -- !!!relpages = 36447; reltuples = 3.140.447 <> 3.140.339

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname =  'comp_cast_type'
; --relpages = 1; reltuples = 4

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname =  'company_name'
; --relpages = 2995; reltuples = 234.997 = 234.997

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname =  'company_type'
; --relpages = 1; reltuples = 4

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname =  'complete_cast'
; --relpages = 731; reltuples = 135.086<>134.086

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'info_type'
; --relpages = 1; reltuples = 113

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname ='keyword'
; --relpages = 949; reltuples = 134170

SELECT Count(*)
FROM kind_type ; -- 7

SELECT Count(*)
FROM link_type ; -- 18

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname =  'movie_companies'
; --relpages = 18.789; reltuples = 2.609.129 = 2.609.129

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'movie_info'
; --relpages =161.521; reltuples = 14.873.344 <> 14.835.720


SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'movie_info_idx';
--relpages =7935; reltuples = 1.380.035 = 1.380.035

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'movie_keyword'
; --relpages =24.454; reltuples = 4.523.930 = 4.523.930

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'movie_link'
; --relpages =163; reltuples = 29.997

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'name'
; --relpages =55.614; reltuples =4.167.454 <> 4.167.491


SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'person_info';
--relpages =50.923; reltuples = 2.964.713 <> 2.963.664

SELECT Count(*)
FROM role_type ; --12

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'title'
; --relpages =35.998; reltuples =2.528.560 <> 2.528.312

EXPLAIN SELECT * FROM title;


SELECT table_name
FROM information_schema.tables;