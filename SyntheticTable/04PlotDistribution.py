import pandas as pd
import matplotlib.pyplot as plt

def plot_distribution(file_path):
    # Einlesen der Daten
    data = pd.read_csv(file_path, header=None)
    data.columns = ['Linear', 'Modulo']

    # Konvertiere alle Spalten in numerische Werte, setze ungültige Umwandlungen als NaN
    data = data.apply(pd.to_numeric, errors='coerce')

    # Gruppiere und zähle die Häufigkeit jedes Wertes in beiden Spalten
    linear_counts = data['Linear'].value_counts().sort_index()
    #modulo_counts = data['Modulo'].value_counts().sort_index()

    # Farben für die Graphen definieren
    colors = ['blue', 'green']

    # Plot erstellen
    plt.figure(figsize=(12, 8))

    # Balkendiagramme für die tatsächlichen Anzahlen erstellen
    plt.bar(linear_counts.index - 0.3, linear_counts.values, color=colors[0], width=0.4, label='Linear distribution')
    #plt.bar(modulo_counts.index + 0.3, modulo_counts.values, color=colors[1], width=0.4, label='Modulo distribution')

    # Legende hinzufügen
    plt.legend()

    # Titel und Labels anpassen
    plt.title('Actual Counts of Linear and Modulo Columns')
    plt.xlabel('Value')
    plt.ylabel('Actual Row Count')

    # Ergebnis anzeigen
    plt.show()

# Pfad zur Datei, passe diesen an deinen Dateipfad an
file_path = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/SyntheticTable/00ImportData/synthetictable.txt'
plot_distribution(file_path)
