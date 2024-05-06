SELECT * FROM "DummyTable";

EXPLAIN SELECT * FROM "DummyTable";

SELECT poisson_distribution FROM "DummyTable" WHERE poisson_distribution >0;

EXPLAIN ANALYZE VERBOSE SELECT normal_distribution FROM "DummyTable";


--einmal "nackte Statistiken" ohne PG_Stats
SELECT
  AVG(normal_distribution) AS average,
  STDDEV(normal_distribution) AS stddev,
  MIN(normal_distribution) AS min_value,
  MAX(normal_distribution) AS max_value
FROM
  "DummyTable";

--Statistik aktualisieren
ANALYZE "DummyTable" (normal_distribution);

--Statistik ausgeben lassen
SELECT
    *
    /* zur Erinnerung
    schemaname,
    tablename,
    attname as column_name,
    null_frac,        -- Anteil der NULL-Werte
    avg_width,        -- Durchschnittliche Breite der Spaltenwerte in Bytes
    n_distinct,       -- Anzahl unterschiedlicher Werte (negative Zahl bedeutet ein Prozentsatz der Gesamtzeilen)
    most_common_vals, -- Häufigste Werte
    most_common_freqs,-- Frequenz der häufigsten Werte
    histogram_bounds  -- Histogramm-Grenzen für die Verteilung der Werte

     */
FROM
    pg_stats
WHERE
    tablename = 'DummyTable' AND
    attname = 'normal_distribution';


