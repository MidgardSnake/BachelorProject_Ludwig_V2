import pandas as pd
import matplotlib.pyplot as plt

def plot_distribution(file_path):
    # Einlesen der Daten
    data = pd.read_csv(file_path, header=None)
    data.columns = ['Exponential', 'Modulo']

    # Attempt to convert all columns to numeric, invalid parsing will be set as NaN
    data = data.apply(pd.to_numeric, errors='coerce')

    # Farben für die Graphen definieren
    colors = ['blue', 'green']

    # Plot erstellen
    plt.figure(figsize=(12, 8))

    # Durch jede Spalte iterieren und ein Histogramm erstellen
    for index, column in enumerate(data.columns):
        column_data = data[column].dropna()  # Drop NaN values resulting from invalid conversions
        plt.hist(column_data, bins=50, color=colors[index], alpha=0.6, label=f'{column} distribution')

        # Anomalien identifizieren (beispielhaft als Werte außerhalb von 3 Standardabweichungen)
        mean = column_data.mean()
        std = column_data.std()
        anomalies = column_data[(column_data < mean - 3 * std) | (column_data > mean + 3 * std)]

        # Anomalien markieren
        for anomaly in anomalies:
            plt.plot(anomaly, 0, marker='X', markersize=10, color=colors[index])

    # Legende hinzufügen
    plt.legend()

    # Titel und Labels hinzufügen
    plt.title('Distribution of Exponential and Modulo Columns')
    plt.xlabel('Value')
    plt.ylabel('Frequency in rows')

    # Ergebnis zeigen
    plt.show()

# Pfad zur Datei, passe diesen an deinen Dateipfad an
file_path = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/SyntheticTable/00ImportData/synthetictable.txt'
plot_distribution(file_path)
