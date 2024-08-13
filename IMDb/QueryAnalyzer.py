import psycopg2
import os
import time
import json
import re
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from DatabaseConnection import DatabaseConnection

def sort_key_func(query_id):
    # Diese Funktion wandelt die Query-IDs in ein Sortierformat um, das erst die Zahlen, dann die Buchstaben berücksichtigt.
    match = re.match(r"(\d+)([a-z]*)", query_id)
    if match:
        return int(match.group(1)), match.group(2)
    return query_id, ''

def sort_execution_plans(execution_plans):
    # Sortiere die Ausführungspläne basierend auf den angepassten Sortierschlüsseln
    return sorted(execution_plans, key=lambda x: sort_key_func(x[0]))

def save_to_file(data, file_path):
    with open(file_path, 'w') as file:
        for query_id, execution_plan in data:
            # Schreibe die Query-ID und den Execution Plan als String in die Datei
            file.write(f"Query {query_id}:\n{execution_plan}\n\n")

def extract_cost_and_time(plan_dict, costs, times):
    if "Total Cost" in plan_dict:
        costs.append(plan_dict["Total Cost"])
    if "Actual Total Time" in plan_dict:
        times.append(plan_dict["Actual Total Time"])
    # Rekursive Suche nach weiteren Plänen innerhalb dieses Plans
    if "Plans" in plan_dict:
        for sub_plan in plan_dict["Plans"]:
            extract_cost_and_time(sub_plan, costs, times)


def plot_execution_data(self, execution_plans, title_suffix):
    # Initialisieren Sie leere Listen für Kosten und Zeiten
    costs = []
    times = []
    labels = []

    for plan in execution_plans:
        plan_dict = json.loads(plan) if isinstance(plan, str) else plan
        extract_cost_and_time(plan_dict["Plan"], costs, times)
        labels.append(plan[0])  # Verwenden der Query-ID als Label

    # Erstellen Sie die Diagramme
    if costs:
        plt.figure(figsize=(10, 5))
        plt.bar(labels, costs, color='blue')
        plt.ylabel('Costs')
        plt.title(f'Query Costs {title_suffix}')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    if times:
        plt.figure(figsize=(10, 5))
        plt.bar(labels, times, color='green')
        plt.ylabel('Execution Time (ms)')
        plt.title(f'Query Execution Times {title_suffix}')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

class QueryAnalyzer:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def analyze_query(self, query):
        with self.db_connection.cursor() as cur:
            cur.execute(f"EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) {query}")
            plan = cur.fetchall()
            return ''.join(row[0] for row in plan)  # Hier fügen wir alle Zeilen der Ausgabe zusammen

    def analyze_queries(self, queries_folder_path, analyze=False):
        execution_plans = []
        if analyze:
            with self.db_connection.cursor() as cur:
                cur.execute("ANALYZE")
        for file_name in os.listdir(queries_folder_path):
            file_path = os.path.join(queries_folder_path, file_name)
            if os.path.isfile(file_path) and file_name.endswith('.sql'):
                with open(file_path, 'r') as file:
                    query = file.read()
                plan = self.analyze_query(query)
                # Entferne die '.sql' Erweiterung vom Dateinamen
                query_id = file_name[:-4]
                execution_plans.append((query_id, plan))
                print(f"Analyse für Query {query_id} abgeschlossen.")
        return execution_plans



    #
    def analyze_and_plot(self, queries_folder_path, results_without_stats, results_with_stats):
        # Queries ohne Statistiken analysieren und sortieren
        execution_plans_without_stats = self.analyze_queries(queries_folder_path)
        sorted_execution_plans_without_stats = sort_execution_plans(execution_plans_without_stats)

        # Queries mit Statistiken analysieren und sortieren
        execution_plans_with_stats = self.analyze_queries(queries_folder_path, analyze=True)
        sorted_execution_plans_with_stats = sort_execution_plans(execution_plans_with_stats)

        # Sortierte Pläne speichern
        save_to_file(sorted_execution_plans_without_stats, results_without_stats)
        save_to_file(sorted_execution_plans_with_stats, results_with_stats)

        # Plot-Graphen für die Ausführungskosten und -zeiten
        self.plot_execution_data(sorted_execution_plans_without_stats, "Without Stats")
        self.plot_execution_data(sorted_execution_plans_with_stats, "With Stats")




