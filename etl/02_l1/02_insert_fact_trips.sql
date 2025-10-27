INSERT INTO l1.fact_trips (
    vendor_id, tpep_pickup_datetime, tpep_dropoff_datetime,
    passenger_count, trip_distance, ratecodeid,
    store_and_fwd_flag, pulocationid, dolocationid,
    payment_type, fare_amount, extra, mta_tax,
    tip_amount, tolls_amount, improvement_surcharge,
    total_amount, congestion_surcharge, airport_fee,
    cbd_congestion_fee,
    _ingestion_month
)
SELECT
    VendorID,
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    passenger_count,
    trip_distance,
    RatecodeID,
    store_and_fwd_flag,
    PULocationID,
    DOLocationID,
    payment_type,
    fare_amount,
    extra,
    mta_tax,
    tip_amount,
    tolls_amount,
    improvement_surcharge,
    total_amount,
    congestion_surcharge,
    Airport_fee,
    cbd_congestion_fee,
    '2025-09' AS _ingestion_month
FROM l0.yellow_trip_2025_09;
