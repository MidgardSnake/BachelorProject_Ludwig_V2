import psycopg2
import os
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import re

class QueryWriter:
    def __init__(self, results, execution_times):
        self.results = results
        self.execution_times = execution_times

    def save_results(self, result_file_path, time_file_path):
        with open(result_file_path, 'w') as res_file:
            for result in self.results:
                res_file.write(f"{result[0]}: {result[1]}\n")
        with open(time_file_path, 'w') as time_file:
            for time in self.execution_times:
                time_file.write(f"{time[0]}: {time[1]}\n")
