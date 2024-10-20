/*Second Queries: estimated cardinality for each Table*/
SELECT *
FROM pg_class;

SELECT oid, relname, relpages, reltuples
FROM pg_class
WHERE relname in ('aka_name','aka_title')
; -- relpages = 11.396 ; reltuples = 901.343


SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname =  'aka_title'
; -- relpages = 6192 ; reltuples = 361.472

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'cast_info'
; --!!!relpages = 252.654 ; reltuples = 36.241.600 <> 36.244.344

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname =  'char_name'
; -- !!!relpages = 36447; reltuples = 3.140.377 <> 3.140.339

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
WHERE relname =  'complete_cast' ; --134.086

SELECT Count(*)
FROM info_type ; -- 113

SELECT Count(*)
FROM keyword; -- 134.170

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

SELECT Count(*)
FROM movie_info_idx ; -- 1.380.035

SELECT oid, relpages, reltuples
FROM pg_class
WHERE relname = 'movie_keyword'
; --relpages =24.454; reltuples = 4.523.930 = 4.523.930

SELECT Count(*)
FROM movie_link ; -- 29.997

SELECT Count(*)
FROM name ; -- 4.167.491

SELECT Count(*)
FROM person_info ; -- 2.963.664

SELECT Count(*)
FROM role_type ; --12

SELECT Count(*)
FROM title ; -- 2.528.312


SELECT table_name
FROM information_schema.tables;

SHOW default_statistics_target;


SELECT oid, relname, reltuples
FROM pg_class
WHERE relname in (
    'aka_name', 'aka_title', 'cast_info',
    'char_name', 'comp_cast_type', 'company_name',
    'company_type', 'complete_cast','info_type','keyword','kind_type', 'link_type',
    'movie_companies',
    'movie_info','movie_info_idx', 'movie_keyword', 'movie_link','name','person_info','role_type','title_count');