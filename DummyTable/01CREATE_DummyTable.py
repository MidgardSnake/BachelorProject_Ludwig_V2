import psycopg2
from psycopg2 import sql


def create_dummy_table():
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

    # SQL-Befehl zum Erstellen der Tabelle
    create_table_command = """
    CREATE TABLE DummyTable (
        normal_dist INTEGER,
        poisson_dist INTEGER,
        exponential_dist INTEGER,
        uniform_dist INTEGER,
        random_dist INTEGER,
        modulo INTEGER
    );
    """

    # SQL-Befehl ausführen
    cur.execute(create_table_command)

    # Änderungen in der Datenbank speichern
    conn.commit()

    # Cursor und Verbindung schließen
    cur.close()
    conn.close()

    print("Tabelle 'DummyTable' wurde erfolgreich erstellt.")


# Funktion aufrufen
create_dummy_table()
