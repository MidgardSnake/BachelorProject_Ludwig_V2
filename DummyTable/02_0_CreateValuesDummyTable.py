import psycopg2
import numpy as np
import random


def generate_and_insert_data(num_entries, num_anomalies):
    # Database connection setup
    connection = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='DKBLV1993',
        port='5432'
    )
    cursor = connection.cursor()

    try:
        for i in range(num_entries):
            normal = int(round(np.clip(np.random.normal(250, 125), -500, 500), 1))
            poisson = int(np.clip(np.random.poisson(250) - 250, -500, 500))
            exponential = int(np.clip(np.random.exponential(250) - 250, -500, 500))
            uniform = int(np.random.uniform(-500, 500))
            random_val = int(np.clip(np.random.lognormal(mean=5, sigma=0.5) - 150, -500, 500))
            modulo = normal % 10

            if i < num_anomalies:
                normal *= random.choice([1, -1])
                modulo = normal % 10
                poisson *= random.choice([1, -1])
                exponential *= random.choice([1, -1])
                uniform *= random.choice([1, -1])
                random_val *= random.choice([1, -1])

            # Convert numpy data types to native Python types
            data = (
                int(normal),
                int(poisson),
                int(exponential),
                int(uniform),
                int(random_val),
                int(modulo)
            )

            # Insert data into the database
            cursor.execute(
                "INSERT INTO dummytable (normal_dist, poisson_dist, exponential_dist, uniform_dist, random_dist, modulo) VALUES (%s, %s, %s, %s, %s, %s)",
                data)

        connection.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


# Configuration
anomalies = random.randint(10, 30)
generate_and_insert_data(10000, anomalies)
