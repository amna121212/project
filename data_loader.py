import pandas as pd
import os

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        """Loads the data from the CSV file into a pandas DataFrame."""
        try:
            if not os.path.exists(self.filepath):
                raise FileNotFoundError(f"File not found at: {self.filepath}")
            data = pd.read_csv(self.filepath)
            print(f"Data loaded successfully with shape: {data.shape}")
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

if __name__ == "__main__":
    loader = DataLoader("Largest_Companies.csv")
    df = loader.load_data()

