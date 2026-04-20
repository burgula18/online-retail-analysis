from pathlib import Path

from src.data_loader import load_data
from src.data_cleaning import (
    inspect_data,
    handle_missing_values,
    remove_duplicates,
    convert_data_types,
)
from src.transformations import add_features
from src.eda import (
    summary_statistics,
    missing_values_report,
    category_analysis,
    region_analysis,
    monthly_trend,
    segment_analysis,
    pivot_analysis,
)

def main() -> None:
    base_path = Path(__file__).resolve().parent
    data_path = base_path / "data" / "sales_data.csv"
    output_path = base_path / "outputs"
    output_path.mkdir(exist_ok=True)

    df = load_data(data_path)
    inspect_data(df)

    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = convert_data_types(df)
    df = add_features(df)

    # Save cleaned dataset
    df.to_csv(output_path / "cleaned_data.csv", index=False)

    # Save analysis outputs
    summary_statistics(df).to_csv(output_path / "summary_statistics.csv")
    missing_values_report(df).to_csv(output_path / "missing_values_report.csv", index=False)
    category_analysis(df).to_csv(output_path / "category_analysis.csv", index=False)
    region_analysis(df).to_csv(output_path / "region_analysis.csv", index=False)
    monthly_trend(df).to_csv(output_path / "monthly_trend.csv", index=False)
    segment_analysis(df).to_csv(output_path / "segment_analysis.csv", index=False)
    pivot_analysis(df).to_csv(output_path / "pivot_analysis.csv")

    print("\nProject executed successfully.")
    print(f"Outputs saved to: {output_path}")

if __name__ == "__main__":
    main()
