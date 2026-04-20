import pandas as pd

def inspect_data(df: pd.DataFrame) -> None:
    """Print basic inspection details."""
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing discount values with the column mean."""
    df = df.copy()
    discount_mean = df["discount"].mean()
    df["discount"] = df["discount"].fillna(discount_mean)
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    df = df.copy()
    return df.drop_duplicates()

def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """Convert order_date to datetime."""
    df = df.copy()
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df
