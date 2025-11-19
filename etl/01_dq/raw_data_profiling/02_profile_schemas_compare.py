import duckdb
import glob
import pandas as pd
from pathlib import Path

con = duckdb.connect()

# Where you downloaded the Parquet samples
files = sorted(glob.glob("data/raw/*tripdata_*.parquet"))

profile_records = []

print("📊 Profiling schema of sampled Parquet files...\n")

for fp in files:
    filename = Path(fp).name  # e.g. "yellow_tripdata_2025-07.parquet"

    # Extract dataset type + YYYY-MM
    dataset_type = filename.split('_')[0]  # yellow, green, fhv, hvfhv
    ym = filename.split('_')[-1].replace('.parquet', '')  # 2025-07

    print(f"→ Profiling {dataset_type:6} {ym} ...")

    # Zero-row scan: DuckDB reads schema only


    try:
        schema_df = con.execute(
            f"DESCRIBE SELECT * FROM parquet_scan('{fp}')"
        ).fetch_df()
    except Exception as e:
        print(f"⚠️ Skipping corrupt file: {fp}")
        continue

    for _, row in schema_df.iterrows():
        profile_records.append({
            "dataset": dataset_type,
            "month": ym,
            "column_name": row['column_name'],
            "column_type": row['column_type']
        })

print("\n✅ Schema profiling complete.")

# Convert to DataFrame
profile_df = pd.DataFrame(profile_records)

# Create pivot table: side-by-side comparison
pivot = profile_df.pivot_table(
    index="column_name",
    columns="dataset",
    values="column_type",
    aggfunc=lambda x: ", ".join(sorted(set(x)))
)

pivot = pivot.sort_index()

# Output results
output_csv = "docs/schema_comparison.csv"
output_md  = "docs/schema_comparison.md"

pivot.to_csv(output_csv)
pivot.to_markdown(output_md)

print(f"📁 Saved side-by-side schema comparison to:")
print(f"   CSV: {output_csv}")
print(f"   MD:  {output_md}")
