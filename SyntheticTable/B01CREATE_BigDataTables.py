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

    def create_table_base(self, table_name):
        if self.conn is not None:
            with self.conn.cursor() as cursor:
                try:
                    query = sql.SQL(
                        "CREATE TABLE {table_name} (ref3 INT, id INT, ref2 INT);"
                    ).format(table_name=sql.Identifier(table_name))
                    print(f"Executing query: {query.as_string(self.conn)}")
                    cursor.execute(query)
                    self.conn.commit()
                    print(f"Table {table_name} created successfully.")
                except psycopg2.Error as e:
                    print(f"Failed to create table {table_name}: {e}")
                    self.conn.rollback()

    def create_table_ref(self, table_name):
        if self.conn is not None:
            with self.conn.cursor() as cursor:
                try:
                    query = sql.SQL(
                        "CREATE TABLE {table_name} (id INT, a INT, b INT);"
                    ).format(table_name=sql.Identifier(table_name))
                    print(f"Executing query: {query.as_string(self.conn)}")
                    cursor.execute(query)
                    self.conn.commit()
                    print(f"Table {table_name} created successfully.")
                except psycopg2.Error as e:
                    print(f"Failed to create table {table_name}: {e}")
                    self.conn.rollback()

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Usage
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'DKBLV1993'
}
db_manager = DatabaseManager(**db_params)
db_manager.connect()
db_manager.create_table_base('tablex1')  # tableX1 with ref3, id, and ref2
db_manager.create_table_ref('tablex2')  # tableX2 with id, a, and b
db_manager.create_table_ref('tablex3')  # tableX3 with id, a, and b
db_manager.close()
