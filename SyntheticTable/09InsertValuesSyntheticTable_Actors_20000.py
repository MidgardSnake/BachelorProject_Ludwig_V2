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

    # 101 häufige Jahre nach dem Jahr 2000, die 15.000 Einträge ausmachen
    frequent_years = list(map(int, np.random.choice(range(2001, 2102), 101, replace=False)))  # Konvertiere zu int
    frequent_entries = []
    remaining_slots_frequent = 15000
    for i, year in enumerate(frequent_years):
        if i == len(frequent_years) - 1:
            count = remaining_slots_frequent  # Das letzte Jahr erhält die restlichen Einträge
        else:
            count = random.randint(100, min(150, remaining_slots_frequent - (len(frequent_years) - i - 1) * 100))
        frequent_entries.extend([year] * count)
        remaining_slots_frequent -= count

    # 98 weniger häufige Jahre vor dem Jahr 2000, die zusammen 4999 Einträge ausmachen
    less_frequent_years = list(map(int, np.random.choice(range(1900, 2000), 98, replace=False)))  # Konvertiere zu int
    less_frequent_entries = []
    remaining_slots_less_frequent = 4999
    for i, year in enumerate(less_frequent_years):
        if i == len(less_frequent_years) - 1:
            count = remaining_slots_less_frequent  # Das letzte Jahr erhält die restlichen Einträge
        else:
            count = random.randint(40, min(50, remaining_slots_less_frequent - (len(less_frequent_years) - i - 1) * 40))
        less_frequent_entries.extend([year] * count)
        remaining_slots_less_frequent -= count

    # 1 seltenes Jahr mit genau 1 Eintrag
    rare_year = int(np.random.choice(list(set(range(1900, 2000)) - set(less_frequent_years)), 1)[0])  # Konvertiere zu int
    rare_entries = [rare_year]

    # Kombiniere alle Einträge zu einer Liste von 20.000 Geburtsjahren
    birth_years = frequent_entries + less_frequent_entries + rare_entries
    random.shuffle(birth_years)

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
