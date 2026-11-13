import duckdb
import os

# Define paths relative to hc-data folder
db_path = "../warehouse/hc.duckdb"
csv_path = "raw/hospital_readmission_risk_dataset.csv"

print(f"Connecting to DuckDB at {db_path}...")
conn = duckdb.connect(db_path)

print(f"Loading {csv_path} into raw table...")
# Create a raw table from the CSV file
conn.execute(f"""
    CREATE OR REPLACE TABLE raw_readmission AS 
    SELECT * FROM read_csv_auto('{csv_path}');
""")

# Verify row count
row_count = conn.execute("SELECT COUNT(*) FROM raw_readmission;").fetchone()[0]
print(f"Successfully loaded {row_count} rows into raw_readmission table!")

conn.close()