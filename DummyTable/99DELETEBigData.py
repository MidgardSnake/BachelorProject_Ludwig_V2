import psycopg2

class DatabaseManager:
    def __init__(self, host, database, user, password, port=5432):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        """ Verbindung zur Datenbank herstellen. """
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Datenbankverbindung erfolgreich hergestellt.")
        except Exception as e:
            print(f"Fehler bei der Verbindung zur Datenbank: {e}")

    def delete_from_table(self, table_name):
        """ Löscht alle Daten aus einer spezifischen Tabelle. """
        try:
            query = f"DELETE FROM {table_name};"
            self.cursor.execute(query)
            self.connection.commit()  # Änderungen in der Datenbank speichern
            print(f"Alle Daten aus {table_name} wurden gelöscht.")
        except Exception as e:
            self.connection.rollback()  # Im Fehlerfall Änderungen zurücknehmen
            print(f"Fehler beim Löschen der Daten aus {table_name}: {e}")

    def close_connection(self):
        """ Schließt die Datenbankverbindung. """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Datenbankverbindung wurde geschlossen.")

# Anwendungsbeispiel
if __name__ == "__main__":
    db_manager = DatabaseManager('localhost', 'postgres', 'postgres', 'DKBLV1993')
    db_manager.connect()  # Verbindung zur Datenbank herstellen
    db_manager.delete_from_table('table1')  # Daten aus table1 löschen
    db_manager.delete_from_table('table2')  # Daten aus table2 löschen
    db_manager.delete_from_table('table3')  # Daten aus table3 löschen
    db_manager.close_connection()  # Verbindung schließen
