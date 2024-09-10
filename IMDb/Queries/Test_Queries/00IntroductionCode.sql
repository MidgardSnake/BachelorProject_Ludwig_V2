EXPLAIN ANALYZE

SELECT at.title, n.name, at.production_year
FROM aka_name AS an
    JOIN cast_info ci ON an.id = ci.person_id
    JOIN title t ON t.id = ci.movie_id
    JOIN aka_title at ON at.movie_id = t.id
    JOIN name n ON n.id = an.id

WHERE n.name = 'Depp, Johnny' and t.title = 'Blow'
;

SELECT *
FROM title
WHERE title = 'Blow';

