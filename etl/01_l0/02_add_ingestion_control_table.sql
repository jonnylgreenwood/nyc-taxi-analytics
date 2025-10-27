DROP TABLE IF EXISTS dq.ingestion_plan;

CREATE TABLE dq.ingestion_plan (
    service_type VARCHAR,
    file_month VARCHAR,
    file_path VARCHAR,
    is_loaded BOOLEAN DEFAULT FALSE,
    loaded_at TIMESTAMP,
    PRIMARY KEY (service_type, file_month)
);
