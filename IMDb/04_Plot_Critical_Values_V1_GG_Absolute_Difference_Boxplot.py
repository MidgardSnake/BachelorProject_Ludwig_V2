import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

class QueryAnalyzer:
    def __init__(self, csv_file):
        try:
            # CSV-Datei einlesen
            self.df = pd.read_csv(csv_file, delimiter=',', encoding='utf-8')
        except Exception as e:
            print(f"Fehler beim Lesen der Datei: {e}")
            raise

    def filter_queries(self):
        # Spaltennamen bereinigen und leere Werte entfernen
        self.df.columns = self.df.columns.str.strip()
        self.df = self.df.dropna(subset=['Deviation (in rows)'])  # Nur Zeilen mit Deviation verwenden

    def plot_deviation(self):
        # Numerischen Teil des Query-Namens extrahieren, um die Daten zu sortieren
        self.df['Query Number'] = self.df['Query Name'].str.extract(r'(\d+)').astype(int)

        # Dataframe nach 'Query Number' sortieren
        self.df = self.df.sort_values(by='Query Number')

        # Plot-Einstellungen
        plt.figure(figsize=(12, 6))

        # Boxplot für jede Query erstellen
        sns.boxplot(x='Query Name', y='Deviation (in rows)', data=self.df, showfliers=True)

        # Titel und Achsenbeschriftungen festlegen
        plt.title('Distribution of Query Deviations')
        plt.xlabel('Query Name')
        plt.xticks(rotation=45, ha='right')
        plt.ylabel('Deviation (in rows)')

        # Anpassung der x-Achsen-Beschriftungen: Zeige jede zweite Bezeichnung
        x_labels = self.df['Query Name'].unique()
        labeled_ticks = [label if (i % 2 == 0) else '' for i, label in enumerate(x_labels)]
        plt.xticks(ticks=range(len(x_labels)), labels=labeled_ticks, rotation=45, ha='right', fontsize=10)

        # Gitternetzlinien und Hintergrundfarbe festlegen
        plt.grid(True, linestyle='--', linewidth=0.5)
        plt.gca().set_facecolor('whitesmoke')

        # Plot anzeigen
        plt.tight_layout()
        plt.show()

    def analyze_and_plot(self):
        self.filter_queries()
        self.plot_deviation()

# Beispielhafter Aufruf:
analyzer = QueryAnalyzer('/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/Resultdifference.csv')
analyzer.analyze_and_plot()
