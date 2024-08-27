import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class QueryAnalyzer:
    def __init__(self, csv_file):
        try:
            # Attempt to read the CSV file, specifying the delimiter and encoding
            self.df = pd.read_csv(csv_file, delimiter=',', encoding='utf-8')
        except Exception as e:
            print(f"Error reading the file: {e}")
            raise

    def calculate_deviation(self):
        # Remove whitespace from column names and clean data
        self.df.columns = self.df.columns.str.strip()
        self.df = self.df.dropna()

        # Convert the 'Estimated Rows' and 'Actual Rows' to numeric, coercing errors
        self.df['Estimated Rows'] = pd.to_numeric(self.df['Estimated Rows'], errors='coerce')
        self.df['Actual Rows'] = pd.to_numeric(self.df['Actual Rows'], errors='coerce')

        # Drop rows where conversion to numeric failed
        self.df = self.df.dropna(subset=['Estimated Rows', 'Actual Rows'])

        # Calculate percentage deviation
        self.df['Deviation (%)'] = (self.df['Actual Rows'] - self.df['Estimated Rows']).abs() / self.df[
            'Estimated Rows'] * 100

        # Group by Query Name and Node Type, then calculate mean deviation
        self.result = self.df.groupby(['Query Name', 'Node Type'])['Deviation (%)'].mean().reset_index()

    def plot_deviation(self):
        # Set the figure size
        plt.figure(figsize=(12, 6))

        # Create a boxplot for each query
        sns.boxplot(x='Query Name', y='Deviation (%)', data=self.df, showfliers=False)

        # Set the title and labels
        plt.title('Deviation Between Estimated and Actual Rows by Query')
        plt.xlabel('Query Name')
        plt.xticks(rotation=45, ha='right')
        plt.ylabel('Deviation (%)')

        # Show plot
        plt.tight_layout()
        plt.show()

    def analyze_and_plot(self):
        self.calculate_deviation()
        self.plot_deviation()

# Example usage:
analyzer = QueryAnalyzer('/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/CRITICAL_values_V2.csv')
analyzer.analyze_and_plot()
