import psycopg2
import csv


def export_table_statistics():
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
        # Table(s) to fetch statistics for
        tables = ['synthetictable']

        for table in tables:
            # Fetch statistics from pg_stats
            cursor.execute("""
            SELECT *
            FROM pg_stats
            WHERE tablename = %s;
            """, (table,))

            rows = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]

            # Save statistics to a file
            output_file = f'/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/SyntheticTable/00ImportData/{table}_statistics.txt'
            with open(output_file, 'w', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(headers)  # Write column headers
                csv_writer.writerows(rows)  # Write data rows

            print(f"Statistics for {table} exported to {output_file} successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    export_table_statistics()
