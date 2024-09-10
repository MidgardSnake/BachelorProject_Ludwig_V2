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

    # Run ANALYZE command on table1
    cur.execute("ANALYZE synthetictable;")

    # Queries to fetch table statistics
    tables = ['synthetictable']
    for table in tables:
        print(f"Statistics for {table}:")
        cur.execute("""
        SELECT *
        FROM pg_stats
        WHERE tablename = %s;
        """, (table,))

        # Fetch and print the result
        results = cur.fetchall()
        if results:
            # Create a PrettyTable
            table_output = PrettyTable()
            # Add columns to the table
            table_output.field_names = [desc[0] for desc in cur.description]
            # Add rows to the table
            for row in results:
                table_output.add_row(row)
            # Print the table with a nice format
            print(table_output)
        else:
            print("No data found.")
        print("\n")  # Add a newline for better separation

    # Close cursor and connection
    cur.close()
    conn.close()


# Call the function
analyze_and_fetch_stats()
