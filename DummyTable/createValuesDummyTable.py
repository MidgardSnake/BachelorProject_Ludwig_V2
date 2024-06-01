import numpy as np
import random

def generate_data(num_entries, num_anomalies):
    # Pfad zur Datei, in der die Daten gespeichert werden
    file_path = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/DummyTable/ImportData/insert_data.txt'

    # Eröffnen der Datei zum Schreiben
    with open(file_path, 'w') as f:
        i = 0
        while i < num_entries:
            # Normalverteilte Daten, begrenzt auf -500 bis 500
            normal = round(np.clip(np.random.normal(250, 125), -500, 500),1)

            # Poisson-verteilte Daten, skaliert auf den Bereich -500 bis 500
            poisson = np.clip(np.random.poisson(250) - 250, -500, 500)

            # Exponentialverteilte Daten, skaliert und verschoben
            exponential = np.clip(np.random.exponential(250) - 250, -500, 500)

            # Gleichverteilte Daten im Bereich -500 bis 500
            uniform = np.random.uniform(-500, 500)

            # Zufällige Daten im Bereich -500 bis 500
            random_val =  np.clip(np.random.lognormal(mean=5, sigma=0.5) - 150, -500, 500)

            # Berechnen von Modulo 10 des normalverteilten Wertes
            modulo = int(normal) % 10

            # Einfügen von Anomalien
            if i < num_anomalies:
                normal *= np.random.choice([1, -1])
                modulo = int(normal) % 10  # Modulo muss aktualisiert werden, wenn 'normal' modifiziert wird
                poisson *= np.random.choice([1, -1])
                exponential *= np.random.choice([1, -1])
                uniform *= np.random.choice([1, -1])
                random_val *= np.random.choice([1, -1])

            # Schreiben der Daten in die Datei
            f.write(f"{normal}, {poisson}, {exponential}, {uniform}, {random_val}, {modulo}\n")

            i += 1

# Variiere die Anzahl der Anomalien
anomalies = random.randint(10, 30)

# Daten generieren
generate_data(10000, anomalies)
