ANALYZE synthetictable;


--- für die anderen attribute musst du normal_dist refactorn  .. passe auf, correlation dabei nicht zu verändern

--1. check distinct values
SELECT COUNT(*)
FROM
    (SELECT DISTINCT (exponential_dist)
    FROM synthetictable
    ORDER BY exponential_dist) as dnd;


--2. check most common vals + check most frequent vals
SELECT
    exponential_dist,
    Count(exponential_dist) as Count,
    COUNT(exponential_dist) * 1.0 / SUM(COUNT(exponential_dist)) OVER () AS Frequency
FROM synthetictable
GROUP BY exponential_dist
ORDER BY count DESC;

--3. check histogram roughly - hier für normal_dist
SELECT MIN(exponential_dist), MAX(exponential_dist)
FROM synthetictable;

/*
--4. check correlation roughly
SELECT
    'normal_dist & poisson_dist' AS pair,
    (COUNT(*) * SUM(normal_dist * poisson_dist) - SUM(normal_dist) * SUM(poisson_dist)) /
    (SQRT(COUNT(*) * SUM(normal_dist * normal_dist) - SUM(normal_dist) * SUM(normal_dist)) *
     SQRT(COUNT(*) * SUM(poisson_dist * poisson_dist) - SUM(poisson_dist) * SUM(poisson_dist))) AS correlation_coefficient
FROM
    synthetictable

UNION ALL

SELECT
    'normal_dist & exponential_dist' AS pair,
    (COUNT(*) * SUM(normal_dist * exponential_dist) - SUM(normal_dist) * SUM(exponential_dist)) /
    (SQRT(COUNT(*) * SUM(normal_dist * normal_dist) - SUM(normal_dist) * SUM(normal_dist)) *
     SQRT(COUNT(*) * SUM(exponential_dist * exponential_dist) - SUM(exponential_dist) * SUM(exponential_dist))) AS correlation_coefficient
FROM
    synthetictable

UNION ALL

SELECT
    'normal_dist & uniform_dist' AS pair,
    (COUNT(*) * SUM(normal_dist * uniform_dist) - SUM(normal_dist) * SUM(uniform_dist)) /
    (SQRT(COUNT(*) * SUM(normal_dist * normal_dist) - SUM(normal_dist) * SUM(normal_dist)) *
     SQRT(COUNT(*) * SUM(uniform_dist * uniform_dist) - SUM(uniform_dist) * SUM(uniform_dist))) AS correlation_coefficient
FROM
    synthetictable

UNION ALL

SELECT
    'normal_dist & random_dist' AS pair,
    (COUNT(*) * SUM(normal_dist * random_dist) - SUM(normal_dist) * SUM(random_dist)) /
    (SQRT(COUNT(*) * SUM(normal_dist * normal_dist) - SUM(normal_dist) * SUM(normal_dist)) *
     SQRT(COUNT(*) * SUM(random_dist * random_dist) - SUM(random_dist) * SUM(random_dist))) AS correlation_coefficient
FROM
    synthetictable;
*/


