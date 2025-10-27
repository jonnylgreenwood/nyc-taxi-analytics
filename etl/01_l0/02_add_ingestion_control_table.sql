CREATE OR REPLACE TABLE dq.ingestion_plan (
    file_month VARCHAR PRIMARY KEY,
    file_path VARCHAR,
    is_loaded BOOLEAN DEFAULT FALSE,
    loaded_at TIMESTAMP
);
