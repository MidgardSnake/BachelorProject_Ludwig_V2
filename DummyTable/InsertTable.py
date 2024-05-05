import numpy as np
import random

# Funktion zum Generieren von Daten
def generate_data(num_entries, num_anomalies):
    with open('insert_data.sql', 'w') as f:
        for i in range(num_entries):
            # Normalverteilte Daten
            normal = np.random.normal(0, 1)
            # Poisson-verteilte Daten
            poisson = np.random.poisson(5)
            # Exponentialverteilte Daten
            exponential = np.random.exponential(1)
            # Gleichverteilte Daten
            uniform = np.random.uniform(0, 1)
            # Zufällige Daten
            random_val = np.random.uniform(-100, 100)

            # Einfügen von Anomalien
            if i < num_anomalies:
                normal *= np.random.choice([10, -10])
                poisson += np.random.choice([20, -20])
                exponential *= np.random.choice([5, -5])
                uniform *= np.random.choice([3, -3])
                random_val *= np.random.choice([50, -50])

            # Schreiben der INSERT-Anweisung
            f.write(f"INSERT INTO \"DummyTable\" (normal_distribution, poisson_distribution, exponential_distribution, uniform_distribution, random_distribution) VALUES ({normal}, {poisson}, {exponential}, {uniform}, {random_val});\n")

# Variiere die Anzahl der Anomalien
anomalies = random.randint(10, 30)

# Daten generieren
generate_data(9995, anomalies)
