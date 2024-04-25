/*First Queries: cardinality counting for all tables*/


SELECT Count(*)
FROM aka_name;

SELECT Count(*)
FROM aka_title ;

SELECT Count(*)
FROM cast_info ;

SELECT Count(*)
FROM char_name ;

SELECT Count(*)
FROM comp_cast_type ;

SELECT Count(*)
FROM company_name ;

SELECT Count(*)
FROM company_type;

SELECT Count(*)
FROM complete_cast ;

SELECT Count(*)
FROM info_type ;

SELECT Count(*)
FROM keyword;

SELECT Count(*)
FROM kind_type ;

SELECT Count(*)
FROM link_type ;

SELECT Count(*)
FROM movie_companies ;

SELECT Count(*)
FROM movie_info ;

SELECT Count(*)
FROM movie_info_idx ;

SELECT Count(*)
FROM movie_keyword ;

SELECT Count(*)
FROM movie_link ;

SELECT Count(*)
FROM name ;

SELECT Count(*)
FROM person_info ;

SELECT Count(*)
FROM role_type ;

SELECT Count(*)
FROM title ;


SELECT table_name
FROM information_schema.tables;