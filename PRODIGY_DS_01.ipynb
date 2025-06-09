import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class PopulationAnalyzer:
    """
    A class to fetch, analyze, and visualize population data from the World Bank API.
    """
    def __init__(self, year=2022):
        self.year = year
        self.data = None
    
    def fetch_population_data(self):
        """
        Fetches population data from the World Bank API for the specified year.
        """
        try:
            print(f"📊 Fetching population data for the year {self.year}...")
            url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL"
            params = {
                "format": "json",
                "date": str(self.year),
                "per_page": "300"
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()[1]

            # Create a DataFrame and process data
            df = pd.DataFrame(data)
            df = df[['country', 'value']]
            df['country'] = df['country'].apply(lambda x: x['value'])
            df = df.dropna()
            df['value'] = df['value'] / 1e6  # Convert to millions

            self.data = df
            print("✅ Data fetched successfully.")
        except Exception as e:
            print(f"❌ Error fetching data: {e}")
            self.data = pd.DataFrame()

    def visualize_population(self, top_n=10):
        """
        Visualizes the top N most populous countries using a bar chart.
        """
        if self.data is None or self.data.empty:
            print("❌ No data to visualize. Please fetch data first.")
            return
        
        try:
            # Sort and select top N countries
            top_countries = self.data.sort_values(by='value', ascending=False).head(top_n)
            
            # Set up Seaborn style
            sns.set_theme(style="whitegrid")
            plt.figure(figsize=(12, 7))
            bars = sns.barplot(
                x='value', y='country', data=top_countries,
                palette='viridis', edgecolor='black'
            )

            # Add value labels on bars
            for index, value in enumerate(top_countries['value']):
                plt.text(value, index, f'{value:.2f}M', va='center', fontsize=10, fontweight='bold')

            # Title and labels
            plt.title(f'Top {top_n} Most Populous Countries ({self.year})', fontsize=18, fontweight='bold')
            plt.xlabel('Population (Millions)', fontsize=14)
            plt.ylabel('Country', fontsize=14)
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"❌ Error during visualization: {e}")

# ----------------- Main Execution -----------------
if __name__ == "__main__":
    # Initialize the PopulationAnalyzer
    year = 2022  # Change the year if needed
    analyzer = PopulationAnalyzer(year)

    # Fetch and visualize population data
    analyzer.fetch_population_data()
    analyzer.visualize_population(top_n=10)
