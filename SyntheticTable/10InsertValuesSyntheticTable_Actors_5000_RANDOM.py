import psycopg2
import random
import numpy as np
from faker import Faker

fake = Faker()

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

    # 101 häufige Jahre nach dem Jahr 2000, die 80 % der 5.000 Einträge ausmachen (4.000 Einträge)
    frequent_years = list(map(int, np.random.choice(range(2001, 2102), 101, replace=False)))  # 101 häufige Geburtsjahre
    frequent_entries = []

    # Gleichmäßige Verteilung auf die 101 häufigen Jahre
    frequent_count_per_year = 4000 // len(frequent_years)  # Ungefähr gleiche Anzahl pro Jahr
    for year in frequent_years:
        frequent_entries.extend([year] * frequent_count_per_year)

    # Den Rest der 4.000 auf zufällige Jahre verteilen (falls 4.000 nicht gleichmäßig durch 101 teilbar sind)
    remaining_frequent = 4000 - len(frequent_entries)
    for i in range(remaining_frequent):
        frequent_entries.append(random.choice(frequent_years))

    # 998 weniger häufige Geburtsjahre, die jeweils einmal vorkommen
    less_frequent_years = list(map(int, np.random.choice(range(1900, 2000), 998, replace=True)))
    less_frequent_entries = less_frequent_years.copy()

    # Überprüfe, ob es noch verbleibende Jahre gibt, bevor das seltene Jahr ausgewählt wird
    remaining_years = list(set(range(1900, 2000)) - set(less_frequent_years))

    if remaining_years:
        rare_year = int(np.random.choice(remaining_years, 1)[0])
    else:
        # Falls alle Jahre bereits vergeben sind, wähle ein zufälliges Jahr aus den weniger häufigen Jahren
        rare_year = int(np.random.choice(less_frequent_years, 1)[0])

    less_frequent_entries.append(rare_year)

    # Kombiniere alle Einträge zu einer Liste von 5.000 Geburtsjahren
    birth_years = frequent_entries + less_frequent_entries
    random.shuffle(birth_years)

    # Stelle sicher, dass genau 5.000 Geburtsjahre vorhanden sind
    while len(birth_years) < 5000:
        birth_years.append(random.choice(range(1900, 2102)))

    try:
        # Einträge in die Datenbank einfügen mit einer inkrementellen ID
        for idx, birthyear in enumerate(birth_years, start=1):
            actor_name = fake.name()
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
