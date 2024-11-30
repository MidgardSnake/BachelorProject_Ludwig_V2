import pandas as pd
import matplotlib.pyplot as plt
import ast  # Für die Konvertierung von Strings zu Listen (ohne `set`)

def plot_combined_most_common_values(file_path):
    # Einlesen der Statistikdaten
    data = pd.read_csv(file_path)

    # Konvertiere Spalten 'most_common_vals' und 'most_common_freqs' von Strings zu Listen
    def parse_values(column):
        try:
            # Ersetze `{}` durch `[]` und verwende `ast.literal_eval`, um es in eine Liste umzuwandeln
            column = column.replace("{", "[").replace("}", "]")
            return list(ast.literal_eval(column)) if pd.notnull(column) else []
        except Exception as e:
            print(f"Fehler beim Parsen der Werte: {e}")
            return []

    # Anwenden auf beide Spalten
    data['most_common_vals'] = data['most_common_vals'].apply(parse_values)
    data['most_common_freqs'] = data['most_common_freqs'].apply(parse_values)

    # Initialisierung des Plots
    plt.figure(figsize=(14, 8))

    # Iteriere durch jede Spalte in der Tabelle und füge Daten zum Plot hinzu
    for index, row in data.iterrows():
        column_name = row['attname']

        # Überspringe die Spalte "modulo"
        if column_name == "modulo":
            continue

        most_common_vals = row['most_common_vals']
        most_common_freqs = row['most_common_freqs']

        # Überspringe Spalten ohne Werte
        if not most_common_vals or not most_common_freqs:
            continue

        # Sicherstellen, dass die Länge von Werten und Frequenzen übereinstimmt
        if len(most_common_vals) != len(most_common_freqs):
            print(f"Warnung: Ungleiche Länge für {column_name}. Überspringe.")
            continue

        # Wenn die Spalte `linear_dist` ist, fülle fehlende Werte auf
        if column_name == 'linear_dist':
            max_value = max(most_common_vals)
            all_values = set(range(max_value + 1))  # Alle Werte von 0 bis max(most_common_vals)
            missing_values = sorted(list(all_values - set(most_common_vals)))  # Fehlende Werte

            # Füge die fehlenden Werte hinzu mit der Frequenz von 0.0021
            for missing_value in missing_values:
                most_common_vals.append(missing_value)
                most_common_freqs.append(0.0021)

        # Plot der Daten für diese Spalte
        plt.bar(
            most_common_vals,
            most_common_freqs,
            width=0.4,
            label=f"{column_name} distribution",
            alpha=0.7
        )

    # Titel und Labels
    plt.title("Most Common Values and Frequencies (Including Missing Values)", fontsize=16)
    plt.xlabel("Values", fontsize=14)
    plt.ylabel("Frequencies", fontsize=14)

    # Legende hinzufügen
    plt.legend(fontsize=12)

    # Achsenformatierung
    plt.xticks(rotation=45, fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Ergebnis anzeigen
    plt.tight_layout()
    plt.show()


# Dateipfad anpassen
file_path = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/SyntheticTable/00ImportData/synthetictable_statistics.txt'
plot_combined_most_common_values(file_path)
