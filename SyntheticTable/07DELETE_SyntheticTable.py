import psycopg2

def delete_data_from_table():
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
        # Execute delete command
        cursor.execute("DELETE FROM synthetictable")
        connection.commit()  # Commit changes to make sure data is deleted
        print("Data deleted successfully from syntheticTable.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()  # Rollback in case of any error
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    delete_data_from_table()
