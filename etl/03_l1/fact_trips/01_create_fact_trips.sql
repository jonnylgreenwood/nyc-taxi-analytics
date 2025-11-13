-- ==================================================
-- Create unified fact_trips table in L1
-- ==================================================

CREATE SCHEMA IF NOT EXISTS l1;

CREATE OR REPLACE TABLE l1.fact_yellow_trips (
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

    _ingestion_month VARCHAR,
    _l1_loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    _flag_null_passenger BOOLEAN,
    _flag_negative_fare BOOLEAN,
    _flag_impossible_distance BOOLEAN
);

CREATE OR REPLACE TABLE l1.fact_green_trips (
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

    _ingestion_month VARCHAR,
    _l1_loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    _flag_null_passenger BOOLEAN,
    _flag_negative_fare BOOLEAN,
    _flag_impossible_distance BOOLEAN
);
CREATE OR REPLACE TABLE l1.fact_fhv_trips (
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

    _ingestion_month VARCHAR,
    _l1_loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    _flag_null_passenger BOOLEAN,
    _flag_negative_fare BOOLEAN,
    _flag_impossible_distance BOOLEAN
);

SELECT * FROM l1.fact_yellow_trips;
SELECT * FROM l1.fact_green_trips;
SELECT * FROM l1.fact_fhv_trips;