import numpy as np
import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create calculated columns used for analysis."""
    df = df.copy()
    df["revenue"] = df["quantity"] * df["price"]
    df["discount_amount"] = df["revenue"] * df["discount"]
    df["final_revenue"] = df["revenue"] - df["discount_amount"]
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    df["segment"] = np.where(
        df["final_revenue"] > 500,
        "High",
        np.where(df["final_revenue"] > 200, "Medium", "Low")
    )
    return df
