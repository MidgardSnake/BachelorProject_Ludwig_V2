import pandas as pd

class QueryAnalyzer:
    def __init__(self, csv_file):
        try:
            # Attempt to read the CSV file, specifying the delimiter and encoding
            self.df = pd.read_csv(csv_file, delimiter=',', encoding='utf-8')
        except Exception as e:
            print(f"Error reading the file: {e}")
            raise

    def filter_queries(self):
        self.df.columns = self.df.columns.str.strip()
        self.df = self.df.dropna()

        self.df['Estimated Rows'] = pd.to_numeric(self.df['Estimated Rows'], errors='coerce')
        self.df['Actual Rows'] = pd.to_numeric(self.df['Actual Rows'], errors='coerce')

        self.df = self.df.dropna(subset=['Estimated Rows', 'Actual Rows'])

    def calculate_deviation(self):
        # Calculate the absolute deviation for each row
        self.df['Deviation (in rows)'] = (self.df['Actual Rows'] - self.df['Estimated Rows']).abs()

    def save_deviation_to_csv(self, output_file):
        # Save the dataframe with deviations to a new CSV file
        # Save the dataframe with deviations and other relevant columns to a new CSV file
        self.df[['Query Name', 'Relation Name', 'Node Type', 'Join Type', 'Scan Direction', 'Parent Node Type',
                 'Deviation (in rows)']].to_csv(output_file, index=False)
        print(f"Deviation data saved to {output_file}")

# Example usage:
# Initialize the analyzer with the path to the CSV file
#analyzer = QueryAnalyzer('/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/CRITICAL_values_no_limit.csv')
analyzer = QueryAnalyzer('/IMDb/Resultfiles/CRITICAL_values_no_limit_Q8d.csv')

# Filter and calculate deviations
analyzer.filter_queries()
analyzer.calculate_deviation()

# Save the deviations to a new CSV file
analyzer.save_deviation_to_csv('/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/Resultdifference.csv')

# Example paths for files can be replaced accordingly
