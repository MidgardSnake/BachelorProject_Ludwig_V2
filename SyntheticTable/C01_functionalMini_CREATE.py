import psycopg2
from psycopg2 import sql

class DatabaseManager:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Database connection established.")
        except psycopg2.DatabaseError as e:
            print(f"An error occurred: {e}")
            self.conn = None

    def create_tables(self):
        if self.conn is not None:
            with self.conn.cursor() as cursor:
                try:
                    # Tabelle 1 erstellen
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS t1 (
                            id SERIAL PRIMARY KEY,
                            attribute1 TEXT
                        );
                    """)
                    # Tabelle 2 erstellen
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS t2 (
                            id SERIAL PRIMARY KEY,
                            ref_id INT REFERENCES t1(id),
                            attribute2 TEXT
                        );
                    """)
                    self.conn.commit()
                    print("Tables 'table1' and 'table2' created successfully.")
                except psycopg2.Error as e:
                    print(f"Failed to create tables: {e}")
                    self.conn.rollback()

    def insert_data(self):
        if self.conn is not None:
            with self.conn.cursor() as cursor:
                try:
                    # Daten in Tabelle 1 einfügen
                    cursor.executemany(
                        "INSERT INTO t1 (attribute1) VALUES (%s);",
                        [(f"value_{i}",) for i in range(1, 1000)]  # Werte von value_1 bis value_10
                    )
                    # Daten in Tabelle 2 einfügen
                    cursor.executemany(
                        "INSERT INTO t2 (ref_id, attribute2) VALUES (%s, %s);",
                        [(i, f"detail_{i}") for i in range(1, 1000)]  # Funktionale Abhängigkeit: ref_id -> table1.id
                    )
                    self.conn.commit()
                    print("Data inserted successfully into 'table1' and 'table2'.")
                except psycopg2.Error as e:
                    print(f"Failed to insert data: {e}")
                    self.conn.rollback()

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Hauptprogramm
if __name__ == "__main__":
    # Datenbankparameter
    db_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'DKBLV1993',
        'host': 'localhost',
        'port': 5432
    }

    db_manager = DatabaseManager(**db_params)
    db_manager.connect()

    # Tabellen erstellen und befüllen
    db_manager.create_tables()
    db_manager.insert_data()

    db_manager.close()
