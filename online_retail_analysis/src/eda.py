import pandas as pd

def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe(include="all")

def missing_values_report(df: pd.DataFrame) -> pd.DataFrame:
    report = df.isnull().sum().reset_index()
    report.columns = ["column_name", "missing_count"]
    return report

def category_analysis(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("category", as_index=False)
          .agg(total_orders=("order_id", "count"),
               total_quantity=("quantity", "sum"),
               total_final_revenue=("final_revenue", "sum"))
          .sort_values("total_final_revenue", ascending=False)
    )

def region_analysis(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("region", as_index=False)
          .agg(total_orders=("order_id", "count"),
               total_final_revenue=("final_revenue", "sum"))
          .sort_values("total_final_revenue", ascending=False)
    )

def monthly_trend(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("month", as_index=False)
          .agg(total_final_revenue=("final_revenue", "sum"))
          .sort_values("month")
    )

def segment_analysis(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("segment", as_index=False)
          .agg(customer_count=("customer_id", "nunique"),
               total_final_revenue=("final_revenue", "sum"))
          .sort_values("total_final_revenue", ascending=False)
    )

def pivot_analysis(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(
        values="final_revenue",
        index="region",
        columns="category",
        aggfunc="sum",
        fill_value=0
    )
