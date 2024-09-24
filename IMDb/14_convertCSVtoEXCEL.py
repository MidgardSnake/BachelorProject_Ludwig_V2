import pandas as pd
import psycopg2
import os
import ast

# Funktion, um eine Verbindung zur PostgreSQL-Datenbank herzustellen und Daten abzufragen
def query_database_to_csv(query, db_params, output_file):
    try:
        # Verbindung zur PostgreSQL-Datenbank herstellen
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Abfrage ausführen
        cursor.execute(query)

        # Ergebnis holen
        rows = cursor.fetchall()

        # Spaltennamen der Abfrage holen
        columns = [desc[0] for desc in cursor.description]

        # DataFrame aus dem Ergebnis erstellen
        df = pd.DataFrame(rows, columns=columns)

        # DataFrame in eine CSV-Datei schreiben
        df.to_csv(output_file, index=False)
        print(f"CSV-Datei wurde erstellt: {output_file}")

    except Exception as error:
        print(f"Fehler bei der Datenbankabfrage: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Funktion, um die CSV-Datei zu verarbeiten und auf 4 Einträge pro Feld zu begrenzen
def process_csv(input_file, output_file):
    # Lesen der CSV-Datei
    df = pd.read_csv(input_file)

    # Funktion zum Überprüfen der Einträge und Beschränken auf die ersten 4
    def limit_to_first_four(values):
        if isinstance(values, str):
            # Versuchen, den String als Liste zu parsen (z.B. bei `most_common_freqs`)
            try:
                parsed_values = ast.literal_eval(values)
                if isinstance(parsed_values, list) and len(parsed_values) > 4:
                    return str(parsed_values[:4])  # Nur die ersten 4 Werte behalten
            except (ValueError, SyntaxError):
                # Wenn es kein listenähnlicher String ist, bleibt es unverändert
                pass

            # Für den Fall, dass es eine durch Kommas getrennte String-Liste in {} ist
            if values.startswith("{") and values.endswith("}"):
                values_list = values[1:-1].split(",")  # Entfernt die Klammern und splittet die Einträge
                if len(values_list) > 4:
                    return "{" + ",".join(values_list[:4]) + "}"  # Nur die ersten 4 Einträge behalten

        return values  # Wenn weniger als 4 oder kein passendes Format, bleibt der Wert gleich

    # Anwenden der Funktion auf jede Spalte des DataFrames
    for column in df.columns:
        df[column] = df[column].apply(limit_to_first_four)

    # Speichern in einer neuen CSV-Datei
    df.to_csv(output_file, index=False)
    print(f"Verarbeitete CSV-Datei wurde erstellt: {output_file}")

# Parameter zur PostgreSQL-Datenbankverbindung
db_params = {
    'host': 'localhost',
    'database': 'JoinOrderBenchmark',
    'user': 'postgres',
    'password': 'DKBLV1993',
    'port': '5432'  # Standard PostgreSQL Port
}


#AB hier jedes mal den TableNamen anpassen!!!!!!!!!!!

# SQL-Abfrage
query = """
SELECT attname, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation
FROM pg_stats
WHERE tablename = 'title'
"""

# Verzeichnis für die Ergebnisdateien
output_directory = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles'

# Sicherstellen, dass das Verzeichnis existiert, andernfalls erstellen
os.makedirs(output_directory, exist_ok=True)

# Pfade für Eingabe- und Ausgabedateien festlegen
input_csv = os.path.join(output_directory, 'dbInputStatitics.csv')
output_csv = os.path.join(output_directory, 'dbOutputStatisticsCUTTED.csv')

# CSV-Datei erstellen durch die Abfrage
query_database_to_csv(query, db_params, input_csv)

# Verarbeitete CSV-Datei erstellen
process_csv(input_csv, output_csv)
