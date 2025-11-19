CREATE OR REPLACE TABLE l2.fact_trips AS
WITH unified AS (
    SELECT *, 'yellow' AS source_type FROM l1.fact_yellow_trips
    UNION ALL
    SELECT *, 'green'  AS source_type FROM l1.fact_green_trips
    UNION ALL
    SELECT *, 'fhv'    AS source_type FROM l1.fact_fhv_trips
),
derived AS (
    SELECT
        *,
        DATE_TRUNC('day', pickup_ts) AS pickup_date,
        EXTRACT(hour FROM pickup_ts) AS pickup_hour,
        EXTRACT(dow FROM pickup_ts)  AS pickup_dayofweek,
        DATE_TRUNC('day', dropoff_ts) AS dropoff_date,
        (EXTRACT(epoch FROM dropoff_ts) - EXTRACT(epoch FROM pickup_ts)) / 60 AS trip_duration_minutes
    FROM unified
)
SELECT
    ROW_NUMBER() OVER () AS trip_key,
    *,
    -- Core business rules
    COALESCE(NULLIF(passenger_count,0),1) AS passenger_count,
    (trip_distance_mi / NULLIF(trip_duration_minutes,0)) * 60 AS speed_mph,
FROM derived

 