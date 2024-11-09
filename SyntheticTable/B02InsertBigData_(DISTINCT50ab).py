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

    # Ein Cursor-Objekt erstellen
    cursor = connection.cursor()

    try:
        # Daten in table1 einfügen (5 Millionen Zeilen)
        for i in range(1, 5000001):
            a = (i % 50)   # Werte zwischen 1 und 50
            b = (i % 50)   # Werte zwischen 1 und 50
            cursor.execute("INSERT INTO table1 (id, a, b) VALUES (%s, %s, %s)", (i, a, b))
            if i % 10000 == 0:  # Batch-Commit nach jedem 10.000 Einträgen
                connection.commit()
                print(f"Table1: {i} von 5.000.000 Zeilen eingefügt.")

        connection.commit()  # Änderungen in der Datenbank speichern
        print("Table1: Fertig")

        # Daten in table2 einfügen (6 Millionen Zeilen)
        for i in range(1, 6000001):
            ref_id = (i - 1) % 5000000 + 1  # Zyklische Verwendung von ref_id (1 bis 5 Millionen)
            a = (i % 50)  # Werte zwischen 1 und 50
            b = (i % 50)  # Werte zwischen 1 und 50
            cursor.execute("INSERT INTO table2 (ref_id, a, b, id) VALUES (%s, %s, %s, %s)", (ref_id, a, b, i))
            if i % 10000 == 0:
                connection.commit()
                print(f"Table2: {i} von 6.000.000 Zeilen eingefügt.")

        connection.commit()  # Änderungen in der Datenbank speichern
        print("Table2: Fertig")

        # Daten in table2 einfügen (6 Millionen Zeilen)
        for i in range(1, 7000001):
            ref_id = (i - 1) % 6000000 + 1  # Zyklische Verwendung von ref_id (1 bis 6 Millionen)
            a = (i % 50)  # Werte zwischen 1 und 50
            b = (i % 50)  # Werte zwischen 1 und 50
            cursor.execute("INSERT INTO table3 (ref_id, a, b, id) VALUES (%s, %s, %s, %s)", (ref_id, a, b, i))
            if i % 10000 == 0:
                connection.commit()
                print(f"Table3: {i} von 7.000.000 Zeilen eingefügt.")

        connection.commit()  # Änderungen in der Datenbank speichern
        print("Table2: Fertig")

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
