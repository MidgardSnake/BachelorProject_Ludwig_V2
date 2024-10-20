/*First Queries: real cardinality counting for all tables*/


SELECT Count(*)
FROM aka_name; -- 901.343

SELECT Count(*)
FROM aka_title ; -- 361.472

SELECT Count(*)
FROM cast_info ; --36.244.344

SELECT Count(*)
FROM char_name ; --3.140.339

SELECT Count(*)
FROM comp_cast_type ; --4

SELECT Count(*)
FROM company_name ; -- 234.997

SELECT Count(*)
FROM company_type; -- 4

SELECT Count(*)
FROM complete_cast ; --134.086

SELECT Count(*)
FROM info_type ; -- 113

SELECT Count(*)
FROM keyword; -- 134.170

SELECT Count(*)
FROM kind_type ; -- 7

SELECT Count(*)
FROM link_type ; -- 18

SELECT Count(*)
FROM movie_companies ; -- 2.609.129

SELECT Count(*)
FROM movie_info ; -- 14.835.720

SELECT Count(*)
FROM movie_info_idx ; -- 1.380.035

SELECT Count(*)
FROM movie_keyword ; -- 4.523.930

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


SELECT
    (SELECT COUNT(*) FROM aka_name) AS aka_name_count,
    (SELECT COUNT(*) FROM aka_title) AS aka_title_count,
    (SELECT COUNT(*) FROM cast_info) AS cast_info_count,
    (SELECT COUNT(*) FROM char_name) AS char_name_count,
    (SELECT COUNT(*) FROM comp_cast_type) AS comp_cast_type_count,
    (SELECT COUNT(*) FROM company_name) AS company_name_count,
    (SELECT COUNT(*) FROM company_type) AS company_type_count,
    (SELECT COUNT(*) FROM complete_cast) AS complete_cast_count,
    (SELECT COUNT(*) FROM info_type) AS info_type_count,
    (SELECT COUNT(*) FROM keyword) AS keyword_count,
    (SELECT COUNT(*) FROM kind_type) AS kind_type_count,
    (SELECT COUNT(*) FROM link_type) AS link_type_count,
    (SELECT COUNT(*) FROM movie_companies) AS movie_companies_count,
    (SELECT COUNT(*) FROM movie_info) AS movie_info_count,
    (SELECT COUNT(*) FROM movie_info_idx) AS movie_info_idx_count,
    (SELECT COUNT(*) FROM movie_keyword) AS movie_keyword_count,
    (SELECT COUNT(*) FROM movie_link) AS movie_link_count,
    (SELECT COUNT(*) FROM name) AS name_count,
    (SELECT COUNT(*) FROM person_info) AS person_info_count,
    (SELECT COUNT(*) FROM role_type) AS role_type_count,
    (SELECT COUNT(*) FROM title) AS title_count;
