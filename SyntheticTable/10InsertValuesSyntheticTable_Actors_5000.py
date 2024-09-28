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

    # 101 häufige Jahre nach dem Jahr 2000, die jetzt 3.750 Einträge ausmachen (75% von 5.000)
    frequent_years = list(map(int, np.random.choice(range(2001, 2102), 101, replace=False)))  # Konvertiere zu int
    frequent_entries = []
    remaining_slots_frequent = 3750  # 75% von 5000
    for i, year in enumerate(frequent_years):
        if i == len(frequent_years) - 1:
            count = remaining_slots_frequent  # Das letzte Jahr erhält die restlichen Einträge
        else:
            count = random.randint(25, min(50, remaining_slots_frequent - (len(frequent_years) - i - 1) * 25))
        frequent_entries.extend([year] * count)
        remaining_slots_frequent -= count

    # 98 weniger häufige Jahre vor dem Jahr 2000, die zusammen 1249 Einträge ausmachen (25% von 5000 minus 1 für das seltene Jahr)
    less_frequent_years = list(map(int, np.random.choice(range(1900, 2000), 98, replace=False)))  # Konvertiere zu int
    less_frequent_entries = []
    remaining_slots_less_frequent = 1249  # 25% von 5000 minus 1
    for i, year in enumerate(less_frequent_years):
        if i == len(less_frequent_years) - 1:
            count = remaining_slots_less_frequent  # Das letzte Jahr erhält die restlichen Einträge
        else:
            count = random.randint(10, min(20, remaining_slots_less_frequent - (len(less_frequent_years) - i - 1) * 10))
        less_frequent_entries.extend([year] * count)
        remaining_slots_less_frequent -= count

    # 1 seltenes Jahr mit genau 1 Eintrag
    rare_year = int(np.random.choice(list(set(range(1900, 2000)) - set(less_frequent_years)), 1)[0])  # Konvertiere zu int
    rare_entries = [rare_year]

    # Kombiniere alle Einträge zu einer Liste von 5.000 Geburtsjahren
    birth_years = frequent_entries + less_frequent_entries + rare_entries
    random.shuffle(birth_years)

    try:
        # Einträge in die Datenbank einfügen ohne id, da sie entfernt wurde
        for birthyear in birth_years:
            actor_name = fake.name()
            cursor.execute(
                "INSERT INTO SyntheticTable_Actors (name, birthyear) VALUES (%s, %s)",
                (actor_name, birthyear)
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
