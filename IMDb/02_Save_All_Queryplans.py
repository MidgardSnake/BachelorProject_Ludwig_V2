
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

        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".sql"):
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
                except Exception as e:
                    print(f"Error in file {filename}: {e}")
                    conn.rollback()

    cursor.close()
    conn.close()


# Beispielaufruf der Funktion
analyze_sql_queries('/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Queries/JOB_Queries',
                    '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/explain_analysis_results.csv')




