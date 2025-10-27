import os
import duckdb
import pandas as pd

con = duckdb.connect('etl/analytics.duckdb')

plan = con.execute("""
    SELECT file_month, file_path
    FROM dq.ingestion_plan;
""").fetch_df()

if plan.empty:
    print("✅ Nothing to load!")
else:
    for _, row in plan.iterrows():
        file_month = row['file_month']  # YYYY-MM
        file_path = row['file_path']

        # ✅ Extract service type from filename
        filename = os.path.basename(file_path)  # yellow_tripdata_2024-10.parquet
        service = filename.split('_')[0]       # "yellow", "green", "fhv"

        safe_month = file_month.replace('-', '_')
        table_name = f"l0.{service}_trip_{safe_month}"

        print(f"📥 Loading: {file_path} → {table_name}")

        con.execute(f"""
            CREATE OR REPLACE TABLE {table_name} AS
            SELECT * FROM parquet_scan('{file_path}');
        """)

        # Metadata
        con.execute(f"""
            ALTER TABLE {table_name}
            ADD COLUMN IF NOT EXISTS _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
        """)
        con.execute(f"""
            ALTER TABLE {table_name}
            ADD COLUMN IF NOT EXISTS _source_file VARCHAR DEFAULT '{file_path}';
        """)

        # Mark ingestion completed
        con.execute(f"""
            UPDATE dq.ingestion_plan
            SET is_loaded = TRUE,
                loaded_at = CURRENT_TIMESTAMP
            WHERE file_month = '{file_month}';
        """)

    print("✅ All new files ingested to L0!")

con.close()
