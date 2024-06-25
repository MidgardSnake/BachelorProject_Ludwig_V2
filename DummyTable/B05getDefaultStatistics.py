import psycopg2
from prettytable import PrettyTable

def analyze_and_fetch_stats():
    # Connection data
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="DKBLV1993",
        host="localhost",
        port="5432"
    )

    # Create cursor to execute SQL commands
    cur = conn.cursor()

    # Tables to analyze and fetch statistics for
    tables = ['table1', 'table2', 'table3']
    for table in tables:
        # Run ANALYZE command on each table
        cur.execute(f"ANALYZE {table};")
        print(f"ANALYZE completed for {table}")

        # Queries to fetch table statistics
        print(f"Statistics for {table}:")
        cur.execute("""
        SELECT *
        FROM pg_stats
        WHERE tablename = %s;
        """, (table,))

        # Fetch and print the result
        columns = [desc[0] for desc in cur.description]
        results = cur.fetchall()
        if results:
            table_output = PrettyTable()
            table_output.field_names = columns
            for row in results:
                table_output.add_row(row)
            print(table_output)
        else:
            print("No data found.")
        print("\n")  # Add a newline for better separation

    # Close cursor and connection
    cur.close()
    conn.close()

# Call the function
analyze_and_fetch_stats()
