import pyarrow.parquet as pq

file_path = "data/raw/yellow_tripdata_2025-09.parquet"

print("Open file:", file_path)
table = pq.read_table(file_path, columns=None)  # all columns
print("Rows:", table.num_rows)
print("Columns:", table.num_columns)
print("Column names & types:")
for name, dtype in zip(table.column_names, table.schema.types):
    print(f"  {name}: {dtype}")

# Simple checks
import pandas as pd
df = table.to_pandas(use_threads=True)
print("Null counts for key cols:")
print(df[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count']].isna().sum())

print("Min/Max trip_distance, fare_amount:")
print(df['trip_distance'].min(), df['trip_distance'].max())
print(df['fare_amount'].min(), df['fare_amount'].max())
