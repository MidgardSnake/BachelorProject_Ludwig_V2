import psycopg2
import os
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from DatabaseConnection import DatabaseConnection
from QueryReader import QueryReader
from QueryWriter import QueryWriter
from QueryAnalyzer import QueryAnalyzer
from QueryPerformanceAnalyzer import QueryPerformanceAnalyzer


class TablePlotter:
    def __init__(self, execution_times):
        self.execution_times = execution_times

    def __init__(self, performance_data):
        self.performance_data = performance_data

    def plot_execution_times(self):
        labels = [time[0] for time in self.execution_times]
        times = [time[1] for time in self.execution_times]
        plt.figure(figsize=(10, 5))
        plt.barh(labels, times, color='blue')
        plt.ylabel('Query ID')
        plt.xlabel('Execution Time (s)')
        plt.title('Query Execution Times')
        plt.tight_layout()
        plt.show()

    def plot_performance_data(self):
        # Sortiere die Daten nach der Query-ID
        self.performance_data.sort(key=lambda x: x[0])
        query_ids = [data[0] for data in self.performance_data]
        times = [data[2] for data in self.performance_data]
        costs = [data[1] for data in self.performance_data]

        fig, ax1 = plt.subplots(figsize=(15, 7))

        ax1.set_xlabel('Query ID')
        ax1.set_ylabel('Execution Time (ms)', color='red')
        ax1.plot(query_ids, times, 'r-', label='Execution Time (ms)')
        ax1.tick_params(axis='y', labelcolor='red')
        ax1.legend(loc='upper left')

        # Erstelle eine zweite y-Achse für die Kosten
        ax2 = ax1.twinx()
        ax2.set_ylabel('Cost', color='blue')
        ax2.plot(query_ids, costs, 'b-', label='Cost')
        ax2.tick_params(axis='y', labelcolor='blue')
        ax2.legend(loc='upper right')

        fig.tight_layout()  # to make sure that the labels don't get cut off
        plt.xticks(rotation=90)  # Drehen der x-Achsenbeschriftungen für bessere Lesbarkeit
        plt.show()


def version1():
    db_config = {
        'dbname': "JoinOrderBenchmark",
        'user': "postgres",
        'password': "DKBLV1993",
        'host': "localhost",
        'port': "5432"
    }
    download_dir = '/Users/lui/PycharmProjects/pythonProject/venv/downloadFile/'
    result_file_path = os.path.join(download_dir, "query_results.txt")
    time_file_path = os.path.join(download_dir, "execution_times.txt")

    # Überprüfen, ob die Dateien bereits existieren
    if os.path.exists(result_file_path) and os.path.exists(time_file_path):
        print("Die Dateien 'execution_times.txt' und 'query_results.txt' existieren bereits.")
        return

    queries_folder_path = '/Users/lui/PycharmProjects/pythonProject/venv/Queries/JOB_Queries'

    db_connection = DatabaseConnection(db_config).connect()
    reader = QueryReader(db_connection, db_config)
    reader.read_query(queries_folder_path)

    writer = QueryWriter(reader.results, reader.execution_times)
    writer.save_results(result_file_path, time_file_path)

    plotter = TablePlotter(reader.execution_times)
    plotter.plot_execution_times()

def version2():
    db_config = {
        'dbname': "JoinOrderBenchmark",
        'user': "postgres",
        'password': "DKBLV1993",
        'host': "localhost",
        'port': "5432"
    }
    download_dir = '/Users/lui/PycharmProjects/pythonProject/venv/downloadFile/'
    queries_folder_path = '/Users/lui/PycharmProjects/pythonProject/venv/Queries/JOB_Queries'

    analyzer = QueryAnalyzer(DatabaseConnection(db_config).connect())
    analyzer.analyze_and_plot(
        queries_folder_path=queries_folder_path,
        results_without_stats=os.path.join(download_dir, "execution_plans_without_stats.txt"),
        results_with_stats=os.path.join(download_dir, "execution_plans_with_stats.txt")
    )
def version3():
    db_config = {
        'dbname': "JoinOrderBenchmark",
        'user': "postgres",
        'password': "DKBLV1993",
        'host': "localhost",
        'port': "5432"
    }
    download_dir = '/Users/lui/BachelorThesis_Ludwig_V1/downloadFile'
    queries_folder_path = '/Users/lui/BachelorThesis_Ludwig_V1/Queries/JOB_Queries'
    result_file_path = os.path.join(download_dir, "query_costs_EXPLAIN.txt")
    time_file_path = os.path.join(download_dir, "execution_times_EXPLAIN.txt")

    analyzer = QueryPerformanceAnalyzer(db_config, queries_folder_path)
    analyzer.analyze_queries()

    #sortierte Daten
    performance_data = analyzer.get_sorted_performance_data()


    # Umwandeln der Leistungsdaten in das erwartete Format für QueryWriter
    results = [(query_id, cost) for query_id, cost, _ in performance_data]
    execution_times = [(query_id, time) for query_id, _, time in performance_data]

    writer = QueryWriter(results, execution_times)
    writer.save_results(result_file_path, time_file_path)

    # Stelle sicher, dass die Plotter-Klasse aktualisiert wurde, um die neuen Datenstrukturen zu handhaben.
    plotter = TablePlotter(performance_data)
    plotter.plot_performance_data()

    analyzer.close_connection()







if __name__ == '__main__':

    #version1()
    #version2()
    version3()
