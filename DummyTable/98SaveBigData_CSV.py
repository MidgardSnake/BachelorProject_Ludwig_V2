import psycopg2
import csv

def export_tables_to_csv():
    # Database connection setup
    connection = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='DKBLV1993',
        port='5432'
    )

    # Tables to export and file paths
    tables = {
        'table1': '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/DummyTable/00ImportData/table1.csv',
        'table2': '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/DummyTable/00ImportData/table2.csv',
        'table3': '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/DummyTable/00ImportData/table3.csv'
    }

    try:
        for table_name, file_path in tables.items():
            # Fetch data from table
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                # Get column headers
                headers = [desc[0] for desc in cursor.description]

            # Write data to CSV
            with open(file_path, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(headers)  # write headers
                csvwriter.writerows(rows)  # write data

            print(f"Data from {table_name} exported successfully to {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the database connection
        connection.close()

if __name__ == "__main__":
    export_tables_to_csv()
