import psycopg2
from prettytable import PrettyTable


def analyze_and_fetch_stats():
    # Verbindungsinformationen anpassen
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="DKBLV1993",
        host="localhost",
    )

    try:
        # Cursor erstellen
        cur = conn.cursor()

        # ANALYZE Kommando ausführen, um die Statistiken zu aktualisieren
        cur.execute("ANALYZE dummytable;")
        print("ANALYZE command executed successfully.")

        # Statistiken abfragen
        cur.execute("SELECT * FROM pg_stats WHERE tablename = 'dummytable';")

        # Spaltennamen extrahieren für die Tabelle
        col_names = [desc[0] for desc in cur.description]
        table = PrettyTable()
        table.field_names = col_names  # Setzen der Spaltenüberschriften für die Tabelle

        # Daten in die Tabelle einfügen
        rows = cur.fetchall()
        for row in rows:
            table.add_row(row)

        # Tabelle ausgeben
        print(table)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cursor und Verbindung schließen
        cur.close()
        conn.close()


# Funktion aufrufen
analyze_and_fetch_stats()
