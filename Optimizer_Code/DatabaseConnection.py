import psycopg2
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter



class DatabaseConnection:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        try:
            return psycopg2.connect(**self.db_config)
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None