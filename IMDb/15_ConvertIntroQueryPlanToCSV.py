import os
import psycopg2
import json
import csv

class QueryPlanProcessor:
    def __init__(self, path, output_csv, db_config):
        self.path = path
        self.output_csv = output_csv
        self.db_config = db_config

    def connect_db(self):
        """Stellt eine Verbindung zur PostgreSQL-Datenbank her."""
        try:
            conn = psycopg2.connect(
                dbname=self.db_config["dbname"],
                user=self.db_config["user"],
                password=self.db_config["password"],
                host=self.db_config["host"],
                port=self.db_config["port"]
            )
            return conn
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None

    def process_sql(self):
        """Überprüft, ob es sich um eine Datei oder ein Verzeichnis handelt, und verarbeitet entsprechend."""
        if os.path.isdir(self.path):
            self.process_sql_files()
        elif os.path.isfile(self.path):
            self.process_single_sql(self.path)
        else:
            print(f"Error: {self.path} is neither a directory nor a file.")

    def process_sql_files(self):
        """Verarbeitet alle SQL-Dateien in einem Verzeichnis."""
        conn = self.connect_db()
        if not conn:
            return

        cursor = conn.cursor()
        sql_files = sorted([f for f in os.listdir(self.path) if f.endswith(".sql")])
        total_files = len(sql_files)

        with open(self.output_csv, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Query ID', 'Estimated Rows', 'Actual Rows', 'Node Type'])

            for index, filename in enumerate(sql_files):
                filepath = os.path.join(self.path, filename)
                with open(filepath, 'r') as file:
                    query = file.read()

                try:
                    # Führe EXPLAIN ANALYZE mit JSON-Formatierung durch
                    cursor.execute(f"EXPLAIN (ANALYZE, FORMAT JSON) {query}")
                    result = cursor.fetchone()

                    if result:
                        plan_json = result[0]
                        self.extract_mismatches(plan_json, csv_writer, filename)

                    # Fortschritt tracken
                    print(f"Processed {index + 1}/{total_files} files: {filename}")

                except Exception as e:
                    print(f"Error processing {filename}: {e}")
                    conn.rollback()

        cursor.close()
        conn.close()

    def process_single_sql(self, filepath):
        """Verarbeitet eine einzelne SQL-Datei."""
        conn = self.connect_db()
        if not conn:
            return

        cursor = conn.cursor()

        with open(filepath, 'r') as file:
            query = file.read()

        try:
            # Führe EXPLAIN ANALYZE mit JSON-Formatierung durch
            cursor.execute(f"EXPLAIN (ANALYZE, FORMAT JSON) {query}")
            result = cursor.fetchone()

            with open(self.output_csv, mode='w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Query ID', 'Estimated Rows', 'Actual Rows', 'Node Type'])

                if result:
                    plan_json = result[0]
                    self.extract_mismatches(plan_json, csv_writer, os.path.basename(filepath))

            # Fortschritt tracken
            print(f"Processed file: {filepath}")

        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            conn.rollback()

        cursor.close()
        conn.close()

    def extract_mismatches(self, plan_json, csv_writer, query_id):
        """Extrahiert Stellen im Plan, bei denen die geschätzten und tatsächlichen Zeilen unterschiedlich sind."""
        def recursive_extract(plan_node):
            if 'Plan Rows' in plan_node and 'Actual Rows' in plan_node and 'Node Type' in plan_node:
                estimated_rows = plan_node['Plan Rows']
                actual_rows = plan_node['Actual Rows']
                node_type = plan_node['Node Type']

                if estimated_rows != actual_rows:
                    # Schreibe die Daten in die CSV-Datei
                    csv_writer.writerow([query_id, estimated_rows, actual_rows, node_type])

            # Gehe rekursiv durch den Abfrageplan, um tiefer liegende Knoten zu überprüfen
            if 'Plans' in plan_node:
                for sub_plan in plan_node['Plans']:
                    recursive_extract(sub_plan)

        # Starte die Extraktion von Mismatches
        recursive_extract(plan_json[0]['Plan'])

# Datenbankkonfigurationsdetails
db_config = {
    "dbname": "JoinOrderBenchmark",
    "user": "postgres",
    "password": "DKBLV1993",
    "host": "localhost",
    "port": "5432"
}

# SQL-Datei oder Verzeichnis mit SQL-Dateien
sql_path = '/IMDb/Queries/Test_Queries/0eJohnnyDepp.sql'

# CSV-Ausgabedatei
output_csv = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/JohnnyDeppResult.csv'

# Erstelle den QueryPlanProcessor und führe die Analyse durch
processor = QueryPlanProcessor(sql_path, output_csv, db_config)
processor.process_sql()
