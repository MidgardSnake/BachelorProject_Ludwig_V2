import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lade die Daten aus der bereinigten Datei
file_path = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/SyntheticTable/01PlotData/cleaned_data.txt'
data = pd.read_csv(file_path)

# Sortiere die Daten nur nach 'counter' (Frequenzen) in aufsteigender Reihenfolge
data_sorted_by_frequency = data.sort_values(by='counter', ascending=True)

# Speicherpfad für die sortierte CSV-Datei
output_dir = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/SyntheticTable/01PlotData'
os.makedirs(output_dir, exist_ok=True)
output_csv_path = os.path.join(output_dir, 'sorted_data.csv')

# Speichere die sortierten Daten in eine neue CSV-Datei
data_sorted_by_frequency.to_csv(output_csv_path, index=False)
print(f"Die sortierte CSV wurde gespeichert unter: {output_csv_path}")

# Erstelle den Plot
x = np.arange(len(data_sorted_by_frequency))  # Positionen für die Bars
width = 0.4  # Breite der Bars

plt.figure(figsize=(14, 8))

# Erstelle zwei Barplots: einen für 'counter' und einen für 'statistic'
plt.bar(x - width/2, data_sorted_by_frequency['counter'], width, label='Counter', color='orange', alpha=0.7)
plt.bar(x + width/2, data_sorted_by_frequency['statistic'], width, label='Statistic', color='blue', alpha=0.7)

# Achsen-Labels, Titel und Legende hinzufügen
plt.xlabel('Birth Years (sorted by frequency)', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.title('Comparison of Counter and Statistic (Sorted by Frequency)', fontsize=16)
plt.xticks(x, data_sorted_by_frequency['birthyear'], rotation=90, fontsize=8)
plt.legend(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Speicherpfad für den Plot
output_plot_path = os.path.join(output_dir, 'comparison_plot.png')

# Plot speichern
plt.tight_layout()
plt.savefig(output_plot_path)
print(f"Der Plot wurde gespeichert unter: {output_plot_path}")

# Zeige den Plot an
plt.show()
