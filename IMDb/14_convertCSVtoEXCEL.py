import pandas as pd


# Definieren einer Klasse, um eine CSV-Datei in eine Excel-Datei zu konvertieren
class CSVToExcelConverter:
    def __init__(self, dataframe, output_excel_file):
        self.dataframe = dataframe
        self.output_excel_file = output_excel_file

    def convert_to_excel(self):
        # Schreiben der Daten in eine Excel-Datei
        with pd.ExcelWriter(self.output_excel_file, engine='xlsxwriter') as writer:
            # DataFrame in Excel-Datei schreiben
            self.dataframe.to_excel(writer, index=False, sheet_name='Data')

            # Optional: Formatierungen oder weitere Sheets hinzufügen
            workbook = writer.book
            worksheet = writer.sheets['Data']

            # Setzt die Spaltenbreiten, um die Excel-Datei übersichtlicher zu machen
            for i, col in enumerate(self.dataframe.columns):
                max_len = max(self.dataframe[col].astype(str).map(len).max(), len(col)) + 2
                worksheet.set_column(i, i, max_len)

        print(f"Excel-Datei wurde erfolgreich erstellt: {self.output_excel_file}")


# Hauptteil des Codes
if __name__ == "__main__":
    # Pfad zur Eingabe-CSV-Datei
    input_csv_file = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/dbOutputStatisticsCUTTED.csv'  # Ersetze mit dem tatsächlichen Pfad

    # Lesen der CSV-Datei in ein DataFrame
    df = pd.read_csv(input_csv_file)

    # Pfad zur Ausgabedatei
    output_excel_file = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/dbOutputStatisticsCUTTED.xlsx'  # Ersetze mit dem tatsächlichen Pfad

    # Initialisieren des Konverters und Konvertieren der CSV in eine Excel-Datei
    converter = CSVToExcelConverter(df, output_excel_file)
    converter.convert_to_excel()
