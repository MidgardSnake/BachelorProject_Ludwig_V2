import psycopg2
from psycopg2 import sql

def insert_data_from_file():
    # Verbindungsdaten
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="DKBLV1993",
        host="localhost",
        port="5432"
    )
    # Cursor zum Ausführen von SQL-Befehlen erstellen
    cur = conn.cursor()

    # Pfad zur Datei, die die Daten enthält
    file_path = '/DummyTable/00ImportData/insert_data.txt'

    try:
        # SQL-Befehl, um Daten aus einer Datei einzufügen
        cur.execute("""
        COPY DummyTable (normal_dist, poisson_dist, exponential_dist, uniform_dist, random_dist, modulo)
        FROM %s
        DELIMITER ',' CSV;
        """, (file_path,))

        # Änderungen in der Datenbank speichern
        conn.commit()
        print("Daten wurden erfolgreich eingefügt.")
    except Exception as e:
        print("Ein Fehler ist aufgetreten: ", e)
        conn.rollback()
    finally:
        # Cursor und Verbindung schließen
        cur.close()
        conn.close()

# Funktion aufrufen
insert_data_from_file()
