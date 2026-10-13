# SkillNexis Week 3 — Python and Pandas Data Cleaning

## Project overview
This project demonstrates basic Python scripting, Pandas data manipulation, and introductory data visualization using a workout dataset.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Tasks completed
1. Loaded a CSV file with Pandas.
2. Inspected and reported missing values.
3. Standardized column names and removed exact duplicate rows.
4. Converted numeric columns and dates to suitable data types.
5. Filled missing numeric values using column medians.
6. Removed rows with missing dates.
7. Filtered workout durations to 30–120 minutes. The 450-minute record is excluded as a likely outlier.
8. Created `calories_per_minute`, `pulse_category`, and `workout_year` columns.
9. Exported the cleaned dataset.
10. Created visualizations with Matplotlib and Seaborn.

## Project files
- `data/raw_data.csv` — source data recreated from the provided spreadsheet screenshot.
- `data/cleaned_data.csv` — cleaned and filtered dataset.
- `week3_data_cleaning.py` — reproducible Python script.
- `outputs/calories_chart.png` — calorie distribution chart.
- `outputs/duration_vs_calories.png` — duration versus calories chart.
- `requirements.txt` — required Python packages.

## How to run
Install dependencies:
```bash
pip install -r requirements.txt
```

Run the script from this folder:
```bash
python week3_data_cleaning.py
```

## Note on data accuracy
The original spreadsheet was provided as a screenshot, not as a CSV or Excel attachment. Therefore, `raw_data.csv` was recreated from the visible rows and values; some dates were not fully visible in the screenshot. Please compare the CSV with your original spreadsheet before submitting if exact source-data accuracy is required.

## Learning outcomes
This project practices CSV reading, data inspection, missing-value handling, duplicate removal, type conversion, filtering, feature creation, and plotting.
