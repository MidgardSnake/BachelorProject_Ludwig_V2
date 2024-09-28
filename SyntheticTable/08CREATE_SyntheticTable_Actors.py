import psycopg2
from psycopg2 import sql


def create_syntheticTable():
    # Verbindungsdaten
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="DKBLV1993",
        host="localhost",
        port="5432"
    )

    # Cursor
    cur = conn.cursor()

    # SQL-Befehl zum Erstellen der Tabelle
    create_table_command = """
    CREATE TABLE SyntheticTable_Actors (
        id INTEGER,
        name VARCHAR,
        birthyear INTEGER
    );
    """

    create_table_command1 = """
        DROP TABLE SyntheticTable_Actors;
        """


    cur.execute(create_table_command)
    conn.commit()
    cur.close()
    conn.close()

    print("Tabelle 'SyntheticTable_Actors' wurde erfolgreich erstellt.")


# Funktion aufrufen
create_syntheticTable()



