import psycopg2
import random

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
        # tableX3 befüllen
        print("Füge Daten in tableX3 ein...")

        for i in range(0, 15000):  # 15.000 Einträge
            random_value = random.random()
            if random_value < 0.25:  # 25% Wahrscheinlichkeit für (a=1, b=1)
                a, b = 1, 1
            elif random_value < 0.50:  # 25% Wahrscheinlichkeit für (a=0, b=1)
                a, b = 0, 1
            elif random_value < 0.75:  # 25% Wahrscheinlichkeit für (a=1, b=0)
                a, b = 1, 0
            else:  # 25% Wahrscheinlichkeit für (a=0, b=0)
                a, b = 0, 0

            cursor.execute("INSERT INTO tablex3 (id, a, b) VALUES (%s, %s, %s)", (i, a, b))

            if i % 1000 == 0:
                connection.commit()
                print(f"TableX3: {i} von 15.000 Zeilen eingefügt.")

        connection.commit()
        print("TableX3: Fertig")

        # tableX1 befüllen
        print("Füge Daten in tableX1 ein...")
        for i in range(0, 15000):
            ref3 = i  # ref3 von 1 bis 15.000
            ref2 = (i % 10000)  # ref2 von 1 bis 10.000, dann wieder 1 bis 5.000
            cursor.execute("INSERT INTO tablex1 (ref3, id, ref2) VALUES (%s, %s, %s)", (ref3, i, ref2))

            if i % 1000 == 0:
                connection.commit()
                print(f"TableX1: {i} von 15.000 Zeilen eingefügt.")

        connection.commit()
        print("TableX1: Fertig")

        # tableX2 befüllen
        print("Füge Daten in tableX2 ein...")
        for i in range(0, 10000):  # 10.000 Einträge
            if i < 5000:  # Die ersten 50% der IDs bekommen (a=0, b=0)
                a, b = 0, 0
            else:  # Die restlichen 50% der IDs bekommen (a=1, b=1)
                a, b = 1, 1
            cursor.execute("INSERT INTO tablex2 (id, a, b) VALUES (%s, %s, %s)", (i, a, b))

            if i % 1000 == 0:
                connection.commit()
                print(f"TableX2: {i} von 10.000 Zeilen eingefügt.")

        connection.commit()
        print("TableX2: Fertig")

        print("Daten erfolgreich in tableX3, tableX1 und tableX2 eingefügt.")

    except Exception as e:
        connection.rollback()  # Im Fehlerfall Änderungen zurücknehmen
        print(f"Ein Fehler ist aufgetreten: {e}")

    finally:
        # Cursor und Verbindung schließen
        cursor.close()
        connection.close()

if __name__ == "__main__":
    populate_tables()
