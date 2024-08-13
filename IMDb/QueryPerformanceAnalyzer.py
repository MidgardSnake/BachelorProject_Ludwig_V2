import os
import psycopg2
import re


class QueryPerformanceAnalyzer:
    def __init__(self, db_connection_params, queries_folder_path):
        self.db_connection = psycopg2.connect(**db_connection_params)
        self.queries_folder_path = queries_folder_path
        self.performance_data = []

    def sort_key_func(self, query_id):
        # Diese Funktion wandelt die Query-IDs in ein Sortierformat um, das erst die Zahlen, dann die Buchstaben berücksichtigt.
        match = re.match(r"(\d+)([a-z]*)", query_id)
        if match:
            return int(match.group(1)), match.group(2)
        return int(query_id), ''

    def get_sorted_performance_data(self):
        # Sortiere die performance_data-Liste basierend auf den Query-IDs
        return sorted(self.performance_data, key=lambda x: self.sort_key_func(x[0]))

    def extract_performance_data(self, explain_output):
        cost_pattern = r"cost=([\d.]+)\.\.([\d.]+)"
        time_pattern = r"actual time=([\d.]+)\.\.([\d.]+)"

        costs = re.search(cost_pattern, explain_output)
        times = re.search(time_pattern, explain_output)

        if costs and times:
            start_cost, end_cost = map(float, costs.groups())
            start_time, end_time = map(float, times.groups())
            return end_cost, end_time - start_time
        return None

    def analyze_queries(self):
        query_files = [f for f in os.listdir(self.queries_folder_path) if f.endswith('.sql')]
        total_queries = len(query_files)
        for i, file_name in enumerate(query_files, start=1):
            query_id = file_name[:-4]  # Strip the '.sql' extension
            file_path = os.path.join(self.queries_folder_path, file_name)

            with open(file_path, 'r') as file:
                query = file.read()

            with self.db_connection.cursor() as cur:
                cur.execute(f"EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) {query}")
                explain_output = '\n'.join(row[0] for row in cur.fetchall())

            perf_data = self.extract_performance_data(explain_output)
            if perf_data:
                cost, time = perf_data
                self.performance_data.append((query_id, cost, time))
                print(f"Analyse für Query {query_id} abgeschlossen ({i}/{total_queries}).")

    def get_performance_data(self):
        return self.performance_data

    def close_connection(self):
        self.db_connection.close()


