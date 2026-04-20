import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load CSV data into a pandas DataFrame."""
    df = pd.read_csv(path)
    print("Data loaded successfully.")
    print(f"Shape: {df.shape}")
    return df
