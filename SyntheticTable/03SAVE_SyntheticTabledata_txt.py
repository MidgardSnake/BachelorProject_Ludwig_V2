import psycopg2
import csv


def export_data_to_txt():
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
        cursor.execute("SELECT * FROM synthetictable")
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]

        # Save to txt
        with open('/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/SyntheticTable/00ImportData/synthetictable.txt', 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(headers)
            csv_writer.writerows(rows)

        print("Data exported to txt successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    export_data_to_txt()
