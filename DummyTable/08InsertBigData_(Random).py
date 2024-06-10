import psycopg2

def populate_tables():
    # Datenbankverbindung herstellen
    connection = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='DKBLV1993',
        port='5432'
    )

    # Ein Cursor-Objekt erstellen, um Operationen in der DB durchzuführen
    cursor = connection.cursor()

    # SQL-Befehle zum Einfügen der Daten in table1, table2 und table3
    try:
        cursor.execute("""
            INSERT INTO table1 (nummer, modulo)
            SELECT i, floor(random() * 101)::INT FROM generate_series(0, 2999999) AS s(i);
        """)
        connection.commit()  # Änderungen in der Datenbank speichern

        cursor.execute("""
            INSERT INTO table2 (nummer, modulo)
            SELECT i, floor(random() * 101)::INT FROM generate_series(0, 4999999) AS s(i);
        """)
        connection.commit()

        cursor.execute("""
            INSERT INTO table3 (nummer, modulo)
            SELECT i, floor(random() * 101)::INT FROM generate_series(0, 6999999) AS s(i);
        """)
        connection.commit()

        print("Daten erfolgreich in table1, table2, und table3 eingefügt.")
    except Exception as e:
        connection.rollback()  # Im Fehlerfall Änderungen zurücknehmen
        print(f"Ein Fehler ist aufgetreten: {e}")
    finally:
        # Cursor und Verbindung schließen
        cursor.close()
        connection.close()

if __name__ == "__main__":
    populate_tables()
