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

    # 101 häufige Birthyears (alle kleiner als 2000), die zusammen 9.231 Einträge ergeben
    frequent_years = list(map(int, np.random.choice(range(1900, 2001), 101, replace=False)))  # 101 häufige Birthyears
    frequent_entries = []

    # Verteilung der 9231 Einträge mit 40 Einträgen für das häufigste Jahr und aufwärts inkrementierend
    start_count = 40
    for i, year in enumerate(frequent_years):
        frequent_entries.extend([year] * (start_count + i))  # Inkrementell +1 für jedes Jahr

    # 99 seltene Birthyears (alle größer als 2000), die zusammen 769 Einträge ergeben
    rare_years = list(map(int, np.random.choice(range(2001, 2102), 99, replace=False)))  # 99 seltene Birthyears
    rare_entries = []

    # Gleichmäßige Verteilung der 769 Einträge auf die 99 seltenen Jahre
    rare_count_per_year = 769 // len(rare_years)  # Ungefähr gleiche Anzahl pro Jahr
    for year in rare_years:
        rare_entries.extend([year] * rare_count_per_year)

    # Den Rest der 769 auf zufällige Jahre verteilen (falls nicht gleichmäßig durch 99 teilbar)
    remaining_rare = 769 - len(rare_entries)
    for i in range(remaining_rare):
        rare_entries.append(random.choice(rare_years))

    # Kombiniere alle Einträge zu einer Liste von Geburtsjahren
    birth_years = frequent_entries + rare_entries
    random.shuffle(birth_years)

    # Wenn weniger als 10.000 Einträge vorhanden sind, fülle sie auf
    while len(birth_years) < 10000:
        birth_years.append(random.choice(frequent_years + rare_years))

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
