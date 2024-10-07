import psycopg2
import random
import string
import numpy as np

def generate_random_varchar(length=4):
    """Generiert eine zufällige Zeichenkette mit der Länge 4."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_and_insert_data():
    # Database connection setup
    connection = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='DKBLV1993',
        port='5432'
    )
    cursor = connection.cursor()

    # 100 Birthyears (alle kleiner als 2000), die jeweils 98 Mal vorkommen
    frequent_years = random.sample(range(1890, 2000), 100)  # Wähle 100 eindeutige Jahre aus dem Bereich 1890-1999
    frequent_entries = []

    # Verteilung der 100 Birthyears mit jeweils 98 Einträgen
    for year in frequent_years:
        frequent_entries.extend([year] * 98)

    # Ein Birthyear, das 80 Mal vorkommt, aus dem Bereich 1890-1999 und noch nicht in frequent_years vorhanden
    year_101 = random.choice([year for year in range(1890, 2000) if year not in frequent_years])
    frequent_entries.extend([year_101] * 80)

    # Ein weiteres eindeutiges Birthyear, das 22 Mal vorkommt, auch aus dem Bereich 1890-1999 und nicht in frequent_years oder year_101
    year_102 = random.choice([year for year in range(1890, 2000) if year not in frequent_years and year != year_101])
    frequent_entries.extend([year_102] * 22)

    # 98 seltene Birthyears (alle größer als 2000), die jeweils einmal vorkommen
    rare_years = random.sample(range(2001, 2102), 98)  # 98 eindeutige Jahre nach 2000
    rare_entries = []

    # Verteilung der 98 Birthyears mit jeweils einem Eintrag
    for year in rare_years:
        rare_entries.extend([year] * 1)

    # Kombiniere alle Einträge zu einer Liste von Geburtsjahren
    birth_years = frequent_entries + rare_entries
    random.shuffle(birth_years)

    # Sicherstellen, dass die Liste genau 10.000 Einträge hat
    assert len(birth_years) == 10000, f"Expected 10,000 entries, but got {len(birth_years)}"

    try:
        # Einträge in die Datenbank einfügen mit einer inkrementellen ID und zufälligem VARCHAR(4)
        for idx, birthyear in enumerate(birth_years, start=1):
            actor_name = generate_random_varchar(4)
            cursor.execute(
                "INSERT INTO SyntheticTable_Actors (id, name, birthyear) VALUES (%s, %s, %s)",
                (idx, actor_name, birthyear)
            )

        connection.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# Daten generieren und einfügen
generate_and_insert_data()
