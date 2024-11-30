INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (1, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (1, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (2, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (2, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (2, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (2, 1);

INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);

INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);
INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (3, 1);



ANALYSE synthetictablemini;

SELECT *
FROM pg_stats
WHERE tablename = 'synthetictablemini';

EXPLAIN ANALYSE SELECT *
FROM synthetictablemini
WHERE linear_dist = '38';

SELECT Count(*)
FROM synthetictablemini
WHERE linear_dist = '2';