import pandas as pd
import matplotlib.pyplot as plt

def plot_distribution(file_path):
    # Einlesen der Daten
    data = pd.read_csv(file_path, header=None)
    data.columns = ['Normal', 'Poisson', 'Exponential', 'Uniform', 'Random', 'Modulo']

    # Farben für die Graphen definieren
    colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown']

    # Plot erstellen
    plt.figure(figsize=(12, 8))

    # Durch jede Spalte iterieren und ein Histogramm erstellen
    for index, column in enumerate(data.columns):
        plt.hist(data[column], bins=50, color=colors[index], alpha=0.6, label=f'{column} distribution')

        # Anomalien identifizieren (beispielhaft als Werte außerhalb von 3 Standardabweichungen)
        mean = data[column].mean()
        std = data[column].std()
        anomalies = data[column][(data[column] < mean - 3 * std) | (data[column] > mean + 3 * std)]

        # Anomalien markieren
        for anomaly in anomalies:
            plt.plot(anomaly, 0, marker='X', markersize=10, color=colors[index])

    # Legende hinzufügen
    plt.legend()

    # Titel und Labels hinzufügen
    plt.title('Distribution of Different Columns')
    plt.xlabel('Values')
    plt.ylabel('Frequency')

    # Ergebnis zeigen
    plt.show()

# Pfad zur Datei, passe diesen an deinen Dateipfad an
file_path = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/DummyTable/ImportData/insert_data.txt'
plot_distribution(file_path)
