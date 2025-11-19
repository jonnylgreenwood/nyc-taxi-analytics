CREATE SCHEMA IF NOT EXISTS l2;

CREATE OR REPLACE TABLE l2.fact_trips (
    vendor_id INTEGER,
    affiliated_base_id VARCHAR,
    pickup_ts TIMESTAMP,
    dropoff_ts TIMESTAMP,
    passenger_count INTEGER,
    trip_distance_mi DOUBLE,
    rate_code_id INTEGER,
    shared_ride_flag BOOLEAN,
    store_and_fwd_flag VARCHAR,
    pickup_location_id INTEGER,
    dropoff_location_id INTEGER,
    payment_type INTEGER,
    fare_amount DOUBLE,
    extra_fees DOUBLE,
    mta_tax DOUBLE,
    tip_amount DOUBLE,
    tolls_amount DOUBLE,
    total_amount DOUBLE,
    improvement_surcharge DOUBLE,
    congestion_surcharge DOUBLE,
    cbd_congestion_fee DOUBLE,
    airport_fee DOUBLE,
    dispatch_base_id VARCHAR,
    ehail_fee DOUBLE,
    hail_service_flag INTEGER,

    source_type VARCHAR,
    _ingestion_month VARCHAR,

    pickup_date DATE,
    pickup_hour INTEGER,
    pickup_dayofweek INTEGER,
    dropoff_date DATE,
    trip_duration_minutes INTEGER
);