import os
import psycopg2
import json
import csv

def analyze_sql_queries(directory, output_csv):
    conn = psycopg2.connect(
        dbname="JoinOrderBenchmark", user="postgres", password="DKBLV1993", host="localhost", port="5432"
    )
    cursor = conn.cursor()

    with open(output_csv, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # alle queries durchzählen
        sql_files = sorted([f for f in os.listdir(directory) if f.endswith(".sql")])
        total_files = len(sql_files)

        for index, filename in enumerate(sql_files):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r') as file:
                query = file.read()

            try:
                cursor.execute(f"EXPLAIN (ANALYZE, FORMAT JSON) {query}")
                result = cursor.fetchone()

                if result:
                    plan_json = result[0]
                    plan_str = json.dumps(plan_json, indent=2)

                    # Schreibe das Ergebnis als einzelne Zeile
                    csv_writer.writerow([f"{filename} :", plan_str])

                # Fortschritt tracken
                print(f"Processed {index + 1}/{total_files} files: {filename}")

            except Exception as e:
                print(f"Error in file {filename}: {e}")
                conn.rollback()

    cursor.close()
    conn.close()


def analyze_sql_queries_batch(directory, output_csv_base, batch_size=10):
    conn = psycopg2.connect(
        dbname="JoinOrderBenchmark", user="postgres", password="DKBLV1993", host="localhost", port="5432"
    )
    cursor = conn.cursor()

    # Alle SQL-Dateien im Verzeichnis auflisten
    sql_files = sorted([f for f in os.listdir(directory) if f.endswith(".sql")])
    total_files = len(sql_files)

    # Zähler für die Batches und den Dateinamen
    batch_counter = 0

    for i in range(0, total_files, batch_size):
        # Neue CSV-Datei für den aktuellen Batch öffnen
        output_csv = f"{output_csv_base}_batch_{batch_counter + 1}.csv"
        with open(output_csv, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Verarbeite die nächsten `batch_size` Dateien
            for j in range(i, min(i + batch_size, total_files)):
                filename = sql_files[j]
                filepath = os.path.join(directory, filename)

                with open(filepath, 'r') as file:
                    query = file.read()

                try:
                    cursor.execute(f"EXPLAIN (ANALYZE, FORMAT JSON) {query}")
                    result = cursor.fetchone()

                    if result:
                        plan_json = result[0]
                        plan_str = json.dumps(plan_json, indent=2)

                        # Schreibe das Ergebnis als einzelne Zeile in die Batch-Datei
                        csv_writer.writerow([f"{filename} :", plan_str])

                    # Fortschritt tracken
                    print(f"Processed {j + 1}/{total_files} files: {filename}")

                except Exception as e:
                    print(f"Error in file {filename}: {e}")
                    conn.rollback()

        # Zähler für die Batch-Datei erhöhen
        batch_counter += 1

    cursor.close()
    conn.close()


# Aufruf der Funktion1 , du kannst auch den batch ausführen um kleinere csv's zu bekommen
analyze_sql_queries(
    '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Queries/JOB_Queries',
    '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/explain_analysis_results.csv'
)


