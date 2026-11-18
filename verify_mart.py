import duckdb

# Connect to the shared warehouse
conn = duckdb.connect("../warehouse/hc.duckdb")

# Check row counts between raw and semantic mart
raw_count = conn.execute("SELECT COUNT(*) FROM raw_readmission").fetchone()[0]
mart_count = conn.execute("SELECT COUNT(*) FROM sv_encounters").fetchone()[0]

# Check readmission rate breakdown
readmit_rate = conn.execute("""
    SELECT 
        readmitted, 
        COUNT(*) as cnt, 
        ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM sv_encounters), 2) as pct 
    FROM sv_encounters 
    GROUP BY readmitted
\n    """).fetchall()

conn.close()

print(f"--- DATA CHECK VERIFICATION ---")
print(f"Raw Rows: {raw_count}")
print(f"Semantic Mart Rows: {mart_count}")
print(f"Match Status: {'PASS' if raw_count == mart_count else 'FAIL'}")
print(f"\nReadmission Rate Distribution:")
for row in readmit_rate:
    print(f"  Readmitted = {row[0]}: {row[1]} rows ({row[2]}%)")