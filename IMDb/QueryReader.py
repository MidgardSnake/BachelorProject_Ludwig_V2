import psycopg2
import os
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import re


class QueryReader:
    def __init__(self, db_connection, db_config):
        self.db_connection = db_connection
        self.db_config = db_config
        self.results = []
        self.execution_times = []

    def read_query(self, queries_folder_path):
        cur = self.db_connection.cursor()
        counter = 0
        if os.path.exists(queries_folder_path) and os.path.isdir(queries_folder_path):
            for file_name in os.listdir(queries_folder_path):
                file_path = os.path.join(queries_folder_path, file_name)
                if os.path.isfile(file_path) and file_name.endswith('.sql'):
                    with open(file_path, 'r') as file:
                        query = file.read()
                    start_time = time.time()
                    cur.execute(query)
                    result = cur.fetchall()
                    execution_time = time.time() - start_time
                    query_id = os.path.basename(file_path).split('.')[0]
                    self.results.append((query_id, result))
                    self.execution_times.append((query_id, execution_time))
                    counter += 1
                    print(f"Query {file_name} processed and saved. Counter {counter}/113")
        self.execution_times.sort(key=lambda x: (int(re.findall(r'\d+', x[0])[0]), x[0])) #queryID sortieren Zeit
        self.results.sort(key=lambda x: (int(re.findall(r'\d+', x[0])[0]), x[0]))         #queryID sortieren Output
        for query_id, execution_time in self.execution_times:
            print(f"Query ID: {query_id}, Execution Time: {execution_time:.2f} seconds")
        cur.close()
