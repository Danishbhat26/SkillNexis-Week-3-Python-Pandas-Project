"""
Week 3 Project: Data Cleaning and Analysis with Pandas
Run from the project folder:
    pip install -r requirements.txt
    python week3_data_cleaning.py
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Load and inspect the original dataset
df = pd.read_csv(DATA_DIR / "raw_data.csv")
print("Original data (first 5 rows):")
print(df.head())
print("\nMissing values before cleaning:")
print(df.isna().sum())

# 2. Standardize column names and remove exact duplicate records
df.columns = df.columns.str.strip().str.lower()
df = df.drop_duplicates().copy()

# 3. Convert columns to appropriate data types
for col in ["duration", "pulse", "maxpulse", "calories"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 4. Handle missing values
# Fill missing numeric values with each column's median.
for col in ["duration", "pulse", "maxpulse", "calories"]:
    df[col] = df[col].fillna(df[col].median())

# Rows with missing dates cannot be used for date-based analysis, so remove them.
df = df.dropna(subset=["date"]).copy()

# 5. Filter rows: keep workouts with duration between 30 and 120 minutes.
# The 450-minute value is retained in raw_data.csv but excluded here as an outlier.
cleaned = df[df["duration"].between(30, 120)].copy()

# 6. Create new columns
cleaned["calories_per_minute"] = (
    cleaned["calories"] / cleaned["duration"]
).round(2)
cleaned["pulse_category"] = np.where(
    cleaned["pulse"] >= 110, "High Pulse", "Normal Pulse"
)
cleaned["workout_year"] = cleaned["date"].dt.year

# 7. Save cleaned data
cleaned.to_csv(DATA_DIR / "cleaned_data.csv", index=False)

print("\nMissing values after cleaning:")
print(cleaned.isna().sum())
print("\nCleaned data summary:")
print(cleaned.describe(numeric_only=True))
print(f"\nOriginal rows after duplicate removal: {len(df)}")
print(f"Rows in cleaned dataset: {len(cleaned)}")

# 8. Visualize calorie distribution
sns.set_theme()
plt.figure(figsize=(8, 5))
sns.histplot(data=cleaned, x="calories", kde=True)
plt.title("Distribution of Calories Burned")
plt.xlabel("Calories")
plt.ylabel("Number of Workouts")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "calories_chart.png", dpi=150)
plt.close()

# 9. Visualize workout duration versus calories
plt.figure(figsize=(8, 5))
sns.scatterplot(data=cleaned, x="duration", y="calories", hue="pulse_category")
plt.title("Workout Duration vs Calories Burned")
plt.xlabel("Duration (minutes)")
plt.ylabel("Calories")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "duration_vs_calories.png", dpi=150)
plt.close()

print("\nDone! Cleaned CSV and charts have been saved.")
