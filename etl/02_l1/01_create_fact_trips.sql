-- ==================================================
-- Create unified fact_trips table in L1
-- ==================================================

CREATE SCHEMA IF NOT EXISTS l1;

CREATE OR REPLACE TABLE l1.fact_trips (
    vendor_id INTEGER,
    tpep_pickup_datetime TIMESTAMP,
    tpep_dropoff_datetime TIMESTAMP,
    passenger_count INTEGER,
    trip_distance DOUBLE,
    ratecodeid INTEGER,
    store_and_fwd_flag VARCHAR,
    pulocationid INTEGER,
    dolocationid INTEGER,
    payment_type INTEGER,
    fare_amount DOUBLE,
    extra DOUBLE,
    mta_tax DOUBLE,
    tip_amount DOUBLE,
    tolls_amount DOUBLE,
    improvement_surcharge DOUBLE,
    total_amount DOUBLE,
    congestion_surcharge DOUBLE,
    airport_fee DOUBLE,
    cbd_congestion_fee DOUBLE,

    -- ✅ Lineage / Governance
    _ingestion_month VARCHAR,
    _l1_loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- ✅ Initial Data Quality Flags (nullable now)
    _flag_null_passenger BOOLEAN,
    _flag_negative_fare BOOLEAN,
    _flag_invalid_distance BOOLEAN
);
