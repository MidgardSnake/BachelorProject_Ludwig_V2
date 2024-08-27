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
        # Filter for queries that end with 'a', using a regex pattern
        self.df = self.df[self.df['Query Name'].apply(lambda x: bool(re.match(r'.*a\.sql', x)))]
        # Remove whitespace from column names and clean data
        self.df.columns = self.df.columns.str.strip()
        self.df = self.df.dropna()

        # Convert the 'Estimated Rows' and 'Actual Rows' to numeric, coercing errors
        self.df['Estimated Rows'] = pd.to_numeric(self.df['Estimated Rows'], errors='coerce')
        self.df['Actual Rows'] = pd.to_numeric(self.df['Actual Rows'], errors='coerce')

        # Drop rows where conversion to numeric failed
        self.df = self.df.dropna(subset=['Estimated Rows', 'Actual Rows'])

    def calculate_deviation(self):
        # Calculate percentage deviation
        self.df['Deviation (%)'] = (self.df['Actual Rows'] - self.df['Estimated Rows']).abs() / self.df['Estimated Rows'] * 100

        # Group by Query Name and Node Type, then calculate mean deviation
        self.result = self.df.groupby(['Query Name', 'Node Type'])['Deviation (%)'].mean().reset_index()

    def plot_deviation(self):
        # Sort the queries by their name in ascending order
        self.df['Query Name'] = pd.Categorical(self.df['Query Name'], ordered=True,
                                               categories=sorted(self.df['Query Name'].unique()))

        # Set the figure size
        plt.figure(figsize=(14, 7))

        # Create a boxplot for each query, colored by Node Type
        sns.boxplot(x='Query Name', y='Deviation (%)', hue='Node Type', data=self.df, showfliers=False, palette="Set2")

        # Set the title and labels
        plt.title('Deviation Between Estimated and Actual Rows by Query')
        plt.xlabel('Query Name')
        plt.xticks(rotation=45, ha='right')
        plt.ylabel('Deviation (%)')

        # Add a legend to explain the color coding for Node Types
        plt.legend(title='Node Type', loc='upper right')

        # Show plot
        plt.tight_layout()
        plt.show()

    def analyze_and_plot(self):
        self.filter_queries()
        self.calculate_deviation()
        self.plot_deviation()

# Example usage:
analyzer = QueryAnalyzer('/IMDb/Resultfiles/CRITICAL_values_bias2.0.csv')
analyzer.analyze_and_plot()
