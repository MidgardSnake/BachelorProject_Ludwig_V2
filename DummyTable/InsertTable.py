import numpy as np
import random


def generate_data(num_entries, num_anomalies):
    # Liste für zufällig gemischte Werte
    random_values = []

    # Pfad zur Datei, in der die Daten gespeichert werden
    file_path = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/DummyTable/downloadData/insert_data.txt'

    # Eröffnen der Datei zum Schreiben
    with open(file_path, 'w') as f:
        i = 0
        while i < num_entries:
            # Normalverteilte Daten
            normal = np.random.normal(0, 1)
            # Poisson-verteilte Daten
            poisson = np.random.poisson(5)
            # Exponentialverteilte Daten
            exponential = np.random.exponential(1)
            # Gleichverteilte Daten mit Min-Max Ausreißern
            uniform = np.random.uniform(0, 1)
            if i % 1000 == 0:  # Jeder 1000. Wert ist ein Ausreißer
                uniform = np.random.uniform(-10, 10)

            # Zufällige Daten
            random_val = np.random.uniform(-100, 100)
            random_values.append(random_val)

            # Einfügen von Anomalien
            if i < num_anomalies:
                normal *= np.random.choice([10, -10])
                poisson += np.random.choice([20, -20])
                exponential *= np.random.choice([5, -5])
                uniform *= np.random.choice([3, -3])
                random_val *= np.random.choice([50, -50])

            # Schreiben der Daten in die Datei
            f.write(f"{normal}, {poisson}, {exponential}, {uniform}, {random_val}\n")

            i += 1

        # Mischen der zufälligen Werte
        random.shuffle(random_values)


# Variiere die Anzahl der Anomalien
anomalies = random.randint(10, 30)

# Daten generieren
generate_data(10000, anomalies)