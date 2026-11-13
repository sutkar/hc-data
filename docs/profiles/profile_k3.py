import os
import duckdb
import pandas as pd

# Connect to the shared DuckDB warehouse (located in hc-platform/warehouse/)
db_path = "C:\\Users\\ASUS\\source\\repos\\Healthcare ML\\hc-platform\\warehouse\\hc.duckdb"
print(f"Connecting to DuckDB at {db_path}...")
conn = duckdb.connect(db_path)

# Load raw_readmission into a pandas dataframe
df = conn.execute("SELECT * FROM raw_readmission").fetchdf()
conn.close()

print("=== DATASET K3 PROFILE SUMMARY ===")
print(f"Total Rows: {len(df)}")
print(f"Total Columns: {len(df.columns)}")
print("\n--- Column Names, Data Types, and Missing Values ---")

profile_data = []
for col in df.columns:
    null_count = df[col].isnull().sum()
    null_pct = (null_count / len(df)) * 100
    dtype = df[col].dtype
    profile_data.append({
        "Column": col, 
        "Type": str(dtype), 
        "Missing Count": null_count, 
        "Missing %": round(null_pct, 2)
    })

profile_df = pd.DataFrame(profile_data)
print(profile_df.to_string(index=False))

# Ensure the destination directory exists automatically
profile_path = "docs/profiles/k3_profile.md"
os.makedirs(os.path.dirname(profile_path), exist_ok=True)

# Save profile to markdown file
with open(profile_path, "w", encoding="utf-8") as f:
    f.write("# Dataset K3 Profile: hospital_readmission_risk_dataset.csv\n\n")
    f.write(f"- **Total Rows:** {len(df)}\n")
    f.write(f"- **Total Columns:** {len(df.columns)}\n\n")
    f.write("## Columns\n")
    f.write(profile_df.to_markdown(index=False))

print(f"\nProfile successfully saved to {profile_path}!")