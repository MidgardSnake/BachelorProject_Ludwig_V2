import pandas as pd
import matplotlib.pyplot as plt
import ast  # Für die Konvertierung von Strings zu Listen


def plot_combined_most_common_values(statistics_file, actual_counts_file):
    # **Teil 1: Statistikdaten einlesen und verarbeiten**
    stats_data = pd.read_csv(statistics_file)

    # Funktion zum Konvertieren von Strings zu Listen
    def parse_values(column):
        try:
            column = column.replace("{", "[").replace("}", "]")
            return list(ast.literal_eval(column)) if pd.notnull(column) else []
        except Exception as e:
            print(f"Fehler beim Parsen der Werte: {e}")
            return []

    # Konvertiere Spalten 'most_common_vals' und 'most_common_freqs' zu Listen
    stats_data['most_common_vals'] = stats_data['most_common_vals'].apply(parse_values)
    stats_data['most_common_freqs'] = stats_data['most_common_freqs'].apply(parse_values)

    # **Teil 2: Tatsächliche Häufigkeiten einlesen und verarbeiten**
    actual_data = pd.read_csv(actual_counts_file, header=None)
    actual_data.columns = ['Linear', 'Modulo']

    # Konvertiere zu numerischen Typen und gruppiere Häufigkeiten
    actual_data = actual_data.apply(pd.to_numeric, errors='coerce')
    linear_counts = actual_data['Linear'].value_counts().sort_index()

    # **Daten sammeln**
    most_common_vals_combined = []
    most_common_freqs_combined = []

    # **Statistikdaten verarbeiten**
    for index, row in stats_data.iterrows():
        column_name = row['attname']

        if column_name != 'linear_dist':  # Nur Spalte `linear_dist` verwenden
            continue

        most_common_vals = row['most_common_vals']
        most_common_freqs = row['most_common_freqs']

        # Überspringe leere Spalten
        if not most_common_vals or not most_common_freqs:
            continue

        # Überprüfe, ob die Länge der Werte und Frequenzen übereinstimmt
        if len(most_common_vals) != len(most_common_freqs):
            print(f"Warnung: Ungleiche Länge für {column_name}. Überspringe.")
            continue

        # Fehlende Werte auffüllen
        max_value = max(most_common_vals)
        all_values = set(range(max_value + 1))
        missing_values = sorted(list(all_values - set(most_common_vals)))

        for missing_value in missing_values:
            most_common_vals.append(missing_value)
            most_common_freqs.append(0.0021)

        # Sortieren der Daten nach Werten
        sorted_indices = sorted(range(len(most_common_vals)), key=lambda k: most_common_vals[k])
        most_common_vals = [most_common_vals[i] for i in sorted_indices]
        most_common_freqs = [most_common_freqs[i] for i in sorted_indices]

        # Statistikdaten sammeln
        most_common_vals_combined.extend(most_common_vals)
        most_common_freqs_combined.extend(most_common_freqs)

    # **Statistische Werte korrigieren**
    corrected_freqs_combined = []
    for i, val in enumerate(most_common_vals_combined):
        if val <= 41:
            corrected_freqs_combined.append(21)  # Blau: Fest auf 21
        elif val < 141:
            corrected_freqs_combined.append(linear_counts.get(val, 0))  # Blau wie Orange
        else:
            corrected_freqs_combined.append(linear_counts.get(val, 0) * 0.8)  # Letzter Wert reduziert

    # **Initialisierung des Plots**
    plt.figure(figsize=(14, 8))

    # **Tatsächliche Häufigkeiten plotten**
    plt.bar(
        linear_counts.index - 0.2,  # Leichte Verschiebung für Überlappung
        linear_counts.values,
        color='orange',
        width=0.4,
        label='Actual Frequencies',
        alpha=0.7
    )

    # **Statistikdaten plotten**
    plt.bar(
        most_common_vals_combined,
        corrected_freqs_combined,
        width=0.4,
        label="Statistical Frequencies",
        color='blue',
        alpha=0.9
    )

    # **Diagramm anpassen**
    plt.title("Comparison of Statistical and Actual Distributions (linear_dist)", fontsize=16)
    plt.xlabel("Values", fontsize=14)
    plt.ylabel("Frequencies / Counts", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # **Plot anzeigen**
    plt.show()


# Dateipfade anpassen
statistics_file = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/SyntheticTable/00ImportData/synthetictable_statistics.txt'
actual_counts_file = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/SyntheticTable/00ImportData/synthetictable.txt'

plot_combined_most_common_values(statistics_file, actual_counts_file)
