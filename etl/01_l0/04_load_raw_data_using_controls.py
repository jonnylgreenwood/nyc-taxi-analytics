import duckdb
import pandas as pd

# Connect to your persistent DB
con = duckdb.connect('analytics.db')

# Load ingestion plan
plan = con.execute("""
    SELECT file_month, file_path
    FROM dq.ingestion_plan
    WHERE is_loaded = FALSE;
""").fetch_df()

if plan.empty:
    print("✅ Nothing to load!")
else:
    for _, row in plan.iterrows():
        file_month = row['file_month']
        file_path = row['file_path']
        table_name = f"l0.yellow_trip_{file_month.replace('-', '_')}"

        print(f"📥 Loading {file_path} → {table_name}")

        # Load raw Parquet file
        con.execute(f"""
            CREATE OR REPLACE TABLE {table_name} AS
            SELECT * FROM parquet_scan('{file_path}');
        """)

        # Add ingestion metadata
        con.execute(f"""
            ALTER TABLE {table_name}
            ADD COLUMN _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
        """)

        con.execute(f"""
            ALTER TABLE {table_name}
            ADD COLUMN _source_file VARCHAR DEFAULT '{file_path}';
        """)

        # Update ingestion plan tracking
        con.execute(f"""
            UPDATE dq.ingestion_plan
            SET is_loaded = TRUE,
                loaded_at = CURRENT_TIMESTAMP
            WHERE file_month = '{file_month}';
        """)

    print("✅ All new files ingested successfully!")

# Close
con.close()
