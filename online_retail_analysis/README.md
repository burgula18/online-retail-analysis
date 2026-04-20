# online_retail_analysis

## Overview
This is a beginner-friendly Python data analysis project using **pandas** and **NumPy**.
The project uses a simple online retail dataset and demonstrates the full workflow:
- reading CSV files
- inspecting data
- handling missing values
- removing duplicates
- transforming columns
- performing aggregates
- doing exploratory data analysis (EDA)
- saving output files

## Project Structure
```bash
online_retail_analysis/
│
├── data/
│   └── sales_data.csv
├── notebooks/
│   └── retail_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── transformations.py
│   └── eda.py
├── outputs/
├── main.py
├── requirements.txt
└── README.md
```

## Dataset Columns
- `order_id`
- `order_date`
- `customer_id`
- `region`
- `category`
- `product`
- `quantity`
- `price`
- `discount`

## What This Project Covers

### Data Cleaning
- Checks missing values
- Fills missing `discount` values with the average discount
- Removes duplicate rows
- Converts `order_date` into datetime format

### Transformations
- Calculates `revenue`
- Calculates `discount_amount`
- Calculates `final_revenue`
- Creates a `month` column
- Creates a customer `segment` using NumPy

### Analysis
- Summary statistics
- Missing values report
- Category-wise revenue analysis
- Region-wise revenue analysis
- Monthly sales trend
- Segment analysis
- Pivot table by region and category

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the project
```bash
python main.py
```

## Output Files
The project generates these files in the `outputs/` folder:
- `cleaned_data.csv`
- `summary_statistics.csv`
- `missing_values_report.csv`
- `category_analysis.csv`
- `region_analysis.csv`
- `monthly_trend.csv`
- `segment_analysis.csv`
- `pivot_analysis.csv`

## Interview Explanation
You can describe this project like this:

> I built a Python data analysis project using pandas and NumPy on an online retail dataset. I loaded CSV data, handled missing values, removed duplicates, created calculated columns like revenue and customer segments, and performed EDA using groupby aggregations and pivot tables to generate business insights.

## Skills Used
- Python
- pandas
- NumPy
- Data cleaning
- EDA
- Aggregations
- Pivot tables
- Feature engineering
