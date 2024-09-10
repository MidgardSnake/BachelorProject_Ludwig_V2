ANALYZE dummytable;


--- für die anderen attribute musst du normal_dist refactorn  .. passe auf, correlation dabei nicht zu verändern

--1. check distinct values
SELECT COUNT(*)
FROM
    (SELECT DISTINCT (modulo)
    FROM dummytable
    ORDER BY modulo) as dnd;


--2. check most common vals + check most frequent vals
SELECT
    modulo,
    Count(modulo) as Count,
    COUNT(modulo) * 1.0 / SUM(COUNT(modulo)) OVER () AS Frequency
FROM dummytable
GROUP BY modulo
ORDER BY count DESC;

--3. check histogram roughly
SELECT MIN(modulo), MAX(modulo)
FROM dummytable;

/*
--4. check correlation roughly
SELECT
    'normal_dist & poisson_dist' AS pair,
    (COUNT(*) * SUM(normal_dist * poisson_dist) - SUM(normal_dist) * SUM(poisson_dist)) /
    (SQRT(COUNT(*) * SUM(normal_dist * normal_dist) - SUM(normal_dist) * SUM(normal_dist)) *
     SQRT(COUNT(*) * SUM(poisson_dist * poisson_dist) - SUM(poisson_dist) * SUM(poisson_dist))) AS correlation_coefficient
FROM
    dummytable

UNION ALL

SELECT
    'normal_dist & exponential_dist' AS pair,
    (COUNT(*) * SUM(normal_dist * exponential_dist) - SUM(normal_dist) * SUM(exponential_dist)) /
    (SQRT(COUNT(*) * SUM(normal_dist * normal_dist) - SUM(normal_dist) * SUM(normal_dist)) *
     SQRT(COUNT(*) * SUM(exponential_dist * exponential_dist) - SUM(exponential_dist) * SUM(exponential_dist))) AS correlation_coefficient
FROM
    dummytable

UNION ALL

SELECT
    'normal_dist & uniform_dist' AS pair,
    (COUNT(*) * SUM(normal_dist * uniform_dist) - SUM(normal_dist) * SUM(uniform_dist)) /
    (SQRT(COUNT(*) * SUM(normal_dist * normal_dist) - SUM(normal_dist) * SUM(normal_dist)) *
     SQRT(COUNT(*) * SUM(uniform_dist * uniform_dist) - SUM(uniform_dist) * SUM(uniform_dist))) AS correlation_coefficient
FROM
    dummytable

UNION ALL

SELECT
    'normal_dist & random_dist' AS pair,
    (COUNT(*) * SUM(normal_dist * random_dist) - SUM(normal_dist) * SUM(random_dist)) /
    (SQRT(COUNT(*) * SUM(normal_dist * normal_dist) - SUM(normal_dist) * SUM(normal_dist)) *
     SQRT(COUNT(*) * SUM(random_dist * random_dist) - SUM(random_dist) * SUM(random_dist))) AS correlation_coefficient
FROM
    dummytable;
*/


