import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class QueryAnalyzer:
    def __init__(self, csv_file):
        try:
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

        # Ausschließen der Query '5b' von der Analyse
        self.df = self.df[~self.df['Query Name'].str.contains('5b')]

        # Ausschließen der Query '5b' von der Analyse
        self.df = self.df[~self.df['Query Name'].str.contains('5b')]

    def calculate_relative_frequency(self):
        # Berechnung der Summe der Estimated und Actual Rows je Query
        grouped_df = self.df.groupby('Query Name').agg({'Estimated Rows': 'sum', 'Actual Rows': 'sum'}).reset_index()

        # Berechnung der relativen Häufigkeit
        grouped_df['Relative Frequency'] = grouped_df['Estimated Rows'] / grouped_df['Actual Rows']

        # Sortierung nach numerischem und alphabetischem Teil von `Query Name`
        grouped_df['Query Number'] = grouped_df['Query Name'].str.extract(r'(\d+)').astype(int)
        grouped_df['Query Letter'] = grouped_df['Query Name'].str.extract(r'([a-zA-Z])')
        grouped_df = grouped_df.sort_values(by=['Query Number', 'Query Letter'])

        self.grouped_df = grouped_df

    def plot_relative_frequency(self):
        # Set the figure size
        plt.figure(figsize=(14, 8))

        # Create a bar plot for each query's relative frequency
        sns.barplot(x='Query Name', y='Relative Frequency', data=self.grouped_df)

        # Set the title and labels
        plt.title('Relative Frequency of Estimated Rows to Actual Rows per Query')
        plt.xlabel('Query Name')
        plt.ylabel('Relative Frequency')

        # Adjust x-axis labels: Only show every nth label and rotate them for better readability
        n_labels = len(self.grouped_df['Query Name'])
        step = 2  # Show every 2nd label
        plt.xticks(ticks=range(0, n_labels, step), labels=self.grouped_df['Query Name'][::step], rotation=90, ha='right')

        # Show plot
        plt.tight_layout()
        plt.show()

    def analyze_and_plot(self):
        self.filter_queries()
        self.calculate_relative_frequency()
        self.plot_relative_frequency()

# Example usage:
analyzer = QueryAnalyzer('/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/CRITICAL_values_no_limit.csv')
analyzer.analyze_and_plot()
