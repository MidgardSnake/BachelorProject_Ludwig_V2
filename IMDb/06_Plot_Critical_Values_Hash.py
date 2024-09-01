import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re


class QueryAnalyzer:
    def __init__(self, csv_file):
        try:
            # Attempt to read the CSV file, specifying the delimiter and encoding
            self.df = pd.read_csv(csv_file, delimiter=',', encoding='utf-8')
        except Exception as e:
            print(f"Error reading the file: {e}")
            raise

    def filter_queries(self):
        # Filter for queries that end with 'sql', using a regex pattern
        self.df = self.df[self.df['Query Name'].apply(lambda x: bool(re.match(r'.*\.sql', x)))]

        # Further filter for rows where the Node Type is 'Seq Scan'
        self.df = self.df[self.df['Node Type'] == 'Hash']

        # Remove whitespace from column names and clean data
        self.df.columns = self.df.columns.str.strip()
        self.df = self.df.dropna()

        # Convert the 'Estimated Rows' and 'Actual Rows' to numeric, coercing errors
        self.df['Estimated Rows'] = pd.to_numeric(self.df['Estimated Rows'], errors='coerce')
        self.df['Actual Rows'] = pd.to_numeric(self.df['Actual Rows'], errors='coerce')

        # Drop rows where conversion to numeric failed
        self.df = self.df.dropna(subset=['Estimated Rows', 'Actual Rows'])

    def calculate_deviation(self):
        # Calculate amount deviation
        self.df['Deviation (in rows)'] = (self.df['Actual Rows'] - self.df['Estimated Rows'])

    def plot_deviation(self):
        # Extract the numeric part of the query name for sorting
        self.df['Query Number'] = self.df['Query Name'].str.extract(r'(\d+)').astype(int)

        # Sort the dataframe based on the query number
        self.df = self.df.sort_values(by='Query Number')

        # Set the figure size
        plt.figure(figsize=(12, 6))

        # Create a boxplot for each query
        sns.boxplot(x='Query Name', y='Deviation (in rows)', data=self.df, showfliers=False)

        # Set the title and labels
        plt.title('Deviation Between Estimated and Actual Rows for Hash by Query')
        plt.xlabel('Query Name')
        plt.xticks(rotation=45, ha='right')
        plt.ylabel('Deviation (in rows)')

        # Show plot
        plt.tight_layout()
        plt.show()

    def analyze_and_plot(self):
        self.filter_queries()
        self.calculate_deviation()
        self.plot_deviation()


# Example usage:
analyzer = QueryAnalyzer('/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/CRITICAL_values_bias1.01.csv')
analyzer.analyze_and_plot()
