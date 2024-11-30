import psycopg2
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
        # Zufällige Positionen für die Anomalien generieren, die sich nicht am Anfang befinden
        anomaly_positions = random.sample(range(100, num_entries), num_anomalies)
        count = 1

        for i in range(1, num_entries + 1):
            # Generate linear values where 1 appears once, 2 appears twice, 3 appears three times, etc.
            linear = count

            # Calculate modulo 10 of linear value
            modulo = linear % 10

            # Check if the current index is an anomaly position
            if i in anomaly_positions:
                linear = random.randint(0, 100)  # Random anomaly value between 0 and 100
                modulo = linear % 10

            # Insert data into the database
            cursor.execute(
                "INSERT INTO SyntheticTablemini (linear_dist, modulo) VALUES (%s, %s)",
                (int(linear), int(modulo))
            )

            # Adjust count to follow the linear pattern (1 appears once, 2 appears twice, etc.)
            if i >= (count * (count + 1)) // 2:
                count += 1

        connection.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


# Configuration
num_entries = 10
anomalies = random.randint(3, 5)  # Number of anomalies between 3 and 5
generate_and_insert_data(num_entries, anomalies)
