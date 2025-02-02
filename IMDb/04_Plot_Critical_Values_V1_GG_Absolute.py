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
        self.df.columns = self.df.columns.str.strip()
        self.df = self.df.dropna()

        self.df['Estimated Rows'] = pd.to_numeric(self.df['Estimated Rows'], errors='coerce')
        self.df['Actual Rows'] = pd.to_numeric(self.df['Actual Rows'], errors='coerce')


        self.df = self.df.dropna(subset=['Estimated Rows', 'Actual Rows'])

    def calculate_deviation(self):
        # Calculate the deviation for each row
        self.df['Deviation (in rows)'] =  self.df['Estimated Rows'] - self.df['Actual Rows']

        # Calculate the cumulative deviation for each 'Query Name'
        self.df['Cumulative Deviation'] = self.df.groupby('Query Name')['Deviation (in rows)'].cumsum()

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
        plt.title('absolute misestimations')
        plt.xlabel('Query Name')
        plt.xticks(rotation=45, ha='right')
        plt.ylabel('Deviation (in rows)')

        # Adjust x-axis labels: Only show every second label that ends with "a"
        x_labels = self.df['Query Name'].unique()
        labeled_ticks = [label if (i % 2 == 0) else '' for i, label in enumerate(x_labels)]
        plt.xticks(ticks=range(len(x_labels)), labels=labeled_ticks, rotation=45, ha='right', fontsize=10)

        # Set grid with checkered background
        plt.grid(True, linestyle='--', linewidth=0.5)
        plt.gca().set_facecolor('whitesmoke')  # Set the background color to be a light gray for the checkered look

        # Show plot
        plt.tight_layout()
        plt.show()
        print("END")

    def analyze_and_plot(self):
        self.filter_queries()
        self.calculate_deviation()
        self.plot_deviation()


# Example usage:
#analyzer = QueryAnalyzer('/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/CRITICAL_values_no_limit.csv')
analyzer = QueryAnalyzer('/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/CRITICAL_values_no_limit_Q8d.csv')
analyzer.analyze_and_plot()
