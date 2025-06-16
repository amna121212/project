import pandas as pd

class Preprocessor:
    def __init__(self, df):
        self.df = df

    def clean_data(self):
        """Basic preprocessing: drop NaNs and encode categorical columns."""
        try:
            df_cleaned = self.df.dropna()
            for column in df_cleaned.select_dtypes(include=['object']).columns:
                df_cleaned[column] = pd.factorize(df_cleaned[column])[0]
            print("Data preprocessing completed.")
            return df_cleaned
        except Exception as e:
            print(f"Error in preprocessing: {e}")
            return self.df

# Load the CSV file
file_path = r"C:\Users\HP\OneDrive\Documents\Desktop\project\Largest_Companies.csv"
df = pd.read_csv(file_path)

# Initialize and clean data
preprocessor = Preprocessor(df)
cleaned_df = preprocessor.clean_data()

# Show first few rows of cleaned data
print(cleaned_df.head())
